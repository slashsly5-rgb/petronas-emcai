"""Alert calculation utilities"""
import pandas as pd
from datetime import datetime, timedelta
import config

def calculate_inventory_alerts(df: pd.DataFrame) -> dict:
    """Calculate inventory-related alerts"""
    alerts = {
        'low_stock_critical': [],
        'low_stock_warning': [],
        'overdue_audit': []
    }

    for _, row in df.iterrows():
        # Low stock alerts
        if row['Stock_Qty'] < config.LOW_STOCK_CRITICAL:
            alerts['low_stock_critical'].append({
                'component_id': row['Component_ID'],
                'item_name': row['Item_Name'],
                'stock': row['Stock_Qty'],
                'location': row['Location']
            })
        elif row['Stock_Qty'] <= config.LOW_STOCK_WARNING:
            alerts['low_stock_warning'].append({
                'component_id': row['Component_ID'],
                'item_name': row['Item_Name'],
                'stock': row['Stock_Qty'],
                'location': row['Location']
            })

        # Overdue audit alerts
        try:
            last_audit = pd.to_datetime(row['Last_Audit'])
            days_since_audit = (datetime.now() - last_audit).days
            if days_since_audit > config.OVERDUE_AUDIT_DAYS:
                alerts['overdue_audit'].append({
                    'component_id': row['Component_ID'],
                    'item_name': row['Item_Name'],
                    'days_overdue': days_since_audit,
                    'last_audit': row['Last_Audit']
                })
        except:
            pass

    return alerts

def calculate_tool_alerts(df: pd.DataFrame) -> dict:
    """Calculate tool-related alerts"""
    alerts = {
        'overdue': [],
        'lost': [],
        'damaged': []
    }

    today = datetime.now()

    for _, row in df.iterrows():
        # Overdue tools
        if row['Status'] == 'Overdue':
            try:
                due_date = pd.to_datetime(row['Date_Due'])
                days_overdue = (today - due_date).days
                alerts['overdue'].append({
                    'tracking_id': row['Tracking_ID'],
                    'tool_name': row['Tool_Name'],
                    'assigned_to': row['Assigned_To'],
                    'days_overdue': days_overdue
                })
            except:
                pass

        # Lost tools
        if row['Status'] == 'Lost':
            alerts['lost'].append({
                'tracking_id': row['Tracking_ID'],
                'tool_name': row['Tool_Name'],
                'assigned_to': row['Assigned_To']
            })

        # Damaged tools
        if row['Condition'] in ['Damaged', 'Needs Calibration']:
            alerts['damaged'].append({
                'tracking_id': row['Tracking_ID'],
                'tool_name': row['Tool_Name'],
                'condition': row['Condition']
            })

    return alerts

def get_total_alert_count(inventory_alerts: dict, tool_alerts: dict) -> int:
    """Get total number of alerts"""
    total = 0
    total += len(inventory_alerts.get('low_stock_critical', []))
    total += len(inventory_alerts.get('low_stock_warning', []))
    total += len(inventory_alerts.get('overdue_audit', []))
    total += len(tool_alerts.get('overdue', []))
    total += len(tool_alerts.get('lost', []))
    total += len(tool_alerts.get('damaged', []))
    return total
