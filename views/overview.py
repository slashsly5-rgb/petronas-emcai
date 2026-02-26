"""Overview Dashboard Tab"""
import streamlit as st
import pandas as pd
from utils import charts
from datetime import datetime, timedelta

def render(components_df, logs_df, tools_df, inventory_alerts, tool_alerts):
    """Render Overview tab"""
    st.header("📊 Dashboard Overview")

    # KPI Metrics
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        total_value = (components_df['Stock_Qty'] * components_df['Unit_Price']).sum()
        st.metric("Total Inventory Value", f"RM {total_value:,.0f}")

    with col2:
        low_stock_count = len(inventory_alerts['low_stock_critical']) + len(inventory_alerts['low_stock_warning'])
        st.metric("Low Stock Alerts", low_stock_count, delta=-low_stock_count if low_stock_count > 0 else 0)

    with col3:
        # Maintenance tasks last 30 days
        logs_df_copy = logs_df.copy()
        logs_df_copy['Date'] = pd.to_datetime(logs_df_copy['Date'])
        thirty_days_ago = datetime.now() - timedelta(days=30)
        recent_tasks = len(logs_df_copy[logs_df_copy['Date'] >= thirty_days_ago])
        st.metric("Tasks (30 days)", recent_tasks)

    with col4:
        # Failure rate
        fail_count = len(logs_df[logs_df['Outcome'] == 'Fail'])
        failure_rate = (fail_count / len(logs_df) * 100) if len(logs_df) > 0 else 0
        st.metric("Failure Rate", f"{failure_rate:.1f}%", delta=f"-{failure_rate:.1f}%" if failure_rate < 20 else f"+{failure_rate:.1f}%")

    st.markdown("---")

    # Second row of KPIs
    col5, col6, col7, col8 = st.columns(4)

    with col5:
        st.metric("Total Components", len(components_df))

    with col6:
        overdue_audits = len(inventory_alerts['overdue_audit'])
        st.metric("Overdue Audits", overdue_audits, delta=-overdue_audits if overdue_audits > 0 else 0)

    with col7:
        available_tools = len(tools_df[tools_df['Status'] == 'Returned'])
        st.metric("Tools Available", available_tools)

    with col8:
        overdue_tools = len(tool_alerts['overdue']) + len(tool_alerts['lost'])
        st.metric("Tools Overdue/Lost", overdue_tools, delta=-overdue_tools if overdue_tools > 0 else 0)

    st.markdown("---")

    # Visualizations
    col_left, col_right = st.columns(2)

    with col_left:
        st.subheader("Inventory Health")
        # Categorize inventory health
        good_stock = len(components_df[components_df['Stock_Qty'] > 15])
        low_stock = len(components_df[(components_df['Stock_Qty'] >= 10) & (components_df['Stock_Qty'] <= 15)])
        critical_stock = len(components_df[components_df['Stock_Qty'] < 10])

        if len(components_df) > 0:
            fig = charts.create_condition_pie_chart(components_df)
            st.plotly_chart(fig, use_container_width=True, key="overview_condition_pie_chart")
        else:
            st.info("No component data to display inventory health.")

    with col_right:
        st.subheader("Maintenance Trends (Last 90 days)")
        if len(logs_df) > 0:
            # Filter logs to last 90 days for better trend visualization
            recent_logs = logs_df.copy()
            recent_logs['Date'] = pd.to_datetime(recent_logs['Date'])
            cutoff_date = datetime.now() - timedelta(days=90)
            recent_logs = recent_logs[recent_logs['Date'] >= cutoff_date]
            
            fig = charts.create_maintenance_trend_chart(recent_logs)
            st.plotly_chart(fig, use_container_width=True, key="overview_maintenance_trend_chart")
        else:
            st.info("No maintenance data in the last 90 days")

    # Tool Status
    col_tool1, col_tool2 = st.columns(2)

    with col_tool1:
        st.subheader("Tool Status Distribution")
        if len(tools_df) > 0:
            fig = charts.create_tool_status_chart(tools_df)
            st.plotly_chart(fig, use_container_width=True, key="overview_tool_status_chart")
        else:
            st.info("No tool data to display status distribution.")
            
    with col_tool2:
        st.subheader("Top Locations by Component Count")
        if len(components_df) > 0:
            fig = charts.create_stock_by_location_chart(components_df)
            st.plotly_chart(fig, use_container_width=True, key="overview_stock_location_chart")
        else:
            st.info("No component data to display stock by location.")

    # Recent Activity
    st.markdown("---")
    st.subheader("📋 Recent Maintenance Activity (Last 10)")
    recent_logs = logs_df.copy()
    recent_logs['Date'] = pd.to_datetime(recent_logs['Date'])
    recent_logs = recent_logs.sort_values('Date', ascending=False).head(10)

    # Color code outcomes
    def color_outcome(val):
        if val == 'Pass':
            return 'background-color: #d4edda'
        elif val == 'Fail':
            return 'background-color: #f8d7da'
        elif val == 'Warning':
            return 'background-color: #fff3cd'
        return ''

    styled_df = recent_logs.style.applymap(color_outcome, subset=['Outcome'])
    st.dataframe(styled_df, use_container_width=True, hide_index=True)
