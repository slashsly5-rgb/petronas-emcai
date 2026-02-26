"""Reports Tab"""
import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import io

def render(components_df, logs_df, tools_df):
    """Render Reports tab"""
    st.header("📈 Reports")

    st.info("Generate and download reports in various formats")

    # Report type selection
    report_type = st.selectbox(
        "Select Report Type",
        [
            "Daily Inventory Summary",
            "Weekly Maintenance Report",
            "Monthly Tool Utilization",
            "Failure Analysis Report"
        ]
    )

    st.markdown("---")

    # Daily Inventory Summary
    if report_type == "Daily Inventory Summary":
        st.subheader("📦 Daily Inventory Summary")

        total_value = (components_df['Stock_Qty'] * components_df['Unit_Price']).sum()
        low_stock = components_df[components_df['Stock_Qty'] < 10]
        overdue_audits = components_df.copy()
        overdue_audits['Last_Audit'] = pd.to_datetime(overdue_audits['Last_Audit'])
        cutoff_date = datetime.now() - timedelta(days=90)
        overdue_audits = overdue_audits[overdue_audits['Last_Audit'] < cutoff_date]

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Inventory Value", f"RM {total_value:,.0f}")
        with col2:
            st.metric("Low Stock Items", len(low_stock))
        with col3:
            st.metric("Overdue Audits", len(overdue_audits))

        st.markdown("### Low Stock Items")
        st.dataframe(low_stock[['Component_ID', 'Item_Name', 'Stock_Qty', 'Location']], use_container_width=True)

        st.markdown("### Overdue Audits")
        st.dataframe(overdue_audits[['Component_ID', 'Item_Name', 'Last_Audit', 'Location']], use_container_width=True)

        # Download button
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            csv = components_df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"inventory_summary_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )

        with col_d2:
            # Excel download
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                components_df.to_excel(writer, sheet_name='Inventory', index=False)
                low_stock.to_excel(writer, sheet_name='Low Stock', index=False)
                overdue_audits.to_excel(writer, sheet_name='Overdue Audits', index=False)
            buffer.seek(0)

            st.download_button(
                label="📥 Download as Excel",
                data=buffer,
                file_name=f"inventory_summary_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Weekly Maintenance Report
    elif report_type == "Weekly Maintenance Report":
        st.subheader("🔧 Weekly Maintenance Report")

        logs_df_copy = logs_df.copy()
        logs_df_copy['Date'] = pd.to_datetime(logs_df_copy['Date'])
        seven_days_ago = datetime.now() - timedelta(days=7)
        weekly_logs = logs_df_copy[logs_df_copy['Date'] >= seven_days_ago]

        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Tasks", len(weekly_logs))
        with col2:
            emergency = len(weekly_logs[weekly_logs['Task_Type'] == 'Emergency'])
            st.metric("Emergency Tasks", emergency)
        with col3:
            failures = len(weekly_logs[weekly_logs['Outcome'] == 'Fail'])
            st.metric("Failed Tasks", failures)
        with col4:
            failure_rate = (failures / len(weekly_logs) * 100) if len(weekly_logs) > 0 else 0
            st.metric("Failure Rate", f"{failure_rate:.1f}%")

        st.markdown("### Tasks by Type")
        task_summary = weekly_logs['Task_Type'].value_counts().reset_index()
        task_summary.columns = ['Task Type', 'Count']
        st.dataframe(task_summary, use_container_width=True)

        st.markdown("### Technician Performance")
        tech_summary = weekly_logs.groupby('Technician').agg({
            'Log_ID': 'count',
            'Outcome': lambda x: (x == 'Pass').sum()
        }).reset_index()
        tech_summary.columns = ['Technician', 'Total Tasks', 'Successful Tasks']
        tech_summary['Success Rate %'] = (tech_summary['Successful Tasks'] / tech_summary['Total Tasks'] * 100).round(1)
        st.dataframe(tech_summary, use_container_width=True)

        # Download
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            csv = weekly_logs.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"weekly_maintenance_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )

        with col_d2:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                weekly_logs.to_excel(writer, sheet_name='Weekly Logs', index=False)
                task_summary.to_excel(writer, sheet_name='Task Summary', index=False)
                tech_summary.to_excel(writer, sheet_name='Technician Performance', index=False)
            buffer.seek(0)

            st.download_button(
                label="📥 Download as Excel",
                data=buffer,
                file_name=f"weekly_maintenance_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Monthly Tool Utilization
    elif report_type == "Monthly Tool Utilization":
        st.subheader("🛠️ Monthly Tool Utilization")

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Tools", len(tools_df))
        with col2:
            lost = len(tools_df[tools_df['Status'] == 'Lost'])
            st.metric("Lost Tools", lost)
        with col3:
            damaged = len(tools_df[tools_df['Condition'].isin(['Damaged', 'Needs Calibration'])])
            st.metric("Damaged Tools", damaged)

        st.markdown("### Tool Usage Frequency")
        tool_usage = tools_df['Tool_Name'].value_counts().reset_index()
        tool_usage.columns = ['Tool Name', 'Checkouts']
        st.dataframe(tool_usage, use_container_width=True)

        st.markdown("### Tools by Technician")
        tech_tools = tools_df['Assigned_To'].value_counts().reset_index()
        tech_tools.columns = ['Technician', 'Tools Checked Out']
        st.dataframe(tech_tools, use_container_width=True)

        st.markdown("### Lost/Damaged Summary")
        problem_tools = tools_df[
            (tools_df['Status'] == 'Lost') |
            (tools_df['Condition'].isin(['Damaged', 'Needs Calibration']))
        ]
        st.dataframe(problem_tools, use_container_width=True)

        # Download
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            csv = tools_df.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"tool_utilization_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )

        with col_d2:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                tools_df.to_excel(writer, sheet_name='All Tools', index=False)
                tool_usage.to_excel(writer, sheet_name='Usage Frequency', index=False)
                problem_tools.to_excel(writer, sheet_name='Lost-Damaged', index=False)
            buffer.seek(0)

            st.download_button(
                label="📥 Download as Excel",
                data=buffer,
                file_name=f"tool_utilization_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )

    # Failure Analysis Report
    elif report_type == "Failure Analysis Report":
        st.subheader("🔍 Failure Analysis Report")

        failed_logs = logs_df[logs_df['Outcome'] == 'Fail']

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Failures", len(failed_logs))
        with col2:
            total_tasks = len(logs_df)
            failure_rate = (len(failed_logs) / total_tasks * 100) if total_tasks > 0 else 0
            st.metric("Overall Failure Rate", f"{failure_rate:.1f}%")
        with col3:
            emergency_fails = len(failed_logs[failed_logs['Task_Type'] == 'Emergency'])
            st.metric("Emergency Failures", emergency_fails)

        st.markdown("### Failures by Component")
        component_fails = failed_logs['Component_ID'].value_counts().head(10).reset_index()
        component_fails.columns = ['Component ID', 'Failure Count']
        st.dataframe(component_fails, use_container_width=True)

        st.markdown("### Failures by Technician")
        tech_fails = failed_logs['Technician'].value_counts().reset_index()
        tech_fails.columns = ['Technician', 'Failures']
        st.dataframe(tech_fails, use_container_width=True)

        st.markdown("### Common Failure Modes")
        st.write("Based on remarks analysis:")
        all_remarks = ' '.join(failed_logs['Remarks'].tolist()).lower()
        keywords = {
            'Oil Leakage': all_remarks.count('oil leakage'),
            'Vibration': all_remarks.count('vibration'),
            'Communication Error': all_remarks.count('communication'),
            'Overheating': all_remarks.count('overheating'),
            'Battery Issues': all_remarks.count('battery'),
            'Silica Gel': all_remarks.count('silica gel')
        }
        failure_modes = pd.DataFrame(list(keywords.items()), columns=['Failure Mode', 'Occurrences'])
        failure_modes = failure_modes[failure_modes['Occurrences'] > 0].sort_values('Occurrences', ascending=False)
        st.dataframe(failure_modes, use_container_width=True)

        # Download
        col_d1, col_d2 = st.columns(2)
        with col_d1:
            csv = failed_logs.to_csv(index=False)
            st.download_button(
                label="📥 Download as CSV",
                data=csv,
                file_name=f"failure_analysis_{datetime.now().strftime('%Y%m%d')}.csv",
                mime="text/csv"
            )

        with col_d2:
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine='openpyxl') as writer:
                failed_logs.to_excel(writer, sheet_name='Failed Tasks', index=False)
                component_fails.to_excel(writer, sheet_name='By Component', index=False)
                failure_modes.to_excel(writer, sheet_name='Failure Modes', index=False)
            buffer.seek(0)

            st.download_button(
                label="📥 Download as Excel",
                data=buffer,
                file_name=f"failure_analysis_{datetime.now().strftime('%Y%m%d')}.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )
