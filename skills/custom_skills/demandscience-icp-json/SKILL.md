---
name: demandscience-icp-json
description: Generates research-validated ICPs for DemandScience partnership requests. Extracts campaign requirements from email briefs, conducts web research, outputs Markdown for human review, then generates standalone HTML report with embedded branding.
---

# DemandScience ICP Generation Skill

## Overview

This skill automates the creation of research-validated Ideal Customer Profiles (ICPs) for DemandScience partnership requests. It follows a two-stage workflow with human-in-the-loop review:

**Stage 1**: Research → Generate ICPs in Markdown → Request human review
**Stage 2**: Convert approved Markdown → Standalone HTML Report

---

## Input Specification

### Business Context: The DemandScience Workflow

**The Players:**
- **DemandScience**: Marketing services provider managing ABM campaigns for technology vendors
- **DemandScience Customer**: The technology vendor (e.g., Kaspersky, Vena Solutions, Autodesk) who needs to market their products
- **GTM Fabric**: Partner organization receiving ICP requests from DemandScience
- **Target Accounts**: The prospective customers that DemandScience's customer wants to reach

**The Flow:**
DemandScience sellers email GTM Fabric with campaign requirements after understanding their customer's needs. The email brief communicates:
- Their customer (the technology vendor)
- What their customer is selling (the product/solution)
- Who their customer wants to reach (target accounts/market)
- How their customer wants to reach them (sales strategy, tactics, motion)

### Core Input Components

#### 1. Email Context / Campaign Brief (REQUIRED)

**What to extract:**
- **DemandScience Customer Name**: The technology vendor requiring ICPs (e.g., "Kaspersky", "Vena Solutions", "Autodesk")
- **Customer's Offering**: What the DemandScience customer is selling
- **Target Audience**: The prospective customers being targeted
- **Target Market/Accounts**: Specific account segments or markets
- **Campaign Focus & Goals**: Primary objectives of the ABM initiative
- **Sales Strategy Elements**: Sales play, sales motion, sales tactics

**Example:**
```
DemandScience Customer: Kaspersky
Products: K-ASAP (cybersecurity awareness) and XDRO (endpoint protection)
Campaign Goal: "They want to see what audiences and industries we can activate"
```

#### 2. Solution Focus (REQUIRED)

**What to extract:**
- **Primary Product(s)**: Specific solutions being marketed
  - Include full product names (e.g., "ServiceNow IT Service Management", "Vena FP&A Platform")
  - Version or tier if relevant (e.g., "Enterprise Edition", "Cloud Version")
- **Product Category**: Solution type (e.g., "Cybersecurity Awareness Platform", "Financial Planning & Analysis Software")

**Example:**
```
Products: Vena Complete Planning Platform
Category: Financial Planning & Analysis Software
```

#### 3. Competitive Displacement / Takeout Targets (OPTIONAL)

**What to extract:**
- **Displacement Targets**: Competitors or legacy vendors to replace
  - Legacy systems (e.g., "Oracle Hyperion", "IBM Cognos")
  - Direct competitors (e.g., "Planful", "OneStream", "Pigment")
- **Specific Product Names**: Competing solutions to displace

**Purpose**: Helps identify Displacement / Modernization Signals

**Example:**
```
Competitive Targets: Planful, OneStream, Workday, Pigment, IBM, Oracle, SAP
Context: Legacy financial consolidation and planning platforms
```

#### 4. Targeting Criteria / Filters (REQUIRED)

**What to extract:**
- **Firmographic Filters**: Company size, revenue range, geographic region
- **Market Segment**: Enterprise, Mid-Market, SMB
- **Industry Verticals**: If specified
- **Special Constraints**: Public sector, private equity-backed, etc.

**Purpose**: Defines the addressable market for the campaign

**Example:**
```
Size: Mid-market companies
Region: North America
Industries: Technology, Manufacturing, Professional Services
```

#### 5. Technographic or Intent Data (OPTIONAL)

**What to extract:**
- **Technologies Installed**: Current tech stack (e.g., "AutoCAD free licenses", "Salesforce Enterprise")
- **Data Source**: HG Insights, BuyerCaddy, ZoomInfo
- **Intent Signals**: Research areas or rising interest
- **Install Base Signals**: What prospective accounts currently use

**Purpose**: Enables Expansion Signals showing readiness to act

**Example:**
```
Install Base: Companies using AutoCAD, Inventor, OR Revit (free/educational versions)
Data Source: HG Insights
```

#### 6. Target Buyer / Department Info (OPTIONAL)

**What to extract:**
- **Primary Decision Maker**: Title/role who owns budget (e.g., "CISO", "CFO", "VP Finance")
- **Influencer Roles**: Supporting stakeholders
- **Department/Function**: Organizational unit experiencing the pain
- **Sometimes Implicit**: Derived from product type when not explicitly stated

**Purpose**: Defines who feels the pain and owns the budget

**Example:**
```
Primary: CFO, VP Finance & Planning
Secondary: FP&A Managers, Finance Transformation Leaders
Department: Office of the CFO
```

#### 7. Geography or Region (OPTIONAL)

**What to extract:**
- **Geographic Scope**: Where the campaign will run (e.g., "EU only", "North America", "APAC")
- **Localization Context**: Regional compliance or market requirements

**Example:**
```
Geography: EMEA only
Regional Context: EU data privacy requirements
```

#### 8. Special Instructions / Style Notes (OPTIONAL)

**What to extract:**
- **Formatting Requirements**: How deliverables should be structured
- **Exclusions**: Things to avoid (e.g., "Don't list the client product as an acceleration signal")
- **Reference Examples**: Prior ICPs that worked well

**Example:**
```
Format: Use same structure as previous Vena ICPs
Exclude: Don't reference client's own product in acceleration indicators
```

### Parsing Strategy

When you receive a DemandScience email brief:

1. **Identify REQUIRED fields first**: Customer name, products, campaign goal, targeting criteria
2. **Extract OPTIONAL fields**: Competitive targets, technographic data, buyer info, geography, special instructions
3. **Infer missing context**:
   - "Cybersecurity product" implies CISO/Security buyer personas
   - "FP&A software" implies CFO/Finance buyers
   - Product category suggests relevant industries
4. **Note sales motion**:
   - Competitive displacement (takeout play)
   - Upsell/expansion (land and expand)
   - New market entry (greenfield)
   - Partner channel (ecosystem play)

---

## Workflow Stages

### STAGE 1: ICP Research & Markdown Generation

#### Step 0: Research Process (REQUIRED)

**IMPORTANT**: Always conduct web research before generating ICPs to ensure accuracy with current market intelligence.

**A. Product Category & Market Research**

1. Search for: `"[product category] vendors 2025"` or `"[product category] solutions comparison"`
   - Example: "endpoint protection vendors 2025"
   - Identify top 5-10 current vendors in the space
   - Note which vendors are growing vs declining

2. Search for: `"[product category] market trends 2025"` or `"[product category] buyer guide"`
   - Understand current buying criteria
   - Identify emerging vs legacy approaches

**B. Competitor Validation & Discovery**

1. Search for: `"[competitor name] customers"` or `"companies using [competitor product]"`
   - Identify actual customer profiles and industries
   - Look for case studies and customer testimonials

2. Search for: `"[competitor product] alternatives"` or `"migrate from [competitor] to"`
   - Find additional competitors not mentioned in brief
   - Understand common migration patterns

3. Search for: `"[competitor product] problems"` or `"[competitor product] limitations"`
   - Identify documented pain points
   - These become your Displacement / Modernization Signals

**C. Industry-Specific Pain Point Research**

1. Search for: `"[industry] [product category] challenges 2025"`
   - Example: "healthcare endpoint security challenges 2025"

2. Search for: `"[industry] [technology stack] modernization"`
   - Example: "banking legacy security infrastructure modernization"
   - Understand what they're moving FROM and TO

3. Search for: `"[industry] compliance requirements [relevant regulations]"`
   - Example: "healthcare HIPAA endpoint security requirements"
   - These drive both pain points and urgency

**D. Technology Stack Research**

1. Search for: `"most used [category] enterprise 2025"` or `"[category] market share"`
   - Prioritize real products with significant install base

2. Search for: `"[modern technology] adoption [industry]"`
   - Example: "cloud ERP adoption manufacturing"
   - These become your Expansion Signals

#### Step 1: Extract Campaign Requirements

From the DemandScience email brief, identify:
- **DemandScience Customer**: The technology vendor (e.g., "Kaspersky", "Vena Solutions")
- **Products**: Specific solutions being marketed
- **Target Industries**: Industries to focus on (if specified)
- **Target Region**: Geographic scope
- **Campaign Goal**: Primary objectives
- **Competitive Targets**: Competitors to displace (if mentioned)

#### Step 2: Generate At Least 3 Distinct ICPs

Each ICP must include:

**Required Sections:**
1. **Title**: `[Segment] - [Primary Use Case/Pain Point]`
2. **Industries**: 2-4 industries (maximum 4)
3. **Departments & Business Functions**: 2-3 departments (maximum 3)
4. **Key Job Roles / Job Titles**: 2-3 roles (maximum 3)
5. **Technographic Fit**:
   - **Displacement / Modernization Signals** (2-4 signals)
   - **Expansion Signals** (2-4 signals)

**Signal Format:**
```
Displacement / Modernization Signals:
- [Business pain description] → **[Validated Vendor Product]**

Expansion Signals:
- [Readiness indicator description] → **[Validated Vendor Product]**
```

#### Step 3: Output Markdown for Human Review

Generate ICPs in this exact Markdown format:

```markdown
# Research-Validated ICPs for [DemandScience Customer]

## ICP 1: [Descriptive Title]

### Industries
- [Industry 1], [Industry 2], [Industry 3], [Industry 4]

### Departments & Business Functions
- [Department 1]
- [Department 2]
- [Department 3]

**Key Job Roles / Job Titles:**
- [Role 1]
- [Role 2]
- [Role 3]

### Technographic Fit

**Displacement / Modernization Signals:**
- [Pain description] → **[Vendor Product]**
- [Pain description] → **[Vendor Product]**
- [Pain description] → **[Vendor Product]**
- [Pain description] → **[Vendor Product]**

**Expansion Signals:**
- [Readiness indicator] → **[Vendor Product]**
- [Readiness indicator] → **[Vendor Product]**
- [Readiness indicator] → **[Vendor Product]**
- [Readiness indicator] → **[Vendor Product]**

---

## ICP 2: [Descriptive Title]
[Same structure as ICP 1]

---

## ICP 3: [Descriptive Title]
[Same structure as ICP 1]

---
```

#### Step 4: Request Human Review

After outputting Markdown, say exactly:

"Please review these ICPs. You can:
- Edit any content directly in the Markdown
- Refine vendor names, pain points, or buyer personas
- Adjust industry focus or technographic signals
- Approve them as-is for JSON conversion

Once you've reviewed and are ready to proceed, let me know and I'll convert them to structured JSON."

**DO NOT PROCEED to Stage 2** until user explicitly approves.

---

### STAGE 2: STANDALONE HTML REPORT GENERATION

**Prerequisites:**
- User has reviewed and approved Markdown ICPs from Stage 1
- User has explicitly said to proceed (e.g., "looks good", "approved", "generate HTML", "create report")

**Objective**: Generate a complete, self-contained HTML file that users can download and open in any browser without needing a server.

#### HTML Generation Process

**Step 1: Parse Markdown to JSON (Internal)**

First, convert the approved Markdown ICPs to JSON structure for embedding:

```json
{
  "campaign_metadata": {
    "demandscience_customer": "Snowflake",
    "products": ["Snowflake Data Cloud", "Snowpark"],
    "campaign_goal": "...",
    "target_region": "North America",
    "generated_date": "2025-11-13",
    "total_icps": 3
  },
  "icps": [...]
}
```

**Step 2: Load Template Resources**

Use Python's `code_execution` tool to load the required template files from the `resources/` directory:

```python
from pathlib import Path
import json

# Load resources
resources_dir = Path('resources')

# Read CSS
with open(resources_dir / 'embedded-css.css', 'r') as f:
    css_content = f.read()

# Read embedded assets (logos, icons as base64)
with open(resources_dir / 'embedded_assets.js', 'r') as f:
    assets_js = f.read()

# Read renderer JavaScript
with open(resources_dir / 'icp-renderer.js', 'r') as f:
    renderer_js = f.read()

# Adapt renderer to use embedded data instead of fetch()
renderer_js = renderer_js.replace(
    'constructor(jsonPath = \'/data/icps.json\')',
    'constructor(data)'
).replace(
    'this.jsonPath = jsonPath;',
    '// Data passed directly'
).replace(
    'src="assets/icons/gtmfabric_darkpurple_icon.png"',
    'src="${EMBEDDED_ASSETS.icons.gtmfabric_darkpurple}"'
).replace(
    'src="assets/icons/industries_icon.png"',
    'src="${EMBEDDED_ASSETS.icons.industries}"'
).replace(
    'src="assets/icons/departmentsfunctions_icon.png"',
    'src="${EMBEDDED_ASSETS.icons.departmentsfunctions}"'
).replace(
    'src="assets/icons/keyroles_icon.png"',
    'src="${EMBEDDED_ASSETS.icons.keyroles}"'
).replace(
    'src="assets/icons/technographicFit_icon.png"',
    'src="${EMBEDDED_ASSETS.icons.technographicFit}"'
)

# Replace fetch logic
renderer_js = renderer_js.replace(
    '''async loadJSON() {
        try {
            const response = await fetch(this.jsonPath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            this.data = await response.json();
            this.validateData();
        } catch (error) {
            throw new Error(`Failed to load ICP data: ${error.message}`);
        }
    }''',
    '''async loadJSON() {
        // Data already embedded
        this.validateData();
    }'''
)
```

**Step 3: Generate Complete HTML**

Create the standalone HTML file with all components embedded:

```python
customer_name = icp_data['campaign_metadata']['demandscience_customer']

html_output = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ICP Sales Report - {customer_name}</title>
    <style>
{css_content}
    </style>
</head>
<body>
    <!-- Sidebar -->
    <div class="sidebar">
        <div class="sidebar-content">
            <div class="sidebar-top-section">
                <img id="demandscience-logo" alt="Demand Science">
            </div>
            <div class="sidebar-customer-section">
                <div class="sidebar-customer-info">
                    <div class="sidebar-customer-name"></div>
                    <div class="sidebar-customer-label">Campaign Report</div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-header">
                    <div class="sidebar-section-title">Campaign Objective</div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-value"></div>
                </div>
            </div>
            <div class="sidebar-section">
                <div class="sidebar-section-header">
                    <div class="sidebar-section-title">Campaign Details</div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Products</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Target Region</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Generated</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Total ICPs</div>
                    <div class="sidebar-detail-value"></div>
                </div>
            </div>
            <div class="sidebar-bottom-section">
                <img id="gtmfabric-footer" alt="GTM Fabric" class="sidebar-bottom-logo">
            </div>
        </div>
    </div>

    <div class="main-content-wrapper">
        <div class="container">
            <!-- Propensity Funnel -->
            <div class="card" style="margin-bottom: 48px;">
                <div class="icp-header">
                    <div class="icp-icon"><img id="funnel-icon" alt="Funnel Icon"></div>
                    <h2>Propensity Funnel</h2>
                </div>
                <div class="funnel-grid">
                    <div>
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Market to Account View</h3>
                            <ul class="funnel-level-list">
                                <li>Define the ideal client profile</li>
                                <li>What does an ideal customer look like?</li>
                                <li>Who's in the right buying group?</li>
                            </ul>
                        </div>
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Research & Intent</h3>
                            <ul class="funnel-level-list">
                                <li>Propensity to buy (Buyer Intent)</li>
                                <li>Research shows interest</li>
                                <li>Who's researching now?</li>
                            </ul>
                        </div>
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Engagement & Outreach</h3>
                            <ul class="funnel-level-list">
                                <li>SDR contact & qualification</li>
                                <li>AE demos & sales</li>
                                <li>Who's ready to talk?</li>
                            </ul>
                        </div>
                    </div>
                    <div class="funnel-visual">
                        <div class="funnel-stage" style="width: 100%; border: 3px solid #9333ea;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(147, 51, 234, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Propensity Fit</h4>
                                <p class="funnel-stage-label">Ideal Customer Profile</p>
                            </div>
                        </div>
                        <div class="funnel-arrow">
                            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="funnel-stage" style="width: 85%; border: 3px solid #a855f7;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1) 0%, rgba(192, 132, 252, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Research & Intent</h4>
                                <p class="funnel-stage-label">Active Buyers</p>
                            </div>
                        </div>
                        <div class="funnel-arrow">
                            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>
                        <div class="funnel-stage" style="width: 65%; border: 3px solid #c084fc;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(192, 132, 252, 0.1) 0%, rgba(216, 180, 254, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Engagement</h4>
                                <p class="funnel-stage-label">Sales Qualified</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ICP Cards will be inserted here by JavaScript -->
            <div id="icp-container"></div>
        </div>
    </div>

    <script>
{assets_js}

// Embedded ICP Data
const ICP_DATA = {json.dumps(icp_data, indent=2)};

{renderer_js}

// Initialize embedded assets
function loadEmbeddedAssets() {{
    document.getElementById('demandscience-logo').src = EMBEDDED_ASSETS.logos.demandscience;
    document.getElementById('gtmfabric-footer').src = EMBEDDED_ASSETS.images.sidebar_footer;
    document.getElementById('funnel-icon').src = EMBEDDED_ASSETS.icons.gtmfabric_darkpurple;
}}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {{
    loadEmbeddedAssets();
    const renderer = new ICPRenderer(ICP_DATA);
    renderer.init();
}});
    </script>
</body>
</html>'''
```

**Step 4: Output HTML to User**

Display the complete HTML in a code block with download instructions:

````markdown
## ✅ Your Standalone HTML Report is Ready!

Download and open this file in any web browser (Chrome, Firefox, Safari, Edge).

**Filename**: `icp-report-{customer_name}-{date}.html`

**Instructions**:
1. Copy the entire HTML code below
2. Save to a file with `.html` extension (e.g., `icp-report-snowflake-2025-11-13.html`)
3. Double-click the file to open in your browser
4. Share with DemandScience or internal stakeholders

The report works completely offline and requires no server or dependencies.

**File Size**: ~485 KB

```html
{html_output}
```

**Features**:
✅ Works offline (no internet needed after download)
✅ All branding included (GTM Fabric + DemandScience logos)
✅ Responsive design (works on mobile and desktop)
✅ Professional formatting with Propensity Funnel
✅ Dynamic ICP cards with all researched data
✅ Ready to share via email or cloud storage
````

---

## Style & Tone Rules

**CRITICAL REQUIREMENTS:**

1. **Write for executives** — clear, confident, concise
2. **Business reasoning comes before vendor examples** (not just "legacy ERP" alone)
3. **Use specific products and vendors** — never generic terms only
4. **Do not mention Gartner, methodologies, or conceptual terms**
5. **Never list the product being sold as an Expansion Signal** unless it's an expansion campaign
6. **Use bold formatting for vendor names and products** in Markdown
7. **Avoid redundancy** — each ICP should be distinct in scope and buyer type

## Quality Validation

### Stage 1: Markdown ICPs

Before outputting, verify:
- ✓ **Research Completed**: Conducted WebSearch for vendors, competitors, pain points
- ✓ **Structure**: At least 3 ICPs, formatted correctly in Markdown
- ✓ **Vendor Precision**: Real, current vendors and product names validated through research
- ✓ **Business Logic**: Pain = Displacement, Readiness = Expansion
- ✓ **Tone**: Executive, credible, business-first
- ✓ **Segmentation**: At least 3 distinct buyer segments
- ✓ **Capacity Limits**: Max 4 industries, 3 departments, 3 roles per ICP
- ✓ **Review Prompt**: Explicitly requests user review before Stage 2

### Stage 2: HTML Output

Before outputting, verify:
- ✓ **Valid HTML**: Output is well-formed, complete HTML document
- ✓ **All Resources Loaded**: CSS, JavaScript, and assets embedded successfully
- ✓ **Data Embedded**: ICP JSON data properly embedded in script tag
- ✓ **File Size**: Total HTML file size < 600 KB
- ✓ **Complete Structure**: Sidebar, Propensity Funnel, and ICP cards included
- ✓ **Assets Embedded**: All logos and icons as base64 data URIs
- ✓ **JavaScript Functional**: Renderer code properly adapted for embedded data
- ✓ **Vendor Preservation**: All vendor/product names maintained exactly

## Example Workflow

**User Input:**
```
From: DemandScience Partner
Subject: Campaign Request - Vena Solutions

We need ICPs for Vena Solutions targeting finance teams.
Products: Vena Complete Planning Platform
Target Industries: Technology, Manufacturing
Use Case: Replacing legacy Excel-based planning and Oracle/SAP EPM
Region: North America
```

**Stage 1 Process:**
1. ✓ Conduct web research:
   - "financial planning software vendors 2025"
   - "Oracle EPM alternatives"
   - "Excel-based planning problems"
   - "SAP BPC limitations"
2. ✓ Generate 3 distinct ICPs with validated vendor names
3. ✓ Output in Markdown format
4. ✓ Request user review

**User Approval**: "Looks good, please generate the HTML report"

**Stage 2 Process:**
1. ✓ Parse Markdown ICPs into JSON structure
2. ✓ Load resources: CSS, assets, renderer JavaScript
3. ✓ Generate complete standalone HTML file
4. ✓ Output HTML with download instructions

**Final Output**: Complete standalone HTML file (~485 KB) ready to download and open in any browser

## Error Handling

### If Web Research Fails
- Retry search with alternative query
- Try different search terms or date ranges
- If still failing: Inform user and request manual input
- **NEVER generate fictional vendor names**

### If User Hasn't Approved Markdown
- Do not proceed to Stage 2
- Explicitly wait for user confirmation
- Say: "I'm waiting for your approval to proceed with HTML generation. Please review the ICPs and let me know if any changes are needed."

### If HTML Generation Fails
- Check that all resource files are accessible in `resources/` directory
- Verify JSON data structure is correct
- Ensure proper string escaping in Python template
- Provide error details to user with specific failure point

## Performance Expectations

- **Stage 1** (Research & Markdown): 2-3 minutes
- **Stage 2** (HTML Generation): 30-60 seconds
- **Total Workflow**: Under 5 minutes ✅
- **Output File Size**: ~485 KB (HTML with embedded assets)

## Technology Cluster Reference

Use these validated vendor/product examples:

**ERP / Finance:**
SAP ECC, Oracle E-Business Suite, Workday Financials, NetSuite

**Security:**
Symantec Endpoint Protection, McAfee ePO, Sophos Intercept X, Trend Micro OfficeScan

**Cloud Infrastructure:**
VMware vSphere, Citrix XenApp, AWS EC2, Azure AD, Google Cloud Platform

**Data / BI:**
IBM Cognos, Tableau, Power BI, Snowflake, Databricks, BigQuery

**Collaboration:**
Microsoft 365, Google Workspace, Slack, Zoom, Webex

**DevOps:**
GitLab, Bitbucket, Jenkins, Jira, GitHub Enterprise

**HR / L&D:**
SAP SuccessFactors, Cornerstone, BambooHR, Workday HCM

**CRM / Marketing:**
Salesforce, HubSpot, Marketo, Oracle Eloqua

**Legacy EPM:**
SAP BPC, IBM Cognos TM1, Oracle Hyperion, Prophix, Anaplan, Planful

## Department Reference

| Function | Example Roles |
|----------|---------------|
| IT / Security | CIO, CISO, IT Director, Security Engineer |
| Finance | CFO, VP FP&A, Finance Director, Controller |
| Operations | COO, Director of Business Ops, Process Improvement Lead |
| HR / L&D | CHRO, Director of Learning, HRIS Manager |
| Sales / Marketing | CRO, VP Sales Ops, Head of Martech |
| Product / Engineering | CTO, VP Engineering, Product Manager |
