# Configuration for Petronas EMCAI Dashboard
import os

# n8n Webhook Base URL
N8N_BASE_URL = os.getenv("N8N_BASE_URL", "https://n8n.srv986677.hstgr.cloud")

# GraphRAG AI Endpoint
GRAPHRAG_ENDPOINT = os.getenv(
    "GRAPHRAG_ENDPOINT",
    "https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595"
)

# Auto-refresh interval (seconds)
REFRESH_INTERVAL = int(os.getenv("REFRESH_INTERVAL", "30"))

# Alert Thresholds
LOW_STOCK_CRITICAL = 10  # Red alert
LOW_STOCK_WARNING = 15   # Yellow alert
OVERDUE_AUDIT_DAYS = 90  # Days before audit is overdue
OVERDUE_TOOL_CRITICAL = 30  # Days overdue for critical alert

# App Settings
APP_TITLE = "Petronas EMCAI Dashboard"
APP_ICON = "⚡"
ITEMS_PER_PAGE = 50

# n8n Webhook Endpoints (customize these based on your actual n8n setup)
# These are placeholder endpoints - update with your actual webhook paths
ENDPOINTS = {
    "components": {
        "list": f"{N8N_BASE_URL}/webhook/components",
        "create": f"{N8N_BASE_URL}/webhook/components",
        "update": f"{N8N_BASE_URL}/webhook/components/{{id}}",
        "delete": f"{N8N_BASE_URL}/webhook/components/{{id}}"
    },
    "logs": {
        "list": f"{N8N_BASE_URL}/webhook/logs",
        "create": f"{N8N_BASE_URL}/webhook/logs",
        "update": f"{N8N_BASE_URL}/webhook/logs/{{id}}",
        "delete": f"{N8N_BASE_URL}/webhook/logs/{{id}}"
    },
    "tools": {
        "list": f"{N8N_BASE_URL}/webhook/tools",
        "create": f"{N8N_BASE_URL}/webhook/tools",
        "update": f"{N8N_BASE_URL}/webhook/tools/{{id}}",
        "delete": f"{N8N_BASE_URL}/webhook/tools/{{id}}"
    }
}
