# Requirements - Petronas EMCAI

## Functional Requirements

### FR1: Dashboard Infrastructure
**Priority**: P0 (Critical)

- **FR1.1**: Single-page Streamlit application with tabbed navigation
  - Tabs: Overview, Inventory, Maintenance, Tools, AI Assistant, Reports
  - Consistent header with app title and real-time timestamp
  - Responsive layout adapting to different screen sizes

- **FR1.2**: Auto-refresh mechanism
  - Configurable refresh interval (default: 30 seconds)
  - Manual refresh button
  - Last updated timestamp display
  - Loading states during data fetch

### FR2: Component Inventory Management
**Priority**: P0 (Critical)

- **FR2.1**: Display component inventory in searchable/filterable table
  - Columns: Component_ID, Item_Name, Category, Specification, Manufacturer, Stock_Qty, Unit_Price, Location, Condition, Last_Audit
  - Sortable by any column
  - Paginated view (50 items per page default)

- **FR2.2**: Inventory filters
  - Multi-select: Location, Manufacturer, Condition
  - Text search: Component_ID, Item_Name, Specification
  - Stock range slider: Min/Max stock quantity
  - Date range: Last_Audit dates

- **FR2.3**: Low stock alerts
  - Critical threshold: Stock_Qty < 10 (red indicator)
  - Warning threshold: Stock_Qty 10-15 (yellow indicator)
  - Visual highlighting in table rows
  - Alert count badge on Inventory tab

- **FR2.4**: Overdue audit alerts
  - Warning: Last_Audit > 90 days from current date
  - Visual highlighting in table rows
  - Alert count badge on Inventory tab

- **FR2.5**: Inventory visualizations
  - Bar chart: Stock quantity by location
  - Pie chart: Condition distribution (New/Used/Refurbished)
  - Bar chart: Component count by manufacturer
  - Metric cards: Total components, Total value, Low stock count, Overdue audits

### FR3: Maintenance Log Management
**Priority**: P0 (Critical)

- **FR3.1**: Display maintenance logs in searchable/filterable table
  - Columns: Log_ID, Date, Component_ID, Task_Type, Technician, Outcome, Remarks
  - Sortable by any column (default: Date descending)
  - Paginated view

- **FR3.2**: Maintenance filters
  - Multi-select: Task_Type, Technician, Outcome
  - Date range picker
  - Text search: Component_ID, Remarks
  - Quick filters: Last 7 days, Last 30 days, This year

- **FR3.3**: Maintenance visualizations
  - Line chart: Maintenance tasks over time
  - Bar chart: Tasks by type (Emergency, Inspection, Corrective, Preventive)
  - Bar chart: Outcome distribution (Pass, Fail, Warning)
  - Bar chart: Technician workload
  - Horizontal bar: Top 10 most maintained components
  - Metric cards: Total tasks, Failure rate, Emergency tasks, Avg response time

- **FR3.4**: Failure analysis
  - Filterable list of failed maintenance tasks
  - Common failure modes extraction from Remarks
  - Component failure frequency ranking
  - Technician-specific failure patterns

### FR4: Tool Tracking Management
**Priority**: P0 (Critical)

- **FR4.1**: Display tool tracking in searchable/filterable table
  - Columns: Tracking_ID, Tool_Name, Assigned_To, Date_Out, Date_Due, Status, Condition
  - Sortable by any column
  - Paginated view

- **FR4.2**: Tool filters
  - Multi-select: Tool_Name, Assigned_To, Status, Condition
  - Date range: Date_Out, Date_Due
  - Quick filters: Available, Checked out, Overdue, Lost, Damaged

- **FR4.3**: Tool availability alerts
  - Overdue tools: Date_Due < Today AND Status = "Overdue" (red)
  - Lost tools: Status = "Lost" (red)
  - Damaged tools: Condition = "Damaged" or "Needs Calibration" (yellow)
  - Alert count badges on Tools tab

- **FR4.4**: Tool visualizations
  - Gauge chart: Available vs Checked out ratio
  - Bar chart: Tool usage by technician
  - Pie chart: Tool status distribution
  - Timeline: Tool checkout/return history
  - Metric cards: Total tools, Available, Overdue, Lost/Damaged

### FR5: AI Chatbot Integration
**Priority**: P1 (High)

- **FR5.1**: Chat interface in dedicated "AI Assistant" tab
  - Text input box for natural language queries
  - Submit button and Enter key support
  - Chat history display (user messages + AI responses)
  - Clear chat button

- **FR5.2**: GraphRAG endpoint integration
  - POST to: `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`
  - Send user query in request body
  - Display streaming or complete text response
  - Handle errors gracefully with user-friendly messages

- **FR5.3**: Quick action examples
  - Display 5-7 example queries as clickable buttons:
    - "Show me all PLC processors in YARD-ALPHA locations"
    - "What maintenance issues did John Doe encounter this month?"
    - "Which tools are currently overdue?"
    - "Generate a summary of battery failures in 2025"
    - "What's the total value of refurbished components?"
    - "List all Siemens equipment in SUBSTATION locations"
  - Clicking example populates input and submits

- **FR5.4**: Response rendering
  - Markdown support for formatted responses
  - Auto-detect and highlight: Component IDs, Log IDs, Tool IDs
  - Copy response button
  - Timestamp for each message

### FR6: Alert System
**Priority**: P1 (High)

- **FR6.1**: Global alert banner
  - Fixed position at top of page (below header)
  - Display critical alerts (low stock < 10, overdue > 30 days)
  - Color-coded: Red (critical), Yellow (warning), Blue (info)
  - Dismissable per session
  - Click to navigate to relevant tab

- **FR6.2**: Sidebar alert summary
  - Alert count badges per category
  - Expandable alert list with details
  - Quick filters to show alerts by type

- **FR6.3**: In-table highlighting
  - Color-coded row backgrounds for alerted items
  - Icon indicators in first column
  - Tooltip on hover explaining alert reason

### FR7: Report Generation
**Priority**: P1 (High)

- **FR7.1**: Daily Inventory Summary Report
  - Total stock value (sum of Stock_Qty × Unit_Price)
  - Components added/removed today (requires change tracking)
  - Low stock alerts (count and list)
  - Overdue audits (count and list)
  - Generate as CSV/Excel

- **FR7.2**: Weekly Maintenance Report
  - Tasks completed by type (last 7 days)
  - Failure rate trend (pass/fail/warning percentages)
  - Technician performance (tasks completed, avg outcome)
  - Critical issues requiring attention
  - Generate as PDF/CSV

- **FR7.3**: Monthly Tool Utilization Report
  - Tool usage frequency (checkout count per tool)
  - Lost/damaged tool summary
  - Calibration due list (Condition = "Needs Calibration")
  - Cost analysis (if applicable)
  - Generate as Excel/CSV

- **FR7.4**: Failure Analysis Report (Custom date range)
  - Failures by component type
  - Failures by location
  - Failures by technician
  - Common failure modes (extracted from Remarks)
  - Preventive recommendations (AI-generated or manual)
  - Generate as PDF

- **FR7.5**: Report download functionality
  - Download buttons for each report type
  - Format selection: CSV, Excel (.xlsx), PDF
  - Auto-generated filename with timestamp
  - Progress indicator during generation

### FR8: Search & Filter System
**Priority**: P1 (High)

- **FR8.1**: Global search
  - Search box in header (searches across all data)
  - Returns results grouped by data type (Components, Logs, Tools)
  - Click result to navigate to relevant tab with filters applied

- **FR8.2**: Advanced filters (per tab)
  - **Location filter**: Multi-select dropdown with autocomplete
    - YARD-ALPHA-*, WH-ZN-*, SUBSTATION-*, etc.
  - **Manufacturer filter**: Multi-select (GE Alstom, ABB, Schneider, Siemens, Crompton, Eaton)
  - **Condition filter**: Multi-select (New, Used, Refurbished)
  - **Date range filter**: Calendar picker (for logs and tool tracking)
  - **Technician filter**: Multi-select dropdown
  - **Component type filter**: Auto-extracted from Item_Name (PLC, Battery, Transformer, Cable, Inverter, Relay)
  - **Task type filter**: Multi-select (Emergency, Inspection, Corrective, Preventive)
  - **Tool status filter**: Multi-select (Available, Overdue, Returned, Lost)

- **FR8.3**: Filter state management
  - Persist filters during session
  - "Clear all filters" button
  - Active filter count indicator
  - URL parameter support for shareable filtered views (nice-to-have)

### FR9: Data Operations (via n8n Webhooks)
**Priority**: P0 (Critical)

- **FR9.1**: Read operations (GET)
  - Fetch all components (with optional filters)
  - Fetch all maintenance logs (with optional filters)
  - Fetch all tool tracking records (with optional filters)
  - Error handling for failed requests
  - Retry logic (max 3 attempts)

- **FR9.2**: Create operations (POST)
  - Add new component (form with validation)
  - Log maintenance activity (form with validation)
  - Check out tool (form with validation)
  - Success confirmation message
  - Refresh data after successful creation

- **FR9.3**: Update operations (PUT)
  - Update component stock/condition (inline edit or modal)
  - Update maintenance log (edit modal)
  - Return tool / update tool status (quick action button)
  - Optimistic UI updates
  - Rollback on failure

- **FR9.4**: Delete operations (DELETE)
  - Remove component (with confirmation dialog)
  - Delete maintenance log (with confirmation dialog)
  - Remove tool from tracking (with confirmation dialog)
  - Soft delete preferred (mark as inactive)

### FR10: Overview Dashboard Tab
**Priority**: P1 (High)

- **FR10.1**: KPI metrics
  - Total components count
  - Total inventory value (RM)
  - Low stock alerts count
  - Overdue audits count
  - Maintenance tasks (last 30 days)
  - Failure rate percentage
  - Tools available / total
  - Overdue tools count

- **FR10.2**: Summary visualizations
  - Inventory health (pie chart: Good stock, Low stock, Overdue audit)
  - Maintenance trends (line chart: last 90 days)
  - Tool status (donut chart: Available, Out, Overdue, Lost)
  - Top 5 locations by component count (bar chart)
  - Recent activity feed (last 10 maintenance logs)

- **FR10.3**: Quick actions
  - "Log Maintenance" button (opens form)
  - "Check Out Tool" button (opens form)
  - "Add Component" button (opens form)
  - "Generate Report" button (opens report selection)

## Non-Functional Requirements

### NFR1: Performance
**Priority**: P0 (Critical)

- **NFR1.1**: Page load time < 3 seconds on standard internet connection
- **NFR1.2**: Data refresh time < 2 seconds for all operations
- **NFR1.3**: Support up to 10,000 records per table without performance degradation
- **NFR1.4**: Chart rendering time < 1 second
- **NFR1.5**: AI chatbot response time < 5 seconds (depends on GraphRAG backend)

### NFR2: Reliability
**Priority**: P0 (Critical)

- **NFR2.1**: 99% uptime (excluding scheduled maintenance)
- **NFR2.2**: Graceful degradation if n8n backend is unavailable
- **NFR2.3**: Data integrity maintained during concurrent operations
- **NFR2.4**: Automatic reconnection on network interruption
- **NFR2.5**: Error messages logged for debugging

### NFR3: Usability
**Priority**: P1 (High)

- **NFR3.1**: Intuitive navigation requiring no training
- **NFR3.2**: Consistent UI/UX across all tabs
- **NFR3.3**: Responsive design (desktop, tablet support; mobile optional)
- **NFR3.4**: Accessible color contrast (WCAG 2.1 AA minimum)
- **NFR3.5**: Keyboard navigation support

### NFR4: Maintainability
**Priority**: P1 (High)

- **NFR4.1**: Modular code structure (separate files per tab/component)
- **NFR4.2**: Configuration file for n8n webhook URLs
- **NFR4.3**: Comprehensive inline code comments
- **NFR4.4**: Requirements.txt for dependency management
- **NFR4.5**: README with setup and deployment instructions

### NFR5: Security
**Priority**: P1 (High)

- **NFR5.1**: HTTPS-only communication with n8n webhooks
- **NFR5.2**: No sensitive data (passwords, API keys) in code
- **NFR5.3**: Environment variables for configuration
- **NFR5.4**: Input validation to prevent injection attacks
- **NFR5.5**: Rate limiting on n8n webhook calls (if supported)

### NFR6: Scalability
**Priority**: P2 (Medium)

- **NFR6.1**: Pagination for large datasets
- **NFR6.2**: Lazy loading of charts and heavy components
- **NFR6.3**: Caching of frequently accessed data (session-level)
- **NFR6.4**: Optimized database queries via n8n (filtering on backend)

### NFR7: Deployment
**Priority**: P0 (Critical)

- **NFR7.1**: Deploy to Streamlit Community Cloud via GitHub
- **NFR7.2**: One-click deployment from GitHub repository
- **NFR7.3**: Environment variables configured in Streamlit Cloud settings
- **NFR7.4**: Automatic redeployment on git push to main branch
- **NFR7.5**: No authentication required (internal network access)

## Data Requirements

### DR1: Data Schemas

**Component Inventory Schema:**
```python
{
  "Component_ID": str,        # Primary key, e.g., "PLC-CPU-1001"
  "Item_Name": str,           # e.g., "PLC Processor"
  "Category": str,            # e.g., "Electrical"
  "Specification": str,       # e.g., "S7-1500 / ControlLogix"
  "Manufacturer": str,        # e.g., "GE Alstom"
  "Stock_Qty": int,           # Current quantity
  "Unit_Price": float,        # Price in RM
  "Location": str,            # e.g., "YARD-ALPHA-65"
  "Condition": str,           # "New" | "Used" | "Refurbished"
  "Last_Audit": date          # Last audit date (YYYY-MM-DD)
}
```

**Maintenance Log Schema:**
```python
{
  "Log_ID": str,              # Primary key, e.g., "LOG-2025-0001"
  "Date": date,               # Maintenance date (YYYY-MM-DD)
  "Component_ID": str,        # Foreign key to Component_ID
  "Task_Type": str,           # "Emergency" | "Inspection" | "Corrective" | "Preventive"
  "Technician": str,          # Technician name
  "Outcome": str,             # "Pass" | "Fail" | "Warning"
  "Remarks": str              # Freetext notes
}
```

**Tool Tracking Schema:**
```python
{
  "Tracking_ID": str,         # Primary key, e.g., "TRK-5001"
  "Tool_Name": str,           # e.g., "Fluke Multimeter"
  "Assigned_To": str,         # Technician name
  "Date_Out": date,           # Checkout date (YYYY-MM-DD)
  "Date_Due": date,           # Due date (YYYY-MM-DD)
  "Status": str,              # "Overdue" | "Returned" | "Lost"
  "Condition": str            # "Good" | "Damaged" | "Needs Calibration"
}
```

### DR2: Data Validation Rules

- **Component_ID**: Alphanumeric, max 20 characters, unique
- **Stock_Qty**: Non-negative integer
- **Unit_Price**: Non-negative float, max 2 decimal places
- **Dates**: Valid ISO format (YYYY-MM-DD), not future dates (except Date_Due)
- **Condition**: Must be one of predefined values
- **Task_Type**: Must be one of predefined values
- **Outcome**: Must be one of predefined values
- **Status**: Must be one of predefined values

### DR3: Data Integrity

- **Referential Integrity**: Component_ID in Maintenance Log must exist in Component Inventory
- **Date Logic**: Date_Out < Date_Due for tool tracking
- **No Orphaned Records**: Deleting a component should handle associated maintenance logs (cascade or prevent)

## Integration Requirements

### IR1: n8n Webhook Integration

- **IR1.1**: Centralized webhook configuration
  - Store all n8n endpoints in `config.py` or `.env`
  - Endpoints needed:
    - GET `/components` - Fetch components (with filter params)
    - POST `/components` - Create component
    - PUT `/components/{id}` - Update component
    - DELETE `/components/{id}` - Delete component
    - GET `/logs` - Fetch maintenance logs (with filter params)
    - POST `/logs` - Create log
    - PUT `/logs/{id}` - Update log
    - DELETE `/logs/{id}` - Delete log
    - GET `/tools` - Fetch tool tracking (with filter params)
    - POST `/tools` - Create tool record
    - PUT `/tools/{id}` - Update tool record
    - DELETE `/tools/{id}` - Delete tool record

- **IR1.2**: Request/Response handling
  - Standard JSON payloads
  - HTTP status code handling (200, 201, 400, 404, 500)
  - Timeout handling (max 10 seconds per request)
  - Retry logic with exponential backoff

### IR2: GraphRAG AI Integration

- **IR2.1**: Chat endpoint
  - URL: `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`
  - Method: POST
  - Payload: `{ "query": "user question here" }`
  - Response: `{ "response": "AI answer here" }` (or similar structure)
  - Timeout: 30 seconds (AI may take longer)

- **IR2.2**: Error handling
  - Display user-friendly message on timeout
  - Fallback message: "The AI assistant is currently unavailable. Please try again later."
  - Log errors for debugging

### IR3: Streamlit Cloud Deployment

- **IR3.1**: GitHub repository structure
  ```
  /
  ├── app.py                 # Main Streamlit entry point
  ├── requirements.txt       # Python dependencies
  ├── .streamlit/
  │   └── config.toml        # Streamlit configuration
  ├── config.py              # App configuration (webhooks, constants)
  ├── pages/
  │   ├── overview.py
  │   ├── inventory.py
  │   ├── maintenance.py
  │   ├── tools.py
  │   ├── ai_assistant.py
  │   └── reports.py
  ├── utils/
  │   ├── api_client.py      # n8n webhook wrapper
  │   ├── charts.py          # Visualization helpers
  │   ├── alerts.py          # Alert logic
  │   └── filters.py         # Filter helpers
  └── README.md
  ```

- **IR3.2**: Environment variables (set in Streamlit Cloud)
  - `N8N_BASE_URL` - n8n instance base URL
  - `N8N_WEBHOOK_PREFIX` - Webhook path prefix
  - `GRAPHRAG_ENDPOINT` - AI chatbot URL
  - `REFRESH_INTERVAL` - Auto-refresh interval (seconds)

## UI/UX Requirements

### UIR1: Design Principles

- **UIR1.1**: Minimalist, professional design
- **UIR1.2**: Petronas brand colors (if available, otherwise neutral palette)
- **UIR1.3**: Clear visual hierarchy (headings, subheadings, body text)
- **UIR1.4**: Consistent spacing and alignment
- **UIR1.5**: Accessible font sizes (minimum 14px body text)

### UIR2: Component Standards

- **UIR2.1**: Buttons
  - Primary actions: Filled button (blue)
  - Secondary actions: Outlined button (gray)
  - Destructive actions: Red button (delete, remove)

- **UIR2.2**: Tables
  - Striped rows for readability
  - Sticky header on scroll
  - Hover highlight on rows
  - Sort indicators on columns

- **UIR2.3**: Forms
  - Clear labels above inputs
  - Validation messages below inputs
  - Required field indicators (*)
  - Submit and Cancel buttons

- **UIR2.4**: Alerts
  - Icon + message + dismiss button
  - Color-coded backgrounds (red, yellow, blue, green)
  - Auto-dismiss after 5 seconds (optional)

### UIR3: Navigation

- **UIR3.1**: Tab bar at top (horizontal)
- **UIR3.2**: Active tab highlighted
- **UIR3.3**: Badge indicators on tabs (alert counts)
- **UIR3.4**: Breadcrumb navigation (if nested views)

## Testing Requirements

### TR1: Unit Testing (Optional for Streamlit)

- Test utility functions (filters, calculations, formatting)
- Test API client wrapper (mock n8n responses)

### TR2: Integration Testing

- Test n8n webhook connectivity
- Test GraphRAG endpoint
- Test data CRUD operations end-to-end

### TR3: User Acceptance Testing

- Verify all functional requirements with stakeholders
- Test with sample data from provided screenshots
- Validate alert thresholds with actual users
- Confirm report formats meet user needs

### TR4: Performance Testing

- Load test with 10,000+ records
- Measure page load times
- Test auto-refresh overhead
- Validate chart rendering performance

## Acceptance Criteria

### AC1: Core Functionality

- ✅ All six tabs render correctly
- ✅ Data loads from n8n webhooks without errors
- ✅ Filters and search work across all tabs
- ✅ CRUD operations succeed via n8n
- ✅ AI chatbot responds to queries
- ✅ Reports generate and download successfully

### AC2: Alert System

- ✅ Low stock alerts trigger correctly (< 10 critical, 10-15 warning)
- ✅ Overdue audit alerts trigger correctly (> 90 days)
- ✅ Overdue tool alerts trigger correctly (Date_Due < Today)
- ✅ Alerts display in banner, sidebar, and table highlights

### AC3: Visualizations

- ✅ All charts render with correct data
- ✅ Charts update when filters applied
- ✅ Metric cards show accurate counts/values
- ✅ No visual glitches or overlapping elements

### AC4: Performance

- ✅ Page loads in < 3 seconds
- ✅ Auto-refresh works without UI freeze
- ✅ No lag with 1,000+ records displayed
- ✅ AI chatbot responds in < 10 seconds

### AC5: Deployment

- ✅ App deploys successfully to Streamlit Cloud
- ✅ Environment variables configured correctly
- ✅ No errors in Streamlit logs
- ✅ Public URL accessible (or network-restricted as needed)

### AC6: User Satisfaction

- ✅ Technicians can find component locations quickly
- ✅ Managers can generate weekly reports in < 1 minute
- ✅ AI chatbot answers 70%+ of queries correctly
- ✅ Users report improved efficiency over previous process

## Out of Scope

### OS1: Explicitly Not Included

- ❌ Mobile app (only web-based Streamlit)
- ❌ User authentication/authorization (no login required)
- ❌ Email/SMS alert notifications (in-app only)
- ❌ Predictive maintenance ML models
- ❌ IoT sensor integration
- ❌ Offline mode / PWA functionality
- ❌ Multi-language support (English only)
- ❌ Advanced analytics (forecasting, anomaly detection)
- ❌ Custom branding themes per user
- ❌ Integration with other enterprise systems (ERP, CMMS)

### OS2: Future Considerations

- 🔮 Role-based access control (RBAC)
- 🔮 Audit trail and change logs
- 🔮 Advanced AI features (predictive failures, recommendations)
- 🔮 Mobile-responsive redesign
- 🔮 Real-time push notifications
- 🔮 Integration with Petronas existing systems

---

**Document Version**: 1.0
**Last Updated**: 2026-02-26
**Status**: Approved for Development
