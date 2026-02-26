"""Tool Tracking Dashboard Tab"""
import streamlit as st
import pandas as pd
from utils import charts
from datetime import datetime

def render(tools_df, tool_alerts):
    """Render Tools tab"""
    st.header("🛠️ Tool Tracking")

    # Filters
    st.subheader("🔍 Filters")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        tool_names = ['All'] + sorted(tools_df['Tool_Name'].unique().tolist())
        selected_tool = st.multiselect("Tool Name", tool_names, default=['All'])

    with col2:
        technicians = ['All'] + sorted(tools_df['Assigned_To'].unique().tolist())
        selected_tech = st.multiselect("Assigned To", technicians, default=['All'])

    with col3:
        statuses = ['All'] + sorted(tools_df['Status'].unique().tolist())
        selected_status = st.multiselect("Status", statuses, default=['All'])

    with col4:
        conditions = ['All'] + sorted(tools_df['Condition'].unique().tolist())
        selected_condition = st.multiselect("Condition", conditions, default=['All'])

    # Quick filters
    col_q1, col_q2, col_q3, col_q4 = st.columns(4)

    with col_q1:
        if st.button("Available"):
            st.session_state['tool_quick_filter'] = 'Returned'

    with col_q2:
        if st.button("Overdue"):
            st.session_state['tool_quick_filter'] = 'Overdue'

    with col_q3:
        if st.button("Lost"):
            st.session_state['tool_quick_filter'] = 'Lost'

    with col_q4:
        if st.button("Clear Filter"):
            st.session_state['tool_quick_filter'] = None

    # Apply filters
    filtered_df = tools_df.copy()

    if 'All' not in selected_tool and len(selected_tool) > 0:
        filtered_df = filtered_df[filtered_df['Tool_Name'].isin(selected_tool)]

    if 'All' not in selected_tech and len(selected_tech) > 0:
        filtered_df = filtered_df[filtered_df['Assigned_To'].isin(selected_tech)]

    if 'All' not in selected_status and len(selected_status) > 0:
        filtered_df = filtered_df[filtered_df['Status'].isin(selected_status)]

    if 'All' not in selected_condition and len(selected_condition) > 0:
        filtered_df = filtered_df[filtered_df['Condition'].isin(selected_condition)]

    # Quick filter
    if 'tool_quick_filter' in st.session_state and st.session_state['tool_quick_filter']:
        filtered_df = filtered_df[filtered_df['Status'] == st.session_state['tool_quick_filter']]

    # Alert summary
    st.markdown("---")
    col_a1, col_a2, col_a3, col_a4 = st.columns(4)

    with col_a1:
        st.metric("🔴 Overdue Tools", len(tool_alerts['overdue']))

    with col_a2:
        st.metric("🔴 Lost Tools", len(tool_alerts['lost']))

    with col_a3:
        st.metric("🟡 Damaged Tools", len(tool_alerts['damaged']))

    with col_a4:
        available = len(tools_df[tools_df['Status'] == 'Returned'])
        st.metric("✅ Available Tools", available)

    # Tool tracking table
    st.markdown("---")
    st.subheader(f"Tool Tracking ({len(filtered_df)} records)")

    # Highlight alerts
    def highlight_tool_alerts(row):
        if row['Status'] == 'Overdue' or row['Status'] == 'Lost':
            return ['background-color: #ffcdd2'] * len(row)
        elif row['Condition'] in ['Damaged', 'Needs Calibration']:
            return ['background-color: #fff9c4'] * len(row)
        return [''] * len(row)

    styled_df = filtered_df.style.apply(highlight_tool_alerts, axis=1)
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

    # Visualizations
    st.markdown("---")
    st.subheader("📊 Tool Analytics")

    col_v1, col_v2 = st.columns(2)

    with col_v1:
        if len(filtered_df) > 0:
            fig = charts.create_tool_status_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True)

    with col_v2:
        if len(filtered_df) > 0:
            fig = charts.create_tool_usage_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True)

    # Availability gauge
    total_tools = len(tools_df)
    available_tools = len(tools_df[tools_df['Status'] == 'Returned'])

    fig = charts.create_gauge_chart(available_tools, total_tools, "Tool Availability %")
    st.plotly_chart(fig, use_container_width=True)

    # Alert Details
    if len(tool_alerts['overdue']) > 0 or len(tool_alerts['lost']) > 0 or len(tool_alerts['damaged']) > 0:
        st.markdown("---")
        st.subheader("⚠️ Alert Details")

        if len(tool_alerts['overdue']) > 0:
            with st.expander("🔴 Overdue Tools"):
                for alert in tool_alerts['overdue']:
                    st.error(f"**{alert['tracking_id']}** - {alert['tool_name']} | Assigned to: {alert['assigned_to']} | {alert['days_overdue']} days overdue")

        if len(tool_alerts['lost']) > 0:
            with st.expander("🔴 Lost Tools"):
                for alert in tool_alerts['lost']:
                    st.error(f"**{alert['tracking_id']}** - {alert['tool_name']} | Last assigned to: {alert['assigned_to']}")

        if len(tool_alerts['damaged']) > 0:
            with st.expander("🟡 Damaged Tools"):
                for alert in tool_alerts['damaged']:
                    st.warning(f"**{alert['tracking_id']}** - {alert['tool_name']} | Condition: {alert['condition']}")
