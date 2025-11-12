# DemandScience ICP Creation Claude Skill Specification

## Instructions
Create a Claude Skill that researches and generates enterprise-grade Ideal Customer Profiles (ICPs) for specified technology sales go-to-market (GTM) campaigns using web research to validate required and optional (if present) input components. Your goal is to produce four distinct ICPs that capture firmographic and technographic characteristics of ideal buyers. Each ICP must connect real technologies to business needs / pain points and trigger signals in clear, executive-friendly language.

## Input Specification

### Input Specification Purpose
This specification defines the structured input format for generating Ideal Customer Profiles (ICPs) based on Account-Based Marketing (ABM) campaign requirements from DemandScience customers. The input describes how DemandScience sellers communicate their clients' B2B technology vendor go-to-market strategies and target market characteristics to GTM Fabric. This skill will output the ICPs in json and then will take that JSON and for each ICP will create a pptx slide. The final output will be a pptx presentation 

---

### Business Context: The DemandScience Workflow

**The Players:**
- **DemandScience**: Marketing services provider managing ABM campaigns for technology vendors
- **DemandScience Customer**: The technology vendor (e.g., Kaspersky, Vena Solutions, Autodesk) who needs to market their products
- **GTM Fabric**: Partner organization receiving ICP requests from DemandScience
- **Target Accounts**: The prospective customers that DemandScience's customer wants to reach

**The Flow:**
DemandScience sellers email GTM Fabric with campaign requirements after understanding their customer's needs. This input document captures what DemandScience communicates about:
- Their customer (the technology vendor)
- What their customer is selling (the product/solution)
- Who their customer wants to reach (target accounts/market)
- How their customer wants to reach them (sales strategy, tactics, motion)

---

### Core Input Components

#### 1. Email Context / Campaign Brief (REQUIRED)
**What it contains:**
- **DemandScience Customer Name**: The technology vendor requiring ICPs (e.g., "Kaspersky", "Vena Solutions", "Autodesk")
- **Customer's Offering**: What the DemandScience customer is selling
- **Target Audience**: The prospective or current customers that the DemandScience customer is targeting
- **Target Market/Accounts**: Specific account segments or markets being pursued
- **Campaign Focus & Goals**: Primary objectives of the ABM initiative
- **Sales Strategy Elements**: Sales play, sales motion, sales tactics being employed

**Example:**
```
DemandScience Customer: Kaspersky
Their Offering: Two new product campaigns
Products: K-ASAP (cybersecurity awareness) and XDRO (endpoint protection)
Campaign Goal: "They want to see what audiences and industries we can activate"
Purpose: Defines why the ICPs are being made and what problem or opportunity they serve
```

**Another Example:**
```
DemandScience Customer: Autodesk
Their Offering: Commercial license upgrades
Target Audience: EU companies (<1000 employees) using free versions
Products: AutoCAD, Inventor, Revit
Campaign Goal: Convert free users to paid commercial licenses
Sales Motion: Upsell/expansion play leveraging existing product usage
```

---

#### 2. Solution Focus (REQUIRED)
**What it contains:**
- **Primary Product(s)**: Specific solution(s) the DemandScience customer needs to market
  - Include full product names (e.g., "ServiceNow IT Service Management", "Vena FP&A Platform")
  - Version or tier if relevant (e.g., "Enterprise Edition", "Cloud Version")
- **Product Category**: Solution type (e.g., "Cybersecurity Awareness Platform", "Financial Planning & Analysis Software")
- **Sometimes Paired With Solution Market Context**: References to "competitor solutions","complementary solutions", or "adjacent solutions"

**Purpose**: Sets the anchor for what counts as a fit technology landscape for the ABM campaign

**Example:**
```
Products the DemandScience customer needs to market:
  - K-ASAP (cybersecurity awareness training)
  - XDRO (extended detection and response for endpoints)
```

---

#### 3. Competitive Displacement / Takeout Targets (OPTIONAL)
**What it contains:**
- **Displacement Targets**: List of competitors or legacy vendors to replace
  - Legacy systems (e.g., "Oracle Hyperion", "IBM Cognos")
  - Direct competitors (e.g., "Planful", "OneStream", "Pigment")
- **Specific Product Names**: Competing solutions that the DemandScience customer wants to displace
- **Clarifications**: Sometimes includes specific product versions or categories

**Purpose**: Helps identify Legacy Indicators (Pain Relief opportunities) and modernization triggers for the ABM campaign

**Example:**
```
Competitive Takeout Targets for Vena Solutions:
"Planful, OneStream, Workday, Pigment, IBM, Oracle, SAP"
Context: Legacy financial consolidation and planning platforms
Sales Tactic: Position Vena as modern alternative to these incumbent systems
```

---

#### 4. Targeting Criteria / Filters (REQUIRED)
**What it contains:**
- **Firmographic Filters**: Organizational criteria for target accounts
  - Company size (employee count or revenue range)
  - Geographic region (e.g., "EMEA", "North America", "EU only")
  - Industry verticals (if specified)
- **Market Segment**: Enterprise, Mid-Market, SMB
- **Additional Filters**: 
  - IT spend levels
  - Technographic coverage requirements
  - Signal strength in platforms like HG Insights
- **Special Constraints**: Public sector, private equity-backed, etc.

**Purpose**: Narrows who the ICP applies to and defines the addressable market for the DemandScience customer's ABM campaign

**Example:**
```
Account Targeting Criteria:
Size: Companies under 1000 employees in EMEA
Install Base Filter: Using AutoCAD free licenses
Data Source: HG Insights technographic coverage
Sales Play Focus: License compliance and feature gap selling
```

---

#### 5. Technographic or Intent Data (OPTIONAL)
**What it contains:**
- **Technologies Installed**: Current tech stack indicators
  - Source platform (HG Insights, BuyerCaddy, ZoomInfo)
  - Specific products installed (e.g., "AutoCAD free licenses", "Salesforce Enterprise")
- **Intent Topics**: Research areas being investigated by target accounts
- **Signal Trends**: Rising/falling interest indicators
- **Install Base Signals**: What the prospective accounts currently use

**Purpose**: Enables inclusion of Expansion Signals showing where companies are ready to act in the DemandScience customer's sales cycle

**Example:**
```
Technographic Requirements:
Required Install: AutoCAD, Inventor, OR Revit (free/educational versions)
Data Source: HG Insights product usage data
Intent Signal: Companies researching CAD software alternatives
Signal Type: Non-commercial license usage indicating upgrade potential
Sales Motion: Expansion/upsell leveraging existing product footprint
```

---

#### 6. Target Buyer / Department Info (OPTIONAL)
**What it contains:**
- **Primary Decision Maker**: Title/role who owns budget
  - Examples: "CISO and Security Awareness teams", "IT Ops & Infrastructure", "Finance transformation leaders", "Heads of eCommerce"
- **Influencer Roles**: Supporting stakeholders in the buying process
- **Department/Function**: Organizational unit experiencing the pain
- **Sometimes Implicit**: Derived from product type when not explicitly stated

**Purpose**: Defines who inside the prospective organization feels the pain and owns the budget for the DemandScience customer's solution

**Example:**
```
Target Buyers for the ABM Campaign:
Primary: CFO, VP Finance & Planning
Secondary: FP&A Managers, Finance Transformation Leaders
Department: Office of the CFO
Sales Play: Executive-level business value selling with departmental champions
```

---

#### 7. Geography or Region (OPTIONAL)
**What it contains:**
- **Geographic Scope**: Where the DemandScience customer wants to run their ABM campaign
  - Examples: "EU only", "North America", "Public sector in the UK", "APAC enterprise accounts"
- **Localization Context**: Regional compliance or market requirements

**Purpose**: Filters for localization and compliance contexts relevant to the sales strategy

**Example:**
```
Campaign Geography: EMEA only
Regional Context: EU data privacy requirements, local language support needs
Sales Motion: Region-specific value propositions
```

---

#### 8. Special Instructions / Style Notes (OPTIONAL)
**What it contains:**
- **Formatting Requirements**: How the DemandScience team or customer wants deliverables structured
  - "Use this format", "Include Industries section", "Match previous ICP structure"
- **Exclusions**: "Don't list the client product as an acceleration signal"
- **Reference Examples**: Prior ICPs that worked well
- **Output Use Cases**: GTM decks, one-pagers, sales enablement materials

**Purpose**: Keeps the ICP output on-brand and usable for the DemandScience customer's GTM motions and sales plays

**Example:**
```
Deliverable Requirements:
Format: Use same structure as previous Vena ICPs
Include: Industries section at top of each profile
Exclude: Don't reference client's own product in acceleration indicators
Use Case: Sales one-pagers for field teams and ABM targeting lists
```

---

## Process Steps

Follow these steps in order:

### 0. Research Process (REQUIRED)

**IMPORTANT**: Always conduct research before generating ICPs to ensure accuracy and relevance with up to date market intelligence from the web.

**A. Product Category & Market Research**

Use WebSearch to understand all of the contents of Solution Focus (primary product(s), product category, and solution market context) and current market:
1. Search for: `"[product category] vendors 2025"` or `"[product category] solutions comparison"`
   - Example: "endpoint protection vendors 2025" or "security awareness training solutions comparison"
   - Identify top 5-10 current vendors in the space
   - Note which vendors are growing vs declining

2. Search for: `"[product category] market trends 2025"` or `"[product category] buyer guide"`
   - Understand current buying criteria
   - Identify emerging vs legacy approaches

**B. Competitor Validation & Discovery**

If competitors are mentioned in the brief, validate and expand:

1. Search for: `"[competitor name] customers"` or `"companies using [competitor product]"`
   - Identify actual customer profiles and industries
   - Look for case studies and customer testimonials

2. Search for: `"[competitor product] alternatives"` or `"migrate from [competitor] to"`
   - Find additional competitors not mentioned in brief
   - Understand common migration patterns

3. Search for: `"[competitor product] problems"` or `"[competitor product] limitations"`
   - Identify documented pain points and complaints
   - These become your Legacy Indicators

**C. Industry-Specific Pain Point Research**

For each target industry, research specific pain points:

1. Search for: `"[industry] [product category] challenges 2025"`
   - Example: "healthcare endpoint security challenges 2025"
   - Example: "financial services security awareness training compliance"

2. Search for: `"[industry] [technology stack] modernization"`
   - Example: "banking legacy security infrastructure modernization"
   - Understand what they're moving FROM and TO

3. Search for: `"[industry] compliance requirements [relevant regulations]"`
   - Example: "healthcare HIPAA endpoint security requirements"
   - Example: "financial services NIS2 security awareness"
   - These drive both pain points and urgency

**D. Technology Stack Research**

Research current technology adoption patterns:

1. Search for: `"most used [category] enterprise 2025"` or `"[category] market share"`
   - Example: "most used endpoint protection enterprise 2025"
   - Prioritize real products with significant install base for Legacy Indicators

2. Search for: `"[modern technology] adoption [industry]"`
   - Example: "SIEM adoption financial services"
   - Example: "cloud ERP adoption manufacturing"
   - These become your Acceleration Indicators

**Research Output Summary**

After research, create a brief summary (for your reference, not in final output):
- Top 5-7 validated legacy products/vendors (Displacement / Modernization Signals)
- Top 5-7 validated modern products/vendors (Expansion Signals)
- 3-5 industry-specific pain points discovered
- 2-3 compliance or regulatory drivers
- Key migration patterns observed

**Using Research Findings in ICPs:**
- **Modernization / Displacement Signals**: Use products mentioned in "problems", "limitations", "migrate from" searches
- **Expansion Signals**: Use products mentioned in "adoption", "integrated with", "recently deployed" contexts
- **Pain Points**: Translate research findings into business-first language (avoid quoting analyst jargon)
- **Industries**: Prioritize industries appearing most frequently in competitor customer case studies
- **Buyer Roles**: Use titles found in customer testimonials and case studies

### 1. Extract Offering Definition
- What does the product do?
- What business function does it modernize?
- Based on research, what category does it compete in?

### 2. Infer Industries & Buyer Personas
- Identify 2–3 industries most aligned with the use case
- Cross-reference with research findings on actual customer profiles
- Identify functional buyer groups and decision-makers

### 3. Build Technographic Fit
- **Displacement / Modernization Signals (Pain Relief)**: Use VALIDATED products from research - technologies or architectures that create inefficiency, fragmentation, or cost
- **Expansion Signals**: Use VALIDATED products from research - modern or adjacent tools showing readiness for integration or scaling
- Ensure all vendor/product names are current and accurate based on 2025 market research

### 4. Output Four Distinct ICPs
- Each ICP covers a unique persona, function, or industry segment
- Always include Industries, Departments & Functions, and Technographic Fit sections
- Use only research-validated vendor names and products

## Output Format

Generate exactly 4 ICPs in JSON format optimized for pptx slide creation using this structure for each:

```
## ICP [1-4]: [Descriptive Title]

### Industries
- [Industry 1], [Industry 2], [Industry 3]

### Departments & Business Functions
[Relevant departments]

**Key Job Roles / Job Titles:**
- [Role/Title 1]
- [Role/Title 2]
- [Role/Title 3]

### Technographic Fit

**Displacement / Modernization Signals:**
- [Plain-English business pain explanation] → **[Vendor Product(s)]**
- [Plain-English business pain explanation] → **[Vendor Product(s)]**

**Expansion Signals:**
- [Plain-English readiness signal explanation] → **[Vendor Product(s)]**
- [Plain-English readiness signal explanation] → **[Vendor Product(s)]**
```

## Style & Tone Rules

**CRITICAL REQUIREMENTS:**

1. **Write for executives** — clear, confident, concise
2. **Business reasoning comes before vendor examples** (not just "legacy ERP" alone)
3. **Use specific products and vendors** — never generic terms only
4. **Do not mention Gartner, methodologies, or conceptual terms**
5. **Never list the product being sold as an Acceleration Indicator** unless it's an expansion campaign
6. **Use bold formatting for vendor names and products**
7. **Avoid redundancy** — each ICP should be distinct in scope and buyer type

## Department Reference Guide

Use these when identifying buyer roles:

| Function | Example Roles |
|----------|---------------|
| IT / Security | CIO, CISO, IT Director, Security Engineer |
| Finance | CFO, VP FP&A, Finance Director, Controller |
| Operations | COO, Director of Business Ops, Process Improvement Lead |
| HR / L&D | CHRO, Director of Learning, HRIS Manager |
| Sales / Marketing | CRO, VP Sales Ops, Head of Martech |
| Product / Engineering | CTO, VP Engineering, Product Manager |

## Technology Cluster Examples

Use these vendor/product examples as reference:

**ERP / Finance:**
- SAP ECC, Oracle E-Business Suite, Workday Financials, NetSuite

**Security:**
- Symantec Endpoint Protection, McAfee ePO, Sophos Intercept X, Trend Micro OfficeScan

**Cloud Infrastructure:**
- VMware vSphere, Citrix XenApp, AWS EC2, Azure AD, Google Cloud Platform

**Data / BI:**
- IBM Cognos, Tableau, Power BI, Snowflake, Databricks, BigQuery

**Collaboration:**
- Microsoft 365, Google Workspace, Slack, Zoom, Webex

**DevOps:**
- GitLab, Bitbucket, Jenkins, Jira, GitHub Enterprise

**HR / L&D:**
- SAP SuccessFactors, Cornerstone, BambooHR, Workday HCM

**CRM / Marketing:**
- Salesforce, HubSpot, Marketo, Oracle Eloqua

**ERP Legacy:**
- SAP BPC, IBM Cognos TM1, Oracle Hyperion

## Example Template 1: Cybersecurity – Endpoint Protection

```
## ICP 1: Financial Services Endpoint Protection Modernizer

### Industries
- Banking, Insurance, Fintech

### Departments & Functions
IT Security, Infrastructure, Compliance

**Key Roles:**
- CISO
- Head of Endpoint Security
- Compliance Officer

### Technographic Fit

**Displacement / Modernization Signals:**
- Relying on outdated antivirus agents without behavioral detection → **Symantec Endpoint Protection, McAfee ePO**
- Manual patching and unmanaged device visibility → **Trend Micro OfficeScan, Sophos Enterprise Console**

**Expansion Signals:**
- Recently implemented SIEM or SOAR for centralized visibility → **Splunk Enterprise Security, IBM QRadar**
- Using hybrid device management for remote workforce → **Microsoft Intune, VMware Workspace ONE**
```

## Example Template 2: Finance Automation

```
## ICP 1: Enterprise FP&A Transformation Lead

### Industries
- Manufacturing, Energy, Retail

### Departments & Functions
Finance, FP&A, Accounting

**Key Roles:**
- CFO
- VP FP&A
- Director of Finance Systems

### Technographic Fit

**Displacement / Modernization Signals:**
- Reliance on disconnected spreadsheets and static reporting → **Excel, Google Sheets**
- Using legacy consolidation systems that lack scenario modeling → **IBM Cognos TM1, SAP BPC**

**Expansion Signals:**
- Recently deployed modern cloud ERP → **Workday Financials, Oracle Fusion Cloud ERP**
- Investing in self-service analytics tools → **Power BI, Tableau Online**
```

## Example Template 3: Cloud Modernization

```
## ICP 1: Hybrid Infrastructure Director

### Industries
- Telecom, Financial Services, Manufacturing

### Departments & Functions
Infrastructure, Cloud Ops, IT

**Key Roles:**
- VP Infrastructure
- Head of Cloud Architecture
- IT Director

### Technographic Fit

**Displacement / Modernization Signals**
- Running heavily virtualized data centers with high OpEx → **VMware vSphere, Citrix XenServer**
- Legacy disaster recovery solutions lacking elasticity → **Commvault, Veeam Backup & Replication**

**Expansion Signals:**
- Already integrated identity and governance tools → **Azure AD, AWS IAM**
- Using cloud-based monitoring or automation → **Datadog, Terraform Cloud**
```

## Example Template 4: AI Readiness & Data Modernization

```
## ICP 1: Enterprise Data Transformation Leader

### Industries
- Retail, Logistics, Financial Services

### Departments & Functions
Data Engineering, Analytics, IT Strategy

**Key Roles:**
- Chief Data Officer
- Head of Data Platforms
- AI Program Lead

### Technographic Fit

**Displacement / Modernization Signals:**
- Using on-prem data warehouses that can't scale → **Oracle Exadata, IBM Netezza**
- Limited access to unstructured or real-time data → **SAP BW, Informatica PowerCenter**

**Expansion Signals:**
- Recently adopted cloud data platform → **Snowflake, Databricks, BigQuery**
- Using modern orchestration or catalog tools → **Apache Airflow, Alation, Collibra**
```

## Research Best Practices

**Time Management:**
- Research phase typically takes 3-5 minutes with 8-12 targeted searches
- Prioritize searches based on information gaps in the brief
- If tight on time, focus on: competitor validation + industry pain points + top legacy vendors

**Search Strategy:**
- Use specific product names, not generic terms
- Include "2025" or "2024" in searches for current information
- Look for vendor comparison sites, G2, Gartner peer insights (for data, not to mention in ICPs)
- Check recent industry analyst reports and vendor press releases

**Quality Signals:**
- Prioritize vendor names that appear in multiple search results
- Look for case studies showing actual customer migrations
- Validate company size and industry from customer testimonials
- Check if products are still actively sold (not discontinued or rebranded)

## Evaluation Criteria

Before outputting, verify:

- **Research Completed**: Conducted WebSearch for vendors, competitors, and industry pain points
- **Structure**: 4 ICPs included, formatted correctly
- **Vendor Precision**: Real, current vendors and product names validated through research
- **Business Logic**: Pain = Legacy, Readiness = Acceleration
- **Tone**: Executive, credible, business-first
- **Segmentation**: 4 distinct buyer segments

## Continuous Improvement Tips

- Keep a reference list of verified vendor technologies by category
- Update examples quarterly to match new product names and market shifts
- Recognize pattern clusters (e.g., "spreadsheet pain" → FP&A, "legacy antivirus" → Endpoint Security)
- If input lacks specificity, generate 4 most plausible ICPs for the offering's category

## Usage Examples

User requests that trigger this skill:

- "Create ICPs for our Kaspersky XDRO campaign targeting mid-market financial services"
- "Generate 4 ICPs for a Vena Solutions campaign replacing Oracle EPM Cloud"
- "I need ICPs for a cloud migration campaign targeting VMware customers"
- "Build ICPs for our data modernization offering in retail and logistics"
- "Create buyer profiles for [product] targeting [industry] with [competitor] takeouts"

## Processing Notes for LLM

1. **DemandScience Context**: Remember this input represents a B2B services workflow where DemandScience is delivering ABM campaigns for their customers (technology vendors) to reach target accounts.

2. **Required vs Optional Fields**: Email Context/Campaign Brief, Solution Focus, and Targeting Criteria are minimum required inputs from the DemandScience seller to GTM Fabric.

3. **Sales Strategy Elements**: Pay attention to sales play, sales motion, and sales tactics mentioned—these define whether it's:
   - Competitive displacement (takeout play)
   - Upsell/expansion (land and expand)
   - New market entry (greenfield)
   - Partner channel (ecosystem play)

4. **Implicit Information**: Extract unstated requirements from context (e.g., "cybersecurity product" implies CISO/Security buyer personas; "FP&A software" implies CFO/Finance buyers).

5. **Multi-ICP Scenarios**: When the DemandScience customer needs multiple ICPs, differentiate by:
   - Product line (different solutions)
   - Vertical industry (same solution, different markets)
   - Company size segment (enterprise vs mid-market)
   - Sales motion (new logo vs expansion)

6. **Data Source Awareness**: Note whether the ABM campaign targeting relies on HG Insights, BuyerCaddy, intent data, or install base signals—this affects ICP specificity and activation feasibility.

7. **Campaign Objectives Drive Everything**: The DemandScience customer's campaign focus and goals should guide all ICP development—every indicator should tie back to the sales strategy.
