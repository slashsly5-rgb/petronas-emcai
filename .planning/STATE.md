# Project State - Petronas EMCAI

## Current Status

**Phase**: Planning Complete
**Date**: 2026-02-26
**Next Action**: Run `/gsd:plan-phase 1` to begin Phase 1 development

---

## Session Context

### What We're Building
A Streamlit-based SaaS dashboard for Petronas electrical maintenance teams to manage:
- Component inventory (PLC processors, batteries, transformers, cables, etc.)
- Maintenance logs (emergency, inspection, corrective, preventive tasks)
- Tool tracking (multimeters, arc flash suits, laptops, safety harnesses, etc.)
- AI-powered insights via GraphRAG chatbot

### Key Technical Decisions
1. **Frontend**: Streamlit (Python) - Single-page app with tabs
2. **Backend**: Existing n8n workflow (all CRUD via webhooks)
3. **Database**: Supabase (PostgreSQL) - accessed through n8n only
4. **AI**: GraphRAG endpoint at `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`
5. **Deployment**: GitHub → Streamlit Community Cloud
6. **Authentication**: None (internal network access)
7. **Charting**: Plotly (interactive visualizations)

### Data Domains (from user-provided screenshots)
1. **Component Inventory** (44 items):
   - Electrical components (PLC, batteries, transformers, cables, inverters, relays)
   - Locations: YARD-ALPHA-*, WH-ZN-*, SUBSTATION-*
   - Manufacturers: GE Alstom, ABB, Schneider, Siemens, Crompton, Eaton
   - Conditions: New, Used, Refurbished
   - Stock quantities: 6-50 units
   - Unit prices: RM 45 - RM 15,000

2. **Maintenance Logs** (12 sample records):
   - Task types: Emergency, Inspection, Corrective, Preventive
   - Technicians: John Doe, Sarah Wong, Ahmad Zulkifli, Rajesh Kumar, Chong Wei
   - Outcomes: Pass, Fail, Warning
   - Common issues: Oil leakage, excessive vibration, communication errors, overheating, battery voltage drops

3. **Tool Tracking** (11 tools):
   - Tools: Megger Insulation Tester, Fluke Multimeter, Arc Flash Suit, Safety Harness, Laptop
   - Technicians: Same as above
   - Statuses: Overdue, Returned, Lost
   - Conditions: Good, Damaged, Needs Calibration

---

## Alert Thresholds (Confirmed)

### Inventory Alerts
- **Critical Low Stock**: Stock_Qty < 10 (red alert)
- **Warning Low Stock**: Stock_Qty 10-15 (yellow alert)
- **Overdue Audit**: Last_Audit > 90 days from today (yellow alert)

### Tool Alerts
- **Overdue**: Date_Due < Today AND Status = "Overdue" (red alert)
- **Lost**: Status = "Lost" (red alert)
- **Damaged**: Condition = "Damaged" or "Needs Calibration" (yellow alert)

---

## Roadmap Progress

### Phases (9 total)
1. ⏸️ **Foundation & Infrastructure** (2-3 days) - Not Started
2. ⏸️ **Component Inventory Dashboard** (4-5 days) - Not Started
3. ⏸️ **Maintenance Log Dashboard** (3-4 days) - Not Started
4. ⏸️ **Tool Tracking Dashboard** (3-4 days) - Not Started
5. ⏸️ **AI Chatbot Integration** (2-3 days) - Not Started
6. ⏸️ **Alert System & Overview Dashboard** (3-4 days) - Not Started
7. ⏸️ **Report Generation & CRUD Operations** (4-5 days) - Not Started
8. ⏸️ **Advanced Search, Filters & Polish** (2-3 days) - Not Started
9. ⏸️ **Deployment & Testing** (2-3 days) - Not Started

**Estimated Total Duration**: 26-34 days (~4-5 weeks)

---

## Key Requirements Summary

### Must-Have Features (P0)
- ✅ Single-page Streamlit app with 6 tabs (Overview, Inventory, Maintenance, Tools, AI Assistant, Reports)
- ✅ Real-time data from n8n webhooks (auto-refresh every 30s)
- ✅ Advanced search & filters across all datasets
- ✅ Alert system (low stock, overdue audits, overdue tools)
- ✅ Visualizations (bar charts, pie charts, line charts, gauges)
- ✅ AI chatbot integration (GraphRAG endpoint)
- ✅ CRUD operations via n8n webhooks
- ✅ Report generation (Daily Inventory, Weekly Maintenance, Monthly Tool Utilization, Failure Analysis)
- ✅ Multi-format downloads (CSV, Excel, PDF)
- ✅ Deployment to Streamlit Community Cloud

### Nice-to-Have Features (P1/P2)
- 🔮 URL parameter support for shareable filtered views
- 🔮 Offline mode / PWA functionality
- 🔮 Role-based access control
- 🔮 Email/SMS alert notifications
- 🔮 Predictive maintenance ML models

---

## Open Questions / Assumptions

### Assumptions Made
1. n8n webhooks are RESTful and return JSON
2. n8n handles authentication to Supabase (no auth needed in Streamlit)
3. Data volume stays < 10,000 rows per table
4. Network connectivity is stable for auto-refresh
5. Users have modern browsers (Chrome, Edge, Firefox)
6. GraphRAG endpoint returns plain text (no structured JSON for tables/charts)
7. Streamlit app will parse AI text responses and render charts manually

### Questions for Future Clarification
- [ ] Do we need audit trails for CRUD operations?
- [ ] Should we soft-delete records or hard-delete?
- [ ] Are there specific Petronas brand colors to use?
- [ ] Do we need multi-language support (Malay, Mandarin)?
- [ ] Should reports be scheduled/automated or manual only?

---

## Known Constraints

1. **No Direct Database Access**: All data operations MUST go through n8n webhooks
2. **No Authentication**: App assumes internal network deployment (no login required)
3. **Streamlit Limitations**: Single-page app with tabs only (no separate URLs per page)
4. **AI Response Format**: Text only (Streamlit must parse and visualize)
5. **Deployment**: Must use Streamlit Community Cloud (free tier limits may apply)

---

## Files Created

- ✅ `.planning/PROJECT.md` - Comprehensive project context document
- ✅ `.planning/config.json` - Workflow configuration
- ✅ `.planning/REQUIREMENTS.md` - Detailed functional and non-functional requirements
- ✅ `.planning/ROADMAP.md` - 9-phase development plan with timelines
- ✅ `.planning/STATE.md` - This file (project memory)

---

## Next Steps

1. **Review planning documents** with stakeholders
2. **Confirm n8n webhook endpoints** are ready:
   - GET/POST/PUT/DELETE for `/components`
   - GET/POST/PUT/DELETE for `/logs`
   - GET/POST/PUT/DELETE for `/tools`
   - POST to GraphRAG AI endpoint
3. **Run `/gsd:plan-phase 1`** to create detailed Phase 1 execution plan
4. **Set up GitHub repository** (if not already done)
5. **Begin coding Phase 1** (project foundation)

---

## Context for Future Sessions

**If resuming work later, you should know:**
- This is a **greenfield project** (starting from scratch)
- User has **existing n8n backend** (GraphRAG AI + CRUD webhooks)
- User provided **3 data screenshots** showing real component inventory, maintenance logs, and tool tracking data
- **No research phase needed** (requirements are clear from user input)
- **Alert thresholds are defined** (see above)
- **GraphRAG endpoint URL confirmed**: `https://n8n.srv986677.hstgr.cloud/webhook/d5960b8c-7caa-43fb-b4b4-7e4cda6b7595`
- **Target users**: Technicians (John Doe, Sarah Wong, Ahmad Zulkifli, Rajesh Kumar, Chong Wei), Managers, Administrators

---

**Last Updated**: 2026-02-26
**Session**: Planning Phase Complete
