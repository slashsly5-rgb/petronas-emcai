"""Inventory Dashboard Tab"""
import streamlit as st
import pandas as pd
from utils import charts
import config

def render(components_df, inventory_alerts):
    """Render Inventory tab"""
    st.header("📦 Component Inventory")

    # Filters
    st.subheader("🔍 Filters")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        locations = ['All'] + sorted(components_df['Location'].unique().tolist())
        selected_location = st.multiselect("Location", locations, default=['All'])

    with col2:
        manufacturers = ['All'] + sorted(components_df['Manufacturer'].unique().tolist())
        selected_manufacturer = st.multiselect("Manufacturer", manufacturers, default=['All'])

    with col3:
        conditions = ['All'] + sorted(components_df['Condition'].unique().tolist())
        selected_condition = st.multiselect("Condition", conditions, default=['All'])

    with col4:
        search_term = st.text_input("Search Component ID/Name", "")

    # Apply filters
    filtered_df = components_df.copy()

    if 'All' not in selected_location and len(selected_location) > 0:
        filtered_df = filtered_df[filtered_df['Location'].isin(selected_location)]

    if 'All' not in selected_manufacturer and len(selected_manufacturer) > 0:
        filtered_df = filtered_df[filtered_df['Manufacturer'].isin(selected_manufacturer)]

    if 'All' not in selected_condition and len(selected_condition) > 0:
        filtered_df = filtered_df[filtered_df['Condition'].isin(selected_condition)]

    if search_term:
        filtered_df = filtered_df[
            filtered_df['Component_ID'].str.contains(search_term, case=False, na=False) |
            filtered_df['Item_Name'].str.contains(search_term, case=False, na=False)
        ]

    # Alert summary
    st.markdown("---")
    col_alert1, col_alert2, col_alert3 = st.columns(3)

    with col_alert1:
        st.metric("🔴 Critical Low Stock", len(inventory_alerts['low_stock_critical']))

    with col_alert2:
        st.metric("🟡 Warning Low Stock", len(inventory_alerts['low_stock_warning']))

    with col_alert3:
        st.metric("🟡 Overdue Audits", len(inventory_alerts['overdue_audit']))

    # Inventory table
    st.markdown("---")
    st.subheader(f"Inventory List ({len(filtered_df)} items)")

    # Highlight low stock and overdue audits
    def highlight_alerts(row):
        if row['Stock_Qty'] < config.LOW_STOCK_CRITICAL:
            return ['background-color: #ffcdd2'] * len(row)
        elif row['Stock_Qty'] <= config.LOW_STOCK_WARNING:
            return ['background-color: #fff9c4'] * len(row)
        return [''] * len(row)

    styled_df = filtered_df.style.apply(highlight_alerts, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

    # Visualizations
    st.markdown("---")
    st.subheader("📊 Inventory Analytics")

    col_viz1, col_viz2 = st.columns(2)

    with col_viz1:
        fig = charts.create_stock_by_location_chart(filtered_df)
        st.plotly_chart(fig, use_container_width=True, key="inventory_stock_location_chart")

    with col_viz2:
        fig = charts.create_condition_pie_chart(filtered_df)
        st.plotly_chart(fig, use_container_width=True, key="inventory_condition_pie_chart")

    # Manufacturer distribution
    fig = charts.create_manufacturer_chart(filtered_df)
    st.plotly_chart(fig, use_container_width=True, key="inventory_manufacturer_chart")

    # Alert Details
    if len(inventory_alerts['low_stock_critical']) > 0 or len(inventory_alerts['overdue_audit']) > 0:
        st.markdown("---")
        st.subheader("⚠️ Alert Details")

        if len(inventory_alerts['low_stock_critical']) > 0:
            with st.expander("🔴 Critical Low Stock Items"):
                for alert in inventory_alerts['low_stock_critical']:
                    st.warning(f"**{alert['component_id']}** - {alert['item_name']} | Stock: {alert['stock']} | Location: {alert['location']}")

        if len(inventory_alerts['overdue_audit']) > 0:
            with st.expander("🟡 Overdue Audits"):
                for alert in inventory_alerts['overdue_audit']:
                    st.warning(f"**{alert['component_id']}** - {alert['item_name']} | {alert['days_overdue']} days overdue | Last Audit: {alert['last_audit']}")
