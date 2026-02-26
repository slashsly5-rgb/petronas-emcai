# Roadmap - Petronas EMCAI

## Project Overview

**Goal**: Build a Streamlit-based SaaS dashboard for Petronas electrical maintenance teams to manage component inventory, maintenance logs, and tool tracking with AI-powered insights.

**Timeline**: ~4 weeks (7 phases)
**Start Date**: 2026-02-26

---

## Phase 1: Project Foundation & Infrastructure
**Duration**: 2-3 days
**Status**: Not Started

### Objectives
- Set up project repository and development environment
- Create core Streamlit app structure
- Establish n8n webhook integration framework
- Implement basic navigation and layout

### Deliverables
- ✅ GitHub repository initialized
- ✅ Project structure with modular architecture
- ✅ `requirements.txt` with dependencies
- ✅ `config.py` for centralized configuration
- ✅ `utils/api_client.py` - n8n webhook wrapper
- ✅ Basic Streamlit app with tab navigation (6 tabs)
- ✅ `.streamlit/config.toml` for app settings
- ✅ README.md with setup instructions

### Requirements Covered
- NFR4: Maintainability (modular code structure)
- NFR7: Deployment (GitHub setup)
- IR3.1: Repository structure

### Success Criteria
- ✅ App runs locally with `streamlit run app.py`
- ✅ All 6 tabs render (even if empty)
- ✅ n8n webhook test succeeds (ping endpoint)

---

## Phase 2: Component Inventory Dashboard
**Duration**: 4-5 days
**Status**: Not Started

### Objectives
- Implement full inventory management functionality
- Display component data in searchable/filterable table
- Create inventory visualizations
- Build alert system for low stock and overdue audits

### Deliverables
- ✅ `pages/inventory.py` - Inventory tab implementation
- ✅ n8n integration: GET /components
- ✅ Inventory data table with sorting and pagination
- ✅ Multi-filter system (Location, Manufacturer, Condition, Stock range, Audit dates)
- ✅ Low stock alert logic (< 10 critical, 10-15 warning)
- ✅ Overdue audit alert logic (> 90 days)
- ✅ Inventory visualizations:
  - Bar chart: Stock by location
  - Pie chart: Condition distribution
  - Bar chart: Component count by manufacturer
  - Metric cards: Total components, Total value, Low stock, Overdue audits
- ✅ `utils/alerts.py` - Alert calculation helpers
- ✅ `utils/filters.py` - Filter logic helpers

### Requirements Covered
- FR2: Component Inventory Management (all sub-requirements)
- FR6.3: In-table highlighting for alerts
- NFR1.3: Support 10,000+ records

### Success Criteria
- ✅ Inventory table displays all components from n8n
- ✅ Filters work correctly and persist during session
- ✅ Low stock and overdue audit alerts trigger accurately
- ✅ Charts render without lag (<1 second)
- ✅ Table supports sorting, searching, and pagination

---

## Phase 3: Maintenance Log Dashboard
**Duration**: 3-4 days
**Status**: Not Started

### Objectives
- Display maintenance log history with advanced filtering
- Visualize maintenance trends and failure patterns
- Implement failure analysis features

### Deliverables
- ✅ `pages/maintenance.py` - Maintenance tab implementation
- ✅ n8n integration: GET /logs
- ✅ Maintenance log table with sorting and pagination
- ✅ Multi-filter system (Task Type, Technician, Outcome, Date range)
- ✅ Quick filters (Last 7 days, Last 30 days, This year)
- ✅ Maintenance visualizations:
  - Line chart: Tasks over time
  - Bar chart: Tasks by type
  - Bar chart: Outcome distribution
  - Bar chart: Technician workload
  - Horizontal bar: Top 10 most maintained components
  - Metric cards: Total tasks, Failure rate, Emergency tasks
- ✅ Failure analysis section:
  - Filterable failed tasks
  - Common failure modes extraction (from Remarks)
  - Component failure frequency ranking

### Requirements Covered
- FR3: Maintenance Log Management (all sub-requirements)
- DR1: Maintenance Log Schema validation

### Success Criteria
- ✅ Log table displays all maintenance records
- ✅ Filters work correctly (including date ranges)
- ✅ Failure analysis accurately extracts patterns from Remarks
- ✅ Charts update dynamically with filter changes
- ✅ Technician workload chart shows accurate data

---

## Phase 4: Tool Tracking Dashboard
**Duration**: 3-4 days
**Status**: Not Started

### Objectives
- Display tool tracking records with availability status
- Implement tool availability alerts
- Visualize tool utilization patterns

### Deliverables
- ✅ `pages/tools.py` - Tools tab implementation
- ✅ n8n integration: GET /tools
- ✅ Tool tracking table with sorting and pagination
- ✅ Multi-filter system (Tool Name, Assigned To, Status, Condition, Date range)
- ✅ Quick filters (Available, Checked out, Overdue, Lost, Damaged)
- ✅ Tool availability alerts:
  - Overdue tools (Date_Due < Today AND Status = "Overdue")
  - Lost tools (Status = "Lost")
  - Damaged tools (Condition = "Damaged" or "Needs Calibration")
- ✅ Tool visualizations:
  - Gauge chart: Available vs Checked out ratio
  - Bar chart: Tool usage by technician
  - Pie chart: Tool status distribution
  - Timeline: Checkout/return history
  - Metric cards: Total tools, Available, Overdue, Lost/Damaged

### Requirements Covered
- FR4: Tool Tracking Management (all sub-requirements)
- FR6.3: In-table highlighting for tool alerts

### Success Criteria
- ✅ Tool table displays all tracking records
- ✅ Overdue/lost/damaged alerts trigger correctly
- ✅ Gauge chart accurately shows availability ratio
- ✅ Timeline visualization shows checkout/return patterns
- ✅ Quick filters work as expected

---

## Phase 5: AI Chatbot Integration
**Duration**: 2-3 days
**Status**: Not Started

### Objectives
- Integrate GraphRAG AI endpoint into dashboard
- Build interactive chat interface
- Provide example queries and chat history

### Deliverables
- ✅ `pages/ai_assistant.py` - AI Assistant tab implementation
- ✅ Chat interface with text input and history display
- ✅ Integration with n8n GraphRAG endpoint:
  - URL: `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`
  - POST request with user query
  - Display text response
- ✅ Quick action example queries (5-7 buttons):
  - "Show me all PLC processors in YARD-ALPHA locations"
  - "What maintenance issues did John Doe encounter this month?"
  - "Which tools are currently overdue?"
  - "Generate a summary of battery failures in 2025"
  - "What's the total value of refurbished components?"
  - "List all Siemens equipment in SUBSTATION locations"
- ✅ Chat history preservation during session
- ✅ Markdown rendering for AI responses
- ✅ Error handling for timeouts and failed requests
- ✅ Loading indicator while waiting for response

### Requirements Covered
- FR5: AI Chatbot Integration (all sub-requirements)
- IR2: GraphRAG AI Integration

### Success Criteria
- ✅ User can type and submit queries
- ✅ AI responds with relevant text answers
- ✅ Example queries work when clicked
- ✅ Chat history displays correctly
- ✅ Error messages shown gracefully if endpoint fails
- ✅ Response time < 10 seconds (or timeout message)

---

## Phase 6: Alert System & Overview Dashboard
**Duration**: 3-4 days
**Status**: Not Started

### Objectives
- Build global alert banner and sidebar summary
- Create comprehensive Overview tab with KPIs
- Implement quick action buttons

### Deliverables
- ✅ `pages/overview.py` - Overview tab implementation
- ✅ Global alert banner (fixed at top):
  - Critical alerts (low stock < 10, overdue > 30 days)
  - Color-coded (red, yellow, blue)
  - Dismissable per session
  - Click to navigate to relevant tab
- ✅ Sidebar alert summary:
  - Alert count badges per category
  - Expandable alert list
- ✅ Overview KPI metrics:
  - Total components count
  - Total inventory value (RM)
  - Low stock alerts count
  - Overdue audits count
  - Maintenance tasks (last 30 days)
  - Failure rate percentage
  - Tools available / total
  - Overdue tools count
- ✅ Overview visualizations:
  - Inventory health pie chart
  - Maintenance trends line chart (last 90 days)
  - Tool status donut chart
  - Top 5 locations by component count bar chart
  - Recent activity feed (last 10 maintenance logs)
- ✅ Quick action buttons:
  - "Log Maintenance" (opens form)
  - "Check Out Tool" (opens form)
  - "Add Component" (opens form)
  - "Generate Report" (opens report selection)

### Requirements Covered
- FR6: Alert System (all sub-requirements)
- FR10: Overview Dashboard Tab (all sub-requirements)

### Success Criteria
- ✅ Alert banner displays critical alerts on all pages
- ✅ Clicking alerts navigates to correct tab with filters
- ✅ Overview tab shows accurate KPIs
- ✅ All visualizations render correctly
- ✅ Quick actions open appropriate forms/modals

---

## Phase 7: Report Generation & CRUD Operations
**Duration**: 4-5 days
**Status**: Not Started

### Objectives
- Implement automated report generation
- Build CRUD forms for data operations
- Enable report downloads in multiple formats

### Deliverables
- ✅ `pages/reports.py` - Reports tab implementation
- ✅ Report types:
  - **Daily Inventory Summary**
    - Total stock value
    - Low stock alerts list
    - Overdue audits list
    - Download as CSV/Excel
  - **Weekly Maintenance Report**
    - Tasks by type (last 7 days)
    - Failure rate trend
    - Technician performance
    - Download as PDF/CSV
  - **Monthly Tool Utilization**
    - Tool usage frequency
    - Lost/damaged summary
    - Calibration due list
    - Download as Excel/CSV
  - **Failure Analysis Report** (custom date range)
    - Failures by component type, location, technician
    - Common failure modes
    - Download as PDF
- ✅ Report download functionality:
  - Format selection (CSV, Excel, PDF)
  - Auto-generated filenames with timestamps
  - Progress indicators
- ✅ CRUD forms (modals or inline):
  - **Add Component** (POST /components)
  - **Update Component** (PUT /components/{id})
  - **Delete Component** (DELETE /components/{id})
  - **Log Maintenance** (POST /logs)
  - **Update Maintenance Log** (PUT /logs/{id})
  - **Delete Maintenance Log** (DELETE /logs/{id})
  - **Check Out Tool** (POST /tools)
  - **Return Tool** (PUT /tools/{id})
  - **Delete Tool** (DELETE /tools/{id})
- ✅ Form validation and error handling
- ✅ Success confirmation messages
- ✅ Data refresh after successful CRUD operations

### Requirements Covered
- FR7: Report Generation (all sub-requirements)
- FR9: Data Operations via n8n (all sub-requirements)
- IR1: n8n Webhook Integration (CRUD endpoints)

### Success Criteria
- ✅ All report types generate correctly with sample data
- ✅ Reports download in all supported formats
- ✅ CRUD forms work for all data types
- ✅ Form validation prevents invalid submissions
- ✅ Data updates reflect immediately in dashboard

---

## Phase 8: Advanced Search, Filters & Polish
**Duration**: 2-3 days
**Status**: Not Started

### Objectives
- Implement global search across all data types
- Enhance filter UX with autocomplete and persistence
- Performance optimization and bug fixes
- Final UI/UX polish

### Deliverables
- ✅ Global search box in header:
  - Search across Components, Logs, Tools
  - Results grouped by data type
  - Click result to navigate with filters applied
- ✅ Enhanced filters:
  - Autocomplete for location and manufacturer
  - Filter state persistence (session storage)
  - "Clear all filters" button
  - Active filter count indicators
- ✅ Performance optimizations:
  - Pagination for large datasets
  - Lazy loading of charts
  - Session-level caching
- ✅ UI/UX improvements:
  - Consistent styling across tabs
  - Loading states for all async operations
  - Tooltips for unclear UI elements
  - Accessibility improvements (keyboard navigation, ARIA labels)
- ✅ Bug fixes and edge case handling
- ✅ `utils/charts.py` - Refactored chart generation

### Requirements Covered
- FR8: Search & Filter System (all sub-requirements)
- NFR3: Usability
- NFR6: Scalability (pagination, lazy loading, caching)

### Success Criteria
- ✅ Global search returns relevant results across all data
- ✅ Filters persist during session
- ✅ No performance lag with 10,000+ records
- ✅ UI is consistent and polished
- ✅ No critical bugs in any functionality

---

## Phase 9: Deployment & Testing
**Duration**: 2-3 days
**Status**: Not Started

### Objectives
- Deploy to Streamlit Community Cloud
- Configure environment variables
- Conduct integration and UAT testing
- Create user documentation

### Deliverables
- ✅ Streamlit Cloud deployment:
  - GitHub repository connected
  - Environment variables configured:
    - `N8N_BASE_URL`
    - `N8N_WEBHOOK_PREFIX`
    - `GRAPHRAG_ENDPOINT`
    - `REFRESH_INTERVAL`
  - Auto-deploy on git push enabled
- ✅ Integration testing:
  - All n8n webhook endpoints tested
  - GraphRAG AI chatbot tested
  - CRUD operations validated end-to-end
- ✅ Performance testing:
  - Load test with 10,000+ records
  - Page load time measurements
  - Auto-refresh overhead validation
- ✅ User Acceptance Testing (UAT):
  - Verify all functional requirements
  - Test with real Petronas data (from screenshots)
  - Validate alert thresholds
  - Confirm report formats
- ✅ Documentation:
  - User guide (how to use dashboard)
  - Admin guide (how to configure webhooks)
  - Troubleshooting guide
  - README update with deployment instructions

### Requirements Covered
- NFR1: Performance (all sub-requirements)
- NFR7: Deployment (all sub-requirements)
- TR1-TR4: Testing Requirements

### Success Criteria
- ✅ App is live on Streamlit Cloud with public URL
- ✅ All environment variables configured correctly
- ✅ No errors in Streamlit logs
- ✅ Page loads in < 3 seconds
- ✅ All functional tests pass
- ✅ UAT feedback incorporated
- ✅ Documentation complete and accessible

---

## Milestone Summary

| Phase | Duration | Deliverables | Requirements |
|-------|----------|--------------|--------------|
| **1. Foundation** | 2-3 days | Project setup, n8n integration, tab structure | NFR4, NFR7, IR3.1 |
| **2. Inventory** | 4-5 days | Inventory table, filters, alerts, charts | FR2, FR6.3, NFR1.3 |
| **3. Maintenance** | 3-4 days | Log table, filters, failure analysis, charts | FR3, DR1 |
| **4. Tools** | 3-4 days | Tool table, alerts, availability charts | FR4, FR6.3 |
| **5. AI Chatbot** | 2-3 days | Chat interface, GraphRAG integration | FR5, IR2 |
| **6. Alerts & Overview** | 3-4 days | Alert banner, sidebar, Overview tab, KPIs | FR6, FR10 |
| **7. Reports & CRUD** | 4-5 days | Report generation, CRUD forms, downloads | FR7, FR9, IR1 |
| **8. Search & Polish** | 2-3 days | Global search, enhanced filters, optimizations | FR8, NFR3, NFR6 |
| **9. Deployment** | 2-3 days | Streamlit Cloud, testing, documentation | NFR1, NFR7, TR1-4 |

**Total Estimated Duration**: ~26-34 days (~4-5 weeks)

---

## Dependencies & Risks

### Dependencies
- ✅ n8n workflow backend is operational and accessible
- ✅ Supabase database has correct schema and sample data
- ✅ GraphRAG AI endpoint is functional
- ✅ Streamlit Community Cloud account available
- ✅ GitHub repository access

### Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| n8n webhook latency > 2s | Medium | High | Implement caching, optimize queries on n8n side |
| Streamlit Cloud free tier limits | Low | Medium | Monitor usage, upgrade if needed |
| AI chatbot hallucinations | High | Medium | Add disclaimers, verify critical queries manually |
| Large dataset rendering (>10k rows) | Medium | Medium | Implement pagination and lazy loading |
| GraphRAG endpoint downtime | Low | High | Add error handling, fallback messages |
| Requirement changes mid-development | Medium | High | Frequent stakeholder check-ins, iterative demos |

---

## Next Steps

1. **Approve this roadmap** with stakeholders
2. **Run `/gsd:plan-phase 1`** to create detailed execution plan for Phase 1
3. **Set up GitHub repository** and initial project structure
4. **Configure n8n webhook endpoints** (if not already done)
5. **Begin Phase 1 development**

---

**Roadmap Version**: 1.0
**Last Updated**: 2026-02-26
**Status**: Pending Approval
