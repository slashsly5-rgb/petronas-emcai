"""Maintenance Dashboard Tab"""
import streamlit as st
import pandas as pd
from utils import charts
from datetime import datetime, timedelta

def render(logs_df):
    """Render Maintenance tab"""
    st.header("🔧 Maintenance Logs")

    # Filters
    st.subheader("🔍 Filters")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        task_types = ['All'] + sorted(logs_df['Task_Type'].unique().tolist())
        selected_task = st.multiselect("Task Type", task_types, default=['All'])

    with col2:
        technicians = ['All'] + sorted(logs_df['Technician'].unique().tolist())
        selected_tech = st.multiselect("Technician", technicians, default=['All'])

    with col3:
        outcomes = ['All'] + sorted(logs_df['Outcome'].unique().tolist())
        selected_outcome = st.multiselect("Outcome", outcomes, default=['All'])

    with col4:
        search_term = st.text_input("Search Component ID/Remarks", "")

    # Quick date filters
    col_date1, col_date2, col_date3, col_date4 = st.columns(4)

    with col_date1:
        if st.button("Last 7 Days"):
            st.session_state['date_filter'] = 7

    with col_date2:
        if st.button("Last 30 Days"):
            st.session_state['date_filter'] = 30

    with col_date3:
        if st.button("This Year"):
            st.session_state['date_filter'] = 365

    with col_date4:
        if st.button("Clear Date Filter"):
            st.session_state['date_filter'] = None

    # Apply filters
    filtered_df = logs_df.copy()
    filtered_df['Date'] = pd.to_datetime(filtered_df['Date'])

    if 'All' not in selected_task and len(selected_task) > 0:
        filtered_df = filtered_df[filtered_df['Task_Type'].isin(selected_task)]

    if 'All' not in selected_tech and len(selected_tech) > 0:
        filtered_df = filtered_df[filtered_df['Technician'].isin(selected_tech)]

    if 'All' not in selected_outcome and len(selected_outcome) > 0:
        filtered_df = filtered_df[filtered_df['Outcome'].isin(selected_outcome)]

    if search_term:
        filtered_df = filtered_df[
            filtered_df['Component_ID'].str.contains(search_term, case=False, na=False) |
            filtered_df['Remarks'].str.contains(search_term, case=False, na=False)
        ]

    # Date filter
    if 'date_filter' in st.session_state and st.session_state['date_filter']:
        cutoff_date = datetime.now() - timedelta(days=st.session_state['date_filter'])
        filtered_df = filtered_df[filtered_df['Date'] >= cutoff_date]

    # Summary metrics
    st.markdown("---")
    col_m1, col_m2, col_m3, col_m4 = st.columns(4)

    with col_m1:
        st.metric("Total Tasks", len(filtered_df))

    with col_m2:
        fail_count = len(filtered_df[filtered_df['Outcome'] == 'Fail'])
        failure_rate = (fail_count / len(filtered_df) * 100) if len(filtered_df) > 0 else 0
        st.metric("Failure Rate", f"{failure_rate:.1f}%")

    with col_m3:
        emergency_count = len(filtered_df[filtered_df['Task_Type'] == 'Emergency'])
        st.metric("Emergency Tasks", emergency_count)

    with col_m4:
        pass_count = len(filtered_df[filtered_df['Outcome'] == 'Pass'])
        st.metric("Successful Tasks", pass_count)

    # Maintenance table
    st.markdown("---")
    st.subheader(f"Maintenance Log ({len(filtered_df)} records)")

    # Color code outcomes
    def color_outcome(val):
        if val == 'Pass':
            return 'background-color: #d4edda'
        elif val == 'Fail':
            return 'background-color: #f8d7da'
        elif val == 'Warning':
            return 'background-color: #fff3cd'
        return ''

    styled_df = filtered_df.sort_values('Date', ascending=False).style.applymap(color_outcome, subset=['Outcome'])
    st.dataframe(styled_df, use_container_width=True, hide_index=True, height=400)

    # Visualizations
    st.markdown("---")
    st.subheader("📊 Maintenance Analytics")

    col_v1, col_v2 = st.columns(2)

    with col_v1:
        if len(filtered_df) > 0:
            fig = charts.create_task_type_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True, key="maintenance_task_type_chart")

    with col_v2:
        if len(filtered_df) > 0:
            fig = charts.create_outcome_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True, key="maintenance_outcome_chart")

    col_v3, col_v4 = st.columns(2)

    with col_v3:
        if len(filtered_df) > 0:
            fig = charts.create_technician_workload_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True, key="maintenance_tech_workload_chart")

    with col_v4:
        if len(filtered_df) > 0:
            fig = charts.create_maintenance_trend_chart(filtered_df)
            st.plotly_chart(fig, use_container_width=True, key="maintenance_trend_chart")

    # Failure Analysis
    st.markdown("---")
    st.subheader("🔍 Failure Analysis")

    failed_tasks = filtered_df[filtered_df['Outcome'] == 'Fail']

    if len(failed_tasks) > 0:
        col_f1, col_f2 = st.columns(2)

        with col_f1:
            st.write("**Failed Tasks by Component**")
            component_failures = failed_tasks['Component_ID'].value_counts().head(10)
            st.bar_chart(component_failures)

        with col_f2:
            st.write("**Common Failure Modes**")
            # Extract keywords from remarks
            all_remarks = ' '.join(failed_tasks['Remarks'].tolist()).lower()
            keywords = ['oil leakage', 'vibration', 'communication', 'overheating', 'battery', 'silica gel']
            keyword_counts = {kw: all_remarks.count(kw) for kw in keywords}
            st.bar_chart(keyword_counts)
    else:
        st.info("No failed tasks in the current filter")
