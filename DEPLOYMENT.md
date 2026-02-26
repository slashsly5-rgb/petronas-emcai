# Deployment Guide - Petronas EMCAI Dashboard

## Quick Deployment to Streamlit Cloud (5 minutes)

### Step 1: Push to GitHub

1. **Create a new GitHub repository**
   - Go to https://github.com/new
   - Repository name: `petronas-emcai-dashboard`
   - Make it Public or Private (your choice)
   - Don't initialize with README (we already have one)

2. **Push your code**
   ```bash
   git remote add origin https://github.com/YOUR_USERNAME/petronas-emcai-dashboard.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy on Streamlit Cloud

1. **Go to Streamlit Cloud**
   - Visit: https://share.streamlit.io
   - Sign in with your GitHub account

2. **Create new app**
   - Click "New app"
   - Repository: Select `YOUR_USERNAME/petronas-emcai-dashboard`
   - Branch: `main`
   - Main file path: `app.py`

3. **Configure environment variables** (Optional - for n8n integration)
   - Click "Advanced settings"
   - Add these environment variables:
     ```
     N8N_BASE_URL=https://n8n.srv986677.hstgr.cloud
     GRAPHRAG_ENDPOINT=https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595
     REFRESH_INTERVAL=30
     ```

4. **Deploy**
   - Click "Deploy!"
   - Wait 2-3 minutes for deployment
   - Your app will be live at: `https://YOUR_APP_NAME.streamlit.app`

### Step 3: Test Your Deployment

1. **Open the URL** provided by Streamlit Cloud
2. **Verify all tabs load**:
   - ✅ Overview
   - ✅ Inventory
   - ✅ Maintenance
   - ✅ Tools
   - ✅ AI Assistant
   - ✅ Reports

3. **Test AI chatbot** (if n8n endpoint is configured)
   - Go to "AI Assistant" tab
   - Click an example query
   - Verify response from GraphRAG

4. **Test downloads**
   - Go to "Reports" tab
   - Generate a report
   - Download CSV or Excel

---

## Alternative: Local Testing

### Run locally before deploying:

1. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**
   ```bash
   streamlit run app.py
   ```

3. **Open browser**
   - Navigate to http://localhost:8501
   - Test all features

---

## Connecting Your n8n Backend

### Update Webhook Endpoints

Edit `config.py` and replace placeholders with your actual n8n webhook URLs:

```python
ENDPOINTS = {
    "components": {
        "list": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/components",
        "create": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/components",
        "update": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/components/{{id}}",
        "delete": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/components/{{id}}"
    },
    "logs": {
        "list": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/logs",
        # ... etc
    },
    "tools": {
        "list": f"{N8N_BASE_URL}/webhook/YOUR_ACTUAL_PATH/tools",
        # ... etc
    }
}
```

### Expected n8n Response Format

Your n8n webhooks should return JSON in one of these formats:

**Option 1: Direct array**
```json
[
  {"Component_ID": "PLC-CPU-1001", "Item_Name": "PLC Processor", ...},
  {"Component_ID": "BAT-DC-1004", "Item_Name": "Substation Battery", ...}
]
```

**Option 2: Object with data property**
```json
{
  "data": [
    {"Component_ID": "PLC-CPU-1001", ...},
    {"Component_ID": "BAT-DC-1004", ...}
  ]
}
```

### AI Chatbot Integration

Your GraphRAG endpoint should:
- Accept POST requests
- Expect JSON: `{"query": "user question"}`
- Return JSON: `{"response": "AI answer"}` or `{"answer": "AI answer"}`

---

## Demo Mode (No n8n Required)

The app includes **sample data** that matches your screenshots:
- 14 sample components (PLC processors, batteries, transformers, etc.)
- 12 sample maintenance logs
- 11 sample tool tracking records

This allows you to:
- ✅ Deploy and present immediately
- ✅ Show all features working
- ✅ Add real n8n integration later

The app automatically falls back to sample data if n8n is unavailable.

---

## Presentation Tips for Tomorrow

### Before Presenting:

1. **Deploy to Streamlit Cloud** (5 min)
2. **Open the URL** and test all tabs
3. **Prepare talking points** for each feature:
   - Overview: "Real-time KPIs and alerts"
   - Inventory: "Track 14+ components with low stock alerts"
   - Maintenance: "Monitor failures and technician performance"
   - Tools: "Manage tool availability and overdue items"
   - AI Assistant: "Ask natural language questions"
   - Reports: "Generate and download comprehensive reports"

### During Presentation:

1. **Start with Overview tab**
   - Show total inventory value (RM 168,725)
   - Point out alert system (red/yellow badges)

2. **Demo Inventory tab**
   - Show filters (location, manufacturer, condition)
   - Highlight low stock alerts
   - Show interactive charts

3. **Show Maintenance tab**
   - Filter by technician (e.g., "John Doe")
   - Show failure analysis
   - Point out failure rate metrics

4. **Demo AI Assistant**
   - Click an example query
   - Show natural language interaction
   - (If n8n connected, show real responses)

5. **Generate a Report**
   - Select "Weekly Maintenance Report"
   - Download Excel file
   - Show multiple sheets

### Key Selling Points:

- ✅ **Modern UI** - Clean, professional Streamlit interface
- ✅ **Real-time Data** - Auto-refresh every 30 seconds
- ✅ **Smart Alerts** - Proactive low stock and overdue notifications
- ✅ **AI-Powered** - GraphRAG chatbot for insights
- ✅ **Comprehensive Reports** - CSV, Excel downloads
- ✅ **Easy Deployment** - Cloud-hosted, no installation needed

---

## Troubleshooting

### Issue: App shows error on deployment
**Solution**: Check Streamlit Cloud logs, ensure `requirements.txt` is correct

### Issue: Charts not rendering
**Solution**: Clear browser cache, reload page

### Issue: AI Assistant returns error
**Solution**: Verify `GRAPHRAG_ENDPOINT` environment variable is set correctly

### Issue: Data not loading from n8n
**Solution**:
1. Check n8n workflows are active
2. Verify webhook URLs in `config.py`
3. Test webhooks directly with Postman/curl

---

## Next Steps After Presentation

1. **Connect real n8n data** (replace sample data)
2. **Customize alert thresholds** in `config.py`
3. **Add authentication** (if needed for production)
4. **Customize branding** (Petronas colors, logo)
5. **Add more reports** as per customer feedback
6. **Scale up** if data volume increases

---

## Support Contacts

- Streamlit Documentation: https://docs.streamlit.io
- n8n Documentation: https://docs.n8n.io
- This project documentation: See `.planning/` folder

---

**Good luck with your presentation tomorrow! 🚀**
