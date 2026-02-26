# Petronas EMCAI Dashboard

⚡ **Electrical Maintenance Component AI System** - A comprehensive Streamlit-based SaaS platform for managing electrical maintenance operations.

## Features

- 📊 **Overview Dashboard** - Real-time KPIs and summary metrics
- 📦 **Component Inventory** - Track electrical components with alerts
- 🔧 **Maintenance Logs** - Monitor maintenance activities and failures
- 🛠️ **Tool Tracking** - Manage tool availability and usage
- 🤖 **AI Assistant** - GraphRAG-powered chatbot for insights
- 📈 **Reports** - Generate and download comprehensive reports

## Quick Start

### Local Development

1. **Clone the repository**
```bash
git clone <your-repo-url>
cd "Petronas EMCAI"
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Configure n8n webhooks** (Optional for demo)
   - Edit `config.py` and update the `ENDPOINTS` section with your actual n8n webhook URLs
   - Set the `GRAPHRAG_ENDPOINT` to your AI chatbot webhook

4. **Run the app**
```bash
streamlit run app.py
```

5. **Open your browser**
   - Navigate to `http://localhost:8501`

### Deployment to Streamlit Cloud

1. **Push code to GitHub**
```bash
git add .
git commit -m "Initial commit"
git push origin main
```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Click "New app"
   - Select your repository, branch (`main`), and main file (`app.py`)
   - Configure environment variables (optional):
     - `N8N_BASE_URL` - Your n8n instance URL
     - `GRAPHRAG_ENDPOINT` - AI chatbot webhook URL
     - `REFRESH_INTERVAL` - Auto-refresh interval in seconds (default: 30)
   - Click "Deploy"

## Configuration

### Environment Variables (Streamlit Cloud)

Set these in Streamlit Cloud settings or create a `.env` file locally:

```bash
N8N_BASE_URL=https://n8n.srv986677.hstgr.cloud
GRAPHRAG_ENDPOINT=https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595
REFRESH_INTERVAL=30
```

### n8n Webhook Endpoints

Update `config.py` with your actual n8n webhook paths:

```python
ENDPOINTS = {
    "components": {
        "list": f"{N8N_BASE_URL}/webhook/components",
        "create": f"{N8N_BASE_URL}/webhook/components",
        # ... etc
    },
    # ... etc
}
```

## Project Structure

```
Petronas EMCAI/
├── app.py                  # Main Streamlit application
├── config.py               # Configuration and settings
├── requirements.txt        # Python dependencies
├── README.md              # This file
├── .streamlit/
│   └── config.toml        # Streamlit configuration
├── pages/                 # Dashboard tabs
│   ├── overview.py        # Overview dashboard
│   ├── inventory.py       # Component inventory
│   ├── maintenance.py     # Maintenance logs
│   ├── tools.py           # Tool tracking
│   ├── ai_assistant.py    # AI chatbot
│   └── reports.py         # Report generation
├── utils/                 # Utility modules
│   ├── api_client.py      # n8n webhook integration
│   ├── charts.py          # Chart generation
│   └── alerts.py          # Alert calculations
└── .planning/             # Project documentation
    ├── PROJECT.md
    ├── REQUIREMENTS.md
    ├── ROADMAP.md
    └── STATE.md
```

## Features Detail

### Alert System

Automatic alerts for:
- 🔴 **Critical Low Stock** - Stock quantity < 10 units
- 🟡 **Warning Low Stock** - Stock quantity 10-15 units
- 🟡 **Overdue Audits** - Last audit > 90 days ago
- 🔴 **Overdue Tools** - Tools past due date
- 🔴 **Lost Tools** - Tools marked as lost
- 🟡 **Damaged Tools** - Tools needing repair or calibration

### AI Assistant

Powered by GraphRAG, the AI assistant can:
- Answer natural language queries about inventory
- Provide maintenance insights
- Generate summaries and reports
- Query across all data types (components, logs, tools)

Example queries:
- "Show me all PLC processors in YARD-ALPHA locations"
- "What maintenance issues did John Doe encounter this month?"
- "Which tools are currently overdue?"

### Reports

Generate and download reports in CSV/Excel formats:
1. **Daily Inventory Summary** - Stock levels and alerts
2. **Weekly Maintenance Report** - Tasks and technician performance
3. **Monthly Tool Utilization** - Tool usage and availability
4. **Failure Analysis Report** - Failure patterns and trends

## Data Integration

The app integrates with your existing n8n workflow and Supabase database:

- **Data Source**: Supabase (PostgreSQL)
- **Middleware**: n8n workflow engine
- **Access Method**: RESTful webhooks
- **AI Engine**: GraphRAG with OpenAI

### Sample Data

The app includes sample data for demonstration purposes. To use real data:
1. Configure your n8n webhook endpoints in `config.py`
2. Ensure n8n workflows are active
3. Restart the Streamlit app

## Troubleshooting

### App shows demo data instead of real data
- Check that `N8N_BASE_URL` and webhook endpoints are correctly configured
- Verify n8n workflows are active and accessible
- Check network connectivity to n8n instance

### AI Assistant not responding
- Verify `GRAPHRAG_ENDPOINT` is correct
- Check n8n GraphRAG workflow is active
- Ensure the endpoint is accessible from your deployment

### Charts not rendering
- Clear browser cache
- Check that data is loading correctly
- Verify Plotly is installed (`pip install plotly`)

## Support

For issues or questions:
- Check the `.planning/` documentation
- Review `REQUIREMENTS.md` for detailed specifications
- Consult `ROADMAP.md` for planned features

## License

© 2026 Petronas EMCAI Project

## Version

**v1.0** - Initial Release (2026-02-26)
