# Petronas EMCAI - Electrical Maintenance Component AI System

## Vision

A comprehensive SaaS platform for Petronas electrical maintenance teams to manage component inventory, maintenance logs, and tool tracking with AI-powered insights and real-time monitoring capabilities.

## Problem Statement

Petronas electrical maintenance teams need a unified platform to:
- Track electrical components across multiple locations (substations, yards, warehouses)
- Monitor maintenance activities and analyze failure patterns
- Manage tool inventory and availability
- Get AI-powered insights from historical data
- Receive real-time alerts for low stock and overdue audits
- Generate automated reports and summaries

## Solution Overview

A Streamlit-based dashboard that integrates with existing n8n workflow backend and Supabase database, providing:

1. **Real-time Dashboard** - Single-page tabbed interface showing:
   - Component inventory status with alerts
   - Maintenance log trends and failure analysis
   - Tool tracking and availability
   - Advanced search/filter across all datasets

2. **AI Chatbot** - GraphRAG-powered conversational interface for:
   - Natural language queries about inventory, logs, and tools
   - Automated report generation and data summaries
   - Maintenance insights and recommendations

3. **Alert System** - Proactive notifications for:
   - Low stock warnings (configurable thresholds)
   - Overdue audit alerts (based on Last_Audit dates)
   - Critical maintenance failures

4. **Report Generation** - Automated reports including:
   - Daily/weekly inventory summaries
   - Maintenance failure analysis (by component, technician, location)
   - Tool utilization reports
   - Downloadable formats (CSV, Excel, PDF)

## Target Users

- **Technicians** - Field workers (John Doe, Sarah Wong, Ahmad Zulkifli, Rajesh Kumar, etc.)
  - View component availability
  - Log maintenance activities
  - Check tool availability
  - Query AI for component specs and locations

- **Managers** - Supervisors and team leads
  - Monitor team performance
  - Review maintenance trends
  - Generate reports
  - Identify failure patterns

- **Administrators** - System managers
  - Overall inventory oversight
  - Audit compliance tracking
  - Resource allocation
  - Strategic planning insights

## Technical Architecture

### Backend (Existing)
- **n8n Workflow Engine** - Handles all CRUD operations via webhooks
- **Supabase Database** - PostgreSQL database storing:
  - Component inventory (44 items tracked)
  - Maintenance logs (Emergency, Inspection, Corrective, Preventive)
  - Tool tracking (Arc Flash Suits, Multimeters, Laptops, etc.)
- **GraphRAG AI Agent** - Agentic RAG Hub with:
  - OpenAI Chat Model integration
  - PostgreSQL Chat Memory
  - SQL query execution capabilities
  - Database schema awareness
  - Endpoint: `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`

### Frontend (To Build)
- **Streamlit** - Python web framework
- **Deployment** - GitHub → Streamlit Community Cloud
- **No Authentication** - Internal network access assumed
- **Auto-refresh** - Real-time data updates

### Data Flow
```
Streamlit App → n8n Webhooks → Supabase Database
                ↓
        AI Chatbot (GraphRAG)
```

## Data Domains

### 1. Component Inventory
**Key Fields:**
- Component_ID (PLC-CPU-1001, BAT-DC-1004, etc.)
- Item_Name (PLC Processor, Substation Battery, Power Transformer, etc.)
- Category (Electrical)
- Specification (S7-1500/ControlLogix, 110V Ni-Cd Bank, etc.)
- Manufacturer (GE Alstom, ABB, Schneider, Siemens, Crompton, Eaton)
- Stock_Qty (Current inventory levels)
- Unit_Price (RM 45 - RM 15000)
- Location (YARD-ALPHA-65, WH-ZN-C-14, SUBSTATION-02-39, etc.)
- Condition (New, Used, Refurbished)
- Last_Audit (Audit dates for compliance tracking)

**Alert Triggers:**
- Low stock: Stock_Qty < 15 units (critical items)
- Overdue audit: Last_Audit > 90 days from today

### 2. Maintenance Logs
**Key Fields:**
- Log_ID (LOG-2025-0001, etc.)
- Date (Maintenance date)
- Component_ID (Links to inventory)
- Task_Type (Emergency, Inspection, Corrective, Preventive)
- Technician (John Doe, Sarah Wong, Ahmad Zulkifli, Rajesh Kumar, Chong Wei)
- Outcome (Pass, Fail, Warning)
- Remarks (Oil leakage observed, Excessive vibration detected, etc.)

**Analysis Focus:**
- Failure patterns by component type
- Technician performance metrics
- Emergency vs preventive task ratios
- Common failure modes

### 3. Tool Tracking
**Key Fields:**
- Tracking_ID (TRK-5001, etc.)
- Tool_Name (Megger Insulation Tester, Fluke Multimeter, Arc Flash Suit, Safety Harness, Laptop)
- Assigned_To (Technician name)
- Date_Out (Checkout date)
- Date_Due (Return due date)
- Status (Overdue, Returned, Lost)
- Condition (Good, Damaged, Needs Calibration)

**Alert Triggers:**
- Overdue tools: Date_Due < Today AND Status = "Overdue"
- Lost tools: Status = "Lost"
- Damaged tools: Condition = "Damaged" or "Needs Calibration"

## Key Features

### Dashboard Capabilities
1. **Multi-Tab Layout** (single page)
   - 📊 Overview - KPIs and summary metrics
   - 📦 Inventory - Component list with filters
   - 🔧 Maintenance - Log history and analysis
   - 🛠️ Tools - Tracking and availability
   - 🤖 AI Assistant - Chatbot interface
   - 📈 Reports - Generated summaries

2. **Search & Filter** (across all datasets)
   - By Location (YARD-ALPHA-*, WH-ZN-*, SUBSTATION-*)
   - By Manufacturer (GE Alstom, ABB, Schneider, Siemens, Crompton, Eaton)
   - By Condition (New, Used, Refurbished)
   - By Date Range (for logs and tool tracking)
   - By Technician (for maintenance logs)
   - By Component Type (PLC, Battery, Transformer, Cable, etc.)
   - By Task Type (Emergency, Inspection, Corrective, Preventive)
   - By Tool Status (Available, Out, Overdue, Lost)

3. **Real-time Alerts**
   - Banner notifications at top of dashboard
   - Sidebar alert summary with counts
   - Color-coded row highlighting in tables
   - Alert categories:
     - 🔴 Critical (Low stock < 10, Overdue > 30 days)
     - 🟡 Warning (Low stock 10-15, Overdue audit > 90 days)
     - 🔵 Info (General notifications)

4. **Visualizations**
   - Inventory levels by location (bar chart)
   - Stock condition distribution (pie chart)
   - Maintenance trend over time (line chart)
   - Failure analysis by component (bar chart)
   - Tool availability status (gauge chart)
   - Technician workload (bar chart)
   - Top failure modes (horizontal bar)

5. **AI Chatbot Integration**
   - Embedded in dedicated "AI Assistant" tab
   - Text input for natural language queries
   - Streaming responses from GraphRAG endpoint
   - Example queries displayed as quick actions:
     - "Show me all PLC processors in YARD-ALPHA locations"
     - "What maintenance issues did John Doe encounter this month?"
     - "Which tools are currently overdue?"
     - "Generate a summary of battery failures in 2025"
     - "What's the total value of refurbished components?"
   - Chat history preserved during session
   - Structured output rendering (Streamlit converts text to tables/charts as needed)

6. **Report Generation**
   - **Daily Inventory Summary**
     - Total stock value
     - New additions/removals
     - Low stock alerts
     - Overdue audits

   - **Weekly Maintenance Report**
     - Tasks completed by type
     - Failure rate trends
     - Technician performance
     - Critical issues requiring attention

   - **Monthly Tool Utilization**
     - Tool usage frequency
     - Lost/damaged tool summary
     - Calibration due list
     - Cost analysis

   - **Failure Analysis Report**
     - By component type
     - By location
     - By technician
     - Common failure modes
     - Preventive recommendations

   - Download formats: CSV, Excel, PDF

### n8n Integration Points

The Streamlit app will interact with n8n webhooks for:
- **Read Operations** (GET)
  - Fetch all components / filtered components
  - Fetch all maintenance logs / filtered logs
  - Fetch all tool tracking / filtered tools

- **Create Operations** (POST)
  - Add new component
  - Log maintenance activity
  - Check out tool

- **Update Operations** (PUT)
  - Update component stock/condition
  - Update maintenance log
  - Return tool / update tool status

- **Delete Operations** (DELETE)
  - Remove component
  - Delete maintenance log
  - Remove tool from tracking

- **AI Query** (POST to GraphRAG endpoint)
  - Send natural language query
  - Receive text response

## Success Metrics

1. **User Adoption**
   - All technicians using tool tracking system
   - Managers generating weekly reports
   - Reduction in manual data entry

2. **Operational Efficiency**
   - 50% reduction in time to locate components
   - 80% improvement in audit compliance
   - 30% reduction in tool loss incidents

3. **Data Quality**
   - 95% accuracy in inventory counts
   - Real-time sync between n8n and dashboard
   - Zero data loss during operations

4. **AI Effectiveness**
   - 70% of queries answered correctly by chatbot
   - Reduction in manual report generation time
   - User satisfaction with AI insights

## Constraints & Assumptions

### Constraints
- Must use existing n8n backend (no direct database access from Streamlit)
- No authentication required (internal network deployment)
- Streamlit single-page application (limited to tab-based navigation)
- GitHub + Streamlit Cloud deployment only
- Text-only responses from AI chatbot

### Assumptions
- n8n webhooks are stable and performant
- Supabase database has proper indexes for query performance
- Network connectivity is reliable for auto-refresh
- Users have modern web browsers (Chrome, Edge, Firefox)
- Data volume remains manageable for Streamlit (< 10k rows per table)

## Technology Stack

### Frontend
- **Framework**: Streamlit (Python)
- **Charting**: Plotly (interactive charts)
- **Data Handling**: Pandas (data manipulation)
- **HTTP Client**: Requests (n8n webhook calls)
- **UI Components**: Streamlit native + streamlit-extras

### Backend (Existing)
- **Workflow**: n8n
- **Database**: Supabase (PostgreSQL)
- **AI**: OpenAI GPT + PostgreSQL memory
- **Authentication**: Supabase Auth (handled by n8n)

### Deployment
- **Version Control**: GitHub
- **Hosting**: Streamlit Community Cloud
- **CI/CD**: GitHub Actions (optional)

## Project Timeline Estimate

- **Phase 1**: Core Dashboard Setup (Inventory tab) - 1 week
- **Phase 2**: Maintenance & Tool Tabs - 1 week
- **Phase 3**: AI Chatbot Integration - 3 days
- **Phase 4**: Alert System - 3 days
- **Phase 5**: Report Generation - 1 week
- **Phase 6**: Advanced Filters & Search - 3 days
- **Phase 7**: Deployment & Testing - 3 days

**Total**: ~4 weeks

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|------------|
| n8n webhook latency | Dashboard slowness | Implement caching, loading states |
| Streamlit Community Cloud limits | App performance | Optimize data queries, pagination |
| AI chatbot hallucinations | Incorrect insights | Add disclaimers, verify critical data |
| No authentication | Unauthorized access | Deploy on internal network only |
| Large dataset rendering | Browser crashes | Implement pagination, lazy loading |

## Future Enhancements

- Mobile-responsive design
- User authentication and role-based access
- Email/SMS alert notifications
- Predictive maintenance using ML
- Integration with IoT sensors
- Offline mode capability
- Multi-language support (Malay, Mandarin)
- Advanced analytics (forecasting, anomaly detection)

---

**Project Start Date**: 2026-02-26
**Status**: Planning Phase
**Owner**: Development Team
**Stakeholders**: Petronas Electrical Maintenance Division
