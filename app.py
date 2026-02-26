"""Petronas EMCAI Dashboard - Main Application"""
import streamlit as st
import sys
from pathlib import Path

# Add utils to path
sys.path.append(str(Path(__file__).parent))

import config
from utils.api_client import client
from utils.alerts import calculate_inventory_alerts, calculate_tool_alerts, get_total_alert_count

# Page configuration
st.set_page_config(
    page_title=config.APP_TITLE,
    page_icon=config.APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #FF6B35;
        text-align: center;
        padding: 1rem 0;
    }
    .alert-banner {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .alert-critical {
        background-color: #ffebee;
        border-left: 5px solid #f44336;
    }
    .alert-warning {
        background-color: #fff3e0;
        border-left: 5px solid #ff9800;
    }
    .metric-card {
        background-color: #f5f5f5;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown(f'<div class="main-header">{config.APP_ICON} {config.APP_TITLE}</div>', unsafe_allow_html=True)

# Load data
@st.cache_data(ttl=config.REFRESH_INTERVAL)
def load_data():
    components = client.get_components()
    logs = client.get_logs()
    tools = client.get_tools()
    return components, logs, tools

try:
    components_df, logs_df, tools_df = load_data()

    # Calculate alerts
    inventory_alerts = calculate_inventory_alerts(components_df)
    tool_alerts = calculate_tool_alerts(tools_df)
    total_alerts = get_total_alert_count(inventory_alerts, tool_alerts)

    # Alert banner
    if total_alerts > 0:
        critical_count = len(inventory_alerts['low_stock_critical']) + len(tool_alerts['overdue']) + len(tool_alerts['lost'])
        warning_count = len(inventory_alerts['low_stock_warning']) + len(inventory_alerts['overdue_audit']) + len(tool_alerts['damaged'])

        if critical_count > 0:
            st.markdown(f"""
            <div class="alert-banner alert-critical">
                <strong>🔴 {critical_count} Critical Alert(s)</strong> -
                {len(inventory_alerts['low_stock_critical'])} low stock,
                {len(tool_alerts['overdue'])} overdue tools,
                {len(tool_alerts['lost'])} lost tools
            </div>
            """, unsafe_allow_html=True)

        if warning_count > 0:
            st.markdown(f"""
            <div class="alert-banner alert-warning">
                <strong>🟡 {warning_count} Warning(s)</strong> -
                {len(inventory_alerts['low_stock_warning'])} low stock warnings,
                {len(inventory_alerts['overdue_audit'])} overdue audits,
                {len(tool_alerts['damaged'])} damaged tools
            </div>
            """, unsafe_allow_html=True)

    # Sidebar
    with st.sidebar:
        st.header("Navigation")
        st.info(f"📊 Total Alerts: **{total_alerts}**")

        if st.button("🔄 Refresh Data"):
            st.cache_data.clear()
            st.rerun()

        st.markdown("---")
        st.markdown("### Quick Stats")
        st.metric("Total Components", len(components_df))
        st.metric("Maintenance Logs", len(logs_df))
        st.metric("Tools Tracked", len(tools_df))

    # Main tabs
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "📊 Overview",
        "📦 Inventory",
        "🔧 Maintenance",
        "🛠️ Tools",
        "🤖 AI Assistant",
        "📈 Reports"
    ])

    # Import and render tab contents
    with tab1:
        from views import overview
        overview.render(components_df, logs_df, tools_df, inventory_alerts, tool_alerts)

    with tab2:
        from views import inventory
        inventory.render(components_df, inventory_alerts)

    with tab3:
        from views import maintenance
        maintenance.render(logs_df)

    with tab4:
        from views import tools
        tools.render(tools_df, tool_alerts)

    with tab5:
        from views import ai_assistant
        ai_assistant.render()

    with tab6:
        from views import reports
        reports.render(components_df, logs_df, tools_df)

except Exception as e:
    st.error(f"Error loading dashboard: {str(e)}")
    st.info("The app is running in demo mode with sample data. Configure n8n webhooks to load real data.")

# Footer
st.markdown("---")
st.markdown(f"<div style='text-align: center; color: gray; font-size: 0.8rem;'>Petronas EMCAI Dashboard v1.0 | Last updated: {st.session_state.get('last_update', 'N/A')}</div>", unsafe_allow_html=True)
