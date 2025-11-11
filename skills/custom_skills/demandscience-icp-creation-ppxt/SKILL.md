---
name: demandscience-icp-creation-ppxt
description: Research and generate 4 enterprise-grade Ideal Customer Profiles (ICPs) for technology sales GTM campaigns using web research and GTM Fabric ontologies, then create a professional PowerPoint presentation
version: 1.0.0
---

# DemandScience ICP Creation Skill

## Overview

This skill researches and generates 4 enterprise-grade Ideal Customer Profiles (ICPs) for technology sales go-to-market (GTM) campaigns. It produces ICPs that capture firmographic and technographic characteristics of ideal buyers, connecting real technologies to business needs, pain points, and trigger signals in clear, executive-friendly language.

**Key Capabilities:**
1. Uses **GTM Fabric Ontologies MCP server** to access formal ICP structures and technographic frameworks
2. Conducts **web research** to validate vendors, competitors, and market intelligence
3. Generates **structured JSON** output with 4 distinct ICPs
4. Creates a **professional PowerPoint presentation** with one slide per ICP using the applying-brand-guidelines-gtmfabric skill

## When to Use This Skill

Invoke this skill when users request:
- "Create ICPs for [product] targeting [industry/segment]"
- "Generate buyer profiles for [campaign]"
- "Build 4 ICPs for [solution] with [competitor] takeouts"
- "I need ICPs for a [technology] campaign"
- Any request involving ICP creation, buyer profiles, or ABM campaign targeting

## Required Capabilities

This skill requires access to:
1. **GTM Fabric Ontologies MCP Server** (`gtm-fabric-ontologies`) - For formal ICP framework and ontological context
2. **Web Search Tools** (`WebSearch`, `WebFetch`) - For market research and vendor validation
3. **PPTX Skill** - For PowerPoint presentation generation
4. **File System Access** - For saving output files

If any of these are unavailable, notify the user and proceed with limitations.

## Business Context

**The DemandScience Workflow:**
- **DemandScience**: Marketing services provider managing ABM campaigns for technology vendors
- **DemandScience Customer**: Technology vendor (e.g., Kaspersky, Vena Solutions, Autodesk) needing to market products
- **GTM Fabric**: Partner organization receiving ICP requests from DemandScience
- **Target Accounts**: Prospective customers that DemandScience's customer wants to reach

DemandScience sellers communicate campaign requirements to GTM Fabric. This skill processes those requirements into actionable ICPs with a professional PowerPoint deliverable.

## Input Specification

### Required Input Components

#### 1. Email Context / Campaign Brief (REQUIRED)
Contains:
- **DemandScience Customer Name**: The technology vendor requiring ICPs
- **Customer's Offering**: What the vendor is selling
- **Target Audience**: Prospective customers being targeted
- **Campaign Focus & Goals**: Primary ABM objectives
- **Sales Strategy Elements**: Sales play, motion, tactics

Example:
```
DemandScience Customer: Kaspersky
Offering: Two new product campaigns - K-ASAP (cybersecurity awareness) and XDRO (endpoint protection)
Campaign Goal: "They want to see what audiences and industries we can activate"
```

#### 2. Solution Focus (REQUIRED)
Contains:
- **Primary Product(s)**: Specific solutions to market (full names, versions)
- **Product Category**: Solution type (e.g., "Endpoint Security", "FP&A Software")
- **Solution Market Context**: References to competitors, complementary solutions, adjacent solutions

#### 3. Targeting Criteria / Filters (REQUIRED)
Contains:
- **Firmographic Filters**: Company size, geography, industry, revenue
- **Market Segment**: Enterprise, Mid-Market, SMB
- **Special Constraints**: Public sector, PE-backed, etc.

### Optional Input Components

#### 4. Competitive Displacement / Takeout Targets (OPTIONAL)
Contains:
- **Displacement Targets**: Competitors or legacy vendors to replace
- **Specific Products**: Competing solutions to displace
- Used to identify Legacy Indicators (pain relief opportunities)

Example:
```
Competitive Takeout Targets: Planful, OneStream, Workday, Pigment, IBM, Oracle, SAP
Context: Legacy financial consolidation and planning platforms
```

#### 5. Technographic or Intent Data (OPTIONAL)
Contains:
- **Technologies Installed**: Current tech stack (from HG Insights, BuyerCaddy, ZoomInfo)
- **Intent Topics**: Research areas by target accounts
- **Signal Trends**: Rising/falling interest indicators
- Used for Expansion Signals (buying readiness)

#### 6. Target Buyer / Department Info (OPTIONAL)
Contains:
- **Primary Decision Maker**: Title/role with budget authority
- **Influencer Roles**: Supporting stakeholders
- **Department/Function**: Organizational unit with pain

#### 7. Geography or Region (OPTIONAL)
Contains:
- **Geographic Scope**: Where to run ABM campaign
- **Localization Context**: Regional compliance/market requirements

#### 8. Special Instructions / Style Notes (OPTIONAL)
Contains:
- **Formatting Requirements**: How deliverables should be structured
- **Exclusions**: What not to include
- **Reference Examples**: Prior successful ICPs

## Process

Execute these steps in order:

### Step -1: Load GTM Fabric Ontology Context

**CRITICAL**: Before any research or ICP generation, load ontological context from GTM Fabric.

Use the `gtm-fabric-ontologies` MCP server:

1. **Get ontology statistics**:
   ```
   Tool: mcp__gtm-fabric-ontologies__get_ontology_stats
   Purpose: Understand available ontologies and their scope
   ```

2. **Extract ICP targeting ontology**:
   ```
   Tool: mcp__gtm-fabric-ontologies__extract_ontology_classes
   Parameter: ontology_uri = "ontology://domain/gtm-targeting-icp"
   Purpose: Load formal ICP structure, technographic concepts, buyer persona framework
   ```

3. **Search for relevant ontology concepts**:
   ```
   Tool: mcp__gtm-fabric-ontologies__search_ontologies
   Parameters: Use keywords from campaign brief (e.g., "displacement", "technographic", industry terms)
   Purpose: Find ontological patterns relevant to the specific campaign
   ```

**What to Extract from Ontologies:**
- `gtm:IdealCustomerProfile` - Root structure for outputs
- `gtm:BuyerPersona` - Framework for key roles/titles
- `gtm:CompetitiveTechnologyStack` - Structure for displacement signals
- `gtm:ComplementaryTechnologyStack` - Structure for expansion signals
- `gtm:FirmographicQuality` - Industry and company size criteria
- `gtm:TechnographicQuality` - Tech stack assessment framework

**Use ontology context to:**
- Validate that your ICP structure aligns with GTM Fabric standards
- Identify additional dimensions to include (e.g., CloudMaturity, ITSpendingLevel)
- Ensure technographic signals are categorized correctly
- Ground your research in the formal framework

### Step 0: Research Process (REQUIRED)

**IMPORTANT**: Always conduct web research before generating ICPs to ensure accuracy and current market intelligence.

#### A. Product Category & Market Research

Use `WebSearch` to understand Solution Focus components:

1. **Market landscape**: Search `"[product category] vendors 2025"` or `"[product category] solutions comparison"`
   - Identify top 5-10 current vendors
   - Note which vendors are growing vs declining

2. **Trends and criteria**: Search `"[product category] market trends 2025"` or `"[product category] buyer guide"`
   - Understand current buying criteria
   - Identify emerging vs legacy approaches

#### B. Competitor Validation & Discovery

If competitors mentioned, validate and expand:

1. **Customer profiles**: Search `"[competitor name] customers"` or `"companies using [competitor product]"`
   - Identify actual customer profiles and industries
   - Look for case studies and testimonials

2. **Alternatives and migrations**: Search `"[competitor product] alternatives"` or `"migrate from [competitor] to"`
   - Find additional competitors not mentioned
   - Understand common migration patterns

3. **Pain points**: Search `"[competitor product] problems"` or `"[competitor product] limitations"`
   - Identify documented pain points and complaints
   - These become Legacy Indicators

#### C. Industry-Specific Pain Point Research

For each target industry:

1. **Industry challenges**: Search `"[industry] [product category] challenges 2025"`
   - Example: "healthcare endpoint security challenges 2025"

2. **Modernization patterns**: Search `"[industry] [technology stack] modernization"`
   - Example: "banking legacy security infrastructure modernization"
   - Understand what they're moving FROM and TO

3. **Compliance drivers**: Search `"[industry] compliance requirements [relevant regulations]"`
   - Example: "healthcare HIPAA endpoint security requirements"
   - These drive pain points and urgency

#### D. Technology Stack Research

Research current technology adoption:

1. **Market leaders**: Search `"most used [category] enterprise 2025"` or `"[category] market share"`
   - Prioritize real products with significant install base for Legacy Indicators

2. **Modern adoption**: Search `"[modern technology] adoption [industry]"`
   - Example: "SIEM adoption financial services"
   - These become Acceleration Indicators

#### Research Output Summary

Create a brief summary (for reference):
- Top 5-7 validated legacy products/vendors (Displacement Signals)
- Top 5-7 validated modern products/vendors (Expansion Signals)
- 3-5 industry-specific pain points discovered
- 2-3 compliance or regulatory drivers
- Key migration patterns observed

**Using Research in ICPs:**
- **Legacy Indicators**: Use products from "problems", "limitations", "migrate from" searches
- **Acceleration Indicators**: Use products from "adoption", "integrated with", "recently deployed" contexts
- **Pain Points**: Translate into business-first language (no analyst jargon)
- **Industries**: Prioritize industries from competitor case studies
- **Buyer Roles**: Use titles from customer testimonials

### Step 1: Extract Offering Definition

Analyze the DemandScience customer's product:
- What does the product do?
- What business function does it modernize?
- Based on research, what category does it compete in?

### Step 2: Infer Industries & Buyer Personas

Identify target markets:
- Identify 2-3 industries most aligned with use case
- Cross-reference with research on actual customer profiles
- Identify functional buyer groups and decision-makers

### Step 3: Build Technographic Fit

Create signal inventory:
- **Displacement / Modernization Signals (Pain Relief)**: VALIDATED products from research - technologies creating inefficiency, fragmentation, or cost
- **Expansion Signals**: VALIDATED products from research - modern/adjacent tools showing readiness for integration or scaling
- Ensure all vendor/product names are current and accurate (2025 market research)

### Step 4: Generate JSON Output

Create structured JSON with exactly 4 distinct ICPs following this format:

```json
{
  "campaign_info": {
    "customer_name": "DemandScience Customer Name",
    "solution_name": "Product/Solution Name",
    "campaign_date": "2025-11-10"
  },
  "icps": [
    {
      "icp_number": 1,
      "title": "Descriptive Title",
      "industries": ["Industry 1", "Industry 2", "Industry 3"],
      "departments_and_functions": "Relevant departments",
      "key_roles": [
        "Role/Title 1",
        "Role/Title 2",
        "Role/Title 3"
      ],
      "technographic_fit": {
        "displacement_signals": [
          {
            "pain_explanation": "Plain-English business pain explanation",
            "vendor_products": ["Vendor Product 1", "Vendor Product 2"]
          }
        ],
        "expansion_signals": [
          {
            "readiness_explanation": "Plain-English readiness signal explanation",
            "vendor_products": ["Vendor Product 4", "Vendor Product 5"]
          }
        ]
      }
    }
  ]
}
```

### Step 5: Create PowerPoint Presentation (REQUIRED)

**CRITICAL**: After generating JSON, ALWAYS create a PowerPoint presentation.

**Presentation Structure:**

1. **Title Slide**:
   - Title: "[DemandScience Customer Name] - Ideal Customer Profiles"
   - Subtitle: "[Product/Solution Name] GTM Campaign"
   - Date: Current date

2. **ICP Slides** (one per ICP - 4 total):
   - **Slide Title**: ICP [Number]: [Descriptive Title]
   - **Content Sections**:
     - **Industries**: Bullet list of target industries
     - **Departments & Business Functions**: Text description + bullet list of key roles
     - **Technographic Fit** with two subsections:
       - **Displacement / Modernization Signals**: 2-3 bullets, pain ’ vendor products in bold
       - **Expansion Signals**: 2-3 bullets, readiness ’ vendor products in bold

3. **Summary Slide** (optional for complex campaigns):
   - Key takeaways across all 4 ICPs
   - Common themes
   - Market sizing notes

**Formatting Requirements:**
- Use the **applying-brand-guidelines-gtmfabric** skill to apply GTM Fabric design system
- Bold all vendor/product names
- Use bullet points for clarity
- Keep text concise (executive-ready)
- Ensure consistent formatting across all ICP slides

**Deliverable:**
- Generate presentation file
- Provide download link to user

## Output Format

### JSON Structure

```json
{
  "campaign_info": {
    "customer_name": "string",
    "solution_name": "string",
    "campaign_date": "YYYY-MM-DD"
  },
  "icps": [
    {
      "icp_number": 1,
      "title": "string",
      "industries": ["string"],
      "departments_and_functions": "string",
      "key_roles": ["string"],
      "technographic_fit": {
        "displacement_signals": [
          {
            "pain_explanation": "string",
            "vendor_products": ["string"]
          }
        ],
        "expansion_signals": [
          {
            "readiness_explanation": "string",
            "vendor_products": ["string"]
          }
        ]
      }
    }
  ]
}
```

### PowerPoint Slide Format

Each ICP slide should follow this structure:

```
ICP [Number]: [Descriptive Title]

Industries
" [Industry 1], [Industry 2], [Industry 3]

Departments & Business Functions
[Departments text description]

Key Job Roles / Job Titles:
" [Role 1]
" [Role 2]
" [Role 3]

Technographic Fit

Displacement / Modernization Signals:
" [Business pain explanation] ’ [Vendor Product 1], [Vendor Product 2]
" [Business pain explanation] ’ [Vendor Product 3]

Expansion Signals:
" [Readiness signal explanation] ’ [Vendor Product 4], [Vendor Product 5]
" [Readiness signal explanation] ’ [Vendor Product 6]
```

## Style & Tone Rules

**CRITICAL REQUIREMENTS:**

1. **Write for executives** - clear, confident, concise
2. **Business reasoning before vendor examples** (not just "legacy ERP" alone)
3. **Use specific products and vendors** - never generic terms only
4. **Do not mention Gartner, methodologies, or conceptual terms**
5. **Never list the product being sold as an Acceleration Indicator** (unless expansion campaign)
6. **Use bold formatting for vendor names and products**
7. **Avoid redundancy** - each ICP must be distinct

## Department Reference Guide

| Function | Example Roles |
|----------|---------------|
| IT / Security | CIO, CISO, IT Director, Security Engineer |
| Finance | CFO, VP FP&A, Finance Director, Controller |
| Operations | COO, Director of Business Ops, Process Improvement Lead |
| HR / L&D | CHRO, Director of Learning, HRIS Manager |
| Sales / Marketing | CRO, VP Sales Ops, Head of Martech |
| Product / Engineering | CTO, VP Engineering, Product Manager |

## Technology Cluster Examples

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

**ERP Legacy:**
SAP BPC, IBM Cognos TM1, Oracle Hyperion

## Example ICP Templates

### Example 1: Cybersecurity - Endpoint Protection

```
ICP 1: Financial Services Endpoint Protection Modernizer

Industries
" Banking, Insurance, Fintech

Departments & Business Functions
IT Security, Infrastructure, Compliance

Key Roles:
" CISO
" Head of Endpoint Security
" Compliance Officer

Technographic Fit

Displacement / Modernization Signals:
" Relying on outdated antivirus agents without behavioral detection ’ Symantec Endpoint Protection, McAfee ePO
" Manual patching and unmanaged device visibility ’ Trend Micro OfficeScan, Sophos Enterprise Console

Expansion Signals:
" Recently implemented SIEM or SOAR for centralized visibility ’ Splunk Enterprise Security, IBM QRadar
" Using hybrid device management for remote workforce ’ Microsoft Intune, VMware Workspace ONE
```

### Example 2: Finance Automation

```
ICP 1: Enterprise FP&A Transformation Lead

Industries
" Manufacturing, Energy, Retail

Departments & Business Functions
Finance, FP&A, Accounting

Key Roles:
" CFO
" VP FP&A
" Director of Finance Systems

Technographic Fit

Displacement / Modernization Signals:
" Reliance on disconnected spreadsheets and static reporting ’ Excel, Google Sheets
" Using legacy consolidation systems that lack scenario modeling ’ IBM Cognos TM1, SAP BPC

Expansion Signals:
" Recently deployed modern cloud ERP ’ Workday Financials, Oracle Fusion Cloud ERP
" Investing in self-service analytics tools ’ Power BI, Tableau Online
```

### Example 3: Cloud Modernization

```
ICP 1: Hybrid Infrastructure Director

Industries
" Telecom, Financial Services, Manufacturing

Departments & Business Functions
Infrastructure, Cloud Ops, IT

Key Roles:
" VP Infrastructure
" Head of Cloud Architecture
" IT Director

Technographic Fit

Displacement / Modernization Signals:
" Running heavily virtualized data centers with high OpEx ’ VMware vSphere, Citrix XenServer
" Legacy disaster recovery solutions lacking elasticity ’ Commvault, Veeam Backup & Replication

Expansion Signals:
" Already integrated identity and governance tools ’ Azure AD, AWS IAM
" Using cloud-based monitoring or automation ’ Datadog, Terraform Cloud
```

### Example 4: AI Readiness & Data Modernization

```
ICP 1: Enterprise Data Transformation Leader

Industries
" Retail, Logistics, Financial Services

Departments & Business Functions
Data Engineering, Analytics, IT Strategy

Key Roles:
" Chief Data Officer
" Head of Data Platforms
" AI Program Lead

Technographic Fit

Displacement / Modernization Signals:
" Using on-prem data warehouses that can't scale ’ Oracle Exadata, IBM Netezza
" Limited access to unstructured or real-time data ’ SAP BW, Informatica PowerCenter

Expansion Signals:
" Recently adopted cloud data platform ’ Snowflake, Databricks, BigQuery
" Using modern orchestration or catalog tools ’ Apache Airflow, Alation, Collibra
```

## Research Best Practices

**Time Management:**
- Research phase: 3-5 minutes with 8-12 targeted searches
- Prioritize based on information gaps in brief
- Focus on: competitor validation + industry pain points + top legacy vendors

**Search Strategy:**
- Use specific product names, not generic terms
- Include "2025" or "2024" for current information
- Look for vendor comparison sites, G2, peer insights
- Check recent analyst reports and vendor press releases

**Quality Signals:**
- Prioritize vendor names appearing in multiple results
- Look for case studies showing customer migrations
- Validate company size and industry from testimonials
- Check if products are still actively sold (not discontinued)

## Validation Checklist

Before completing, verify:

-  **Ontology Context Loaded**: Called GTM Fabric Ontologies MCP server for ICP framework
-  **Research Completed**: Conducted WebSearch for vendors, competitors, pain points
-  **Structure**: 4 ICPs included, formatted correctly
-  **Vendor Precision**: Real, current vendors/products validated through research
-  **Business Logic**: Pain = Legacy, Readiness = Acceleration
-  **Tone**: Executive, credible, business-first
-  **Segmentation**: 4 distinct buyer segments
-  **JSON Generated**: Structured JSON format created
-  **PowerPoint Created**: Professional .pptx presentation with title slide + 4 ICP slides
-  **Deliverable Provided**: Download link to final presentation file

## GTM Fabric Ontology Alignment

This skill aligns with GTM Fabric's ontological framework:

**Core Concepts:**
- `gtm:IdealCustomerProfile` - Root concept for outputs
- `gtm:BuyerPersona` - Maps to Key Job Roles section
- `gtm:FirmographicQuality` - Maps to Industries and company filters
- `gtm:TechnographicQuality` - Foundation for Technographic Fit section

**Technographic Concepts:**
- `gtm:CompetitiveTechnologyStack` - Displacement / Modernization Signals
- `gtm:ComplementaryTechnologyStack` - Expansion Signals
- `gtm:CompetitiveTechnologyProfile` - Competitive displacement strategies
- `gtm:TechnologyInstallData` - HG Insights/install base validation

**Account Scoring Connection:**
- `gtm:FitScore` - Firmographic + technographic alignment
- `gtm:NeedScore` - Pain intensity / urgency signals
- `gtm:IntentScore` - Buying readiness signals
- `gtm:TechnographicAttribute` - Competitive displacement and complementary tech opportunities

**Process Alignment:**
- `gtm:ICPBuildingProcess` - Overall workflow
- `gtm:DataInterrogationProcess` - Research validation phase
- `gtm:ICPRefinementProcess` - Iterative improvement

## Implementation Notes

1. **DemandScience Context**: Input represents B2B services workflow where DemandScience delivers ABM campaigns for customers (tech vendors) to reach target accounts

2. **Required vs Optional**: Email Context, Solution Focus, and Targeting Criteria are minimum inputs

3. **Sales Strategy**: Pay attention to sales play, motion, tactics:
   - Competitive displacement (takeout play)
   - Upsell/expansion (land and expand)
   - New market entry (greenfield)
   - Partner channel (ecosystem play)

4. **Implicit Information**: Extract unstated requirements from context

5. **Multi-ICP Scenarios**: Differentiate by:
   - Product line (different solutions)
   - Vertical industry (same solution, different markets)
   - Company size segment (enterprise vs mid-market)
   - Sales motion (new logo vs expansion)

6. **Data Source Awareness**: Note campaign targeting data source (HG Insights, BuyerCaddy, intent data, install base)

7. **Campaign Objectives Drive Everything**: All indicators should tie back to sales strategy

## Complete Workflow Example

**Input**: "Create ICPs for Kaspersky XDRO (endpoint protection) targeting mid-market financial services in North America. They want to displace Symantec and McAfee."

**Execution Flow**:

```
Step -1: Load Ontology Context
  Call: mcp__gtm-fabric-ontologies__get_ontology_stats
  Call: mcp__gtm-fabric-ontologies__extract_ontology_classes (gtm-targeting-icp)
  Call: mcp__gtm-fabric-ontologies__search_ontologies (keyword: "displacement")
  Extract: CompetitiveTechnologyStack, ComplementaryTechnologyStack concepts

Step 0: Research Process
  WebSearch: "endpoint protection vendors 2025"
  WebSearch: "Symantec endpoint protection problems"
  WebSearch: "McAfee ePO limitations"
  WebSearch: "financial services endpoint security challenges 2025"
  WebSearch: "SIEM adoption financial services"
  WebSearch: "most used endpoint protection enterprise 2025"
  WebFetch: [Top 2-3 relevant URLs for deeper context]
  Compile: Legacy products list, Modern products list, Pain points, Buyer roles

Step 1: Extract Offering Definition
  Output: "XDRO provides extended detection and response for endpoints, modernizing legacy antivirus with behavioral analytics"

Step 2: Infer Industries & Buyer Personas
  Output: Banking, Insurance, Fintech | CISO, Head of Endpoint Security, IT Security Director

Step 3: Build Technographic Fit
  Displacement Signals: Symantec Endpoint Protection, McAfee ePO, Trend Micro OfficeScan
  Expansion Signals: Splunk Enterprise Security, Microsoft Defender for Endpoint, CrowdStrike Falcon

Step 4: Generate JSON
  Create structured JSON with 4 distinct ICPs (different industry focuses, company sizes, or pain profiles)

Step 5: Create PowerPoint
  Use applying-brand-guidelines-gtmfabric skill for GTM Fabric design system
  Create title slide: "Kaspersky - Ideal Customer Profiles"
  Create 4 ICP slides with formatted content
  Save presentation
  Provide download link

Final Output: Professional PowerPoint presentation ready for DemandScience sales team
```

**Time Estimate**: 5-8 minutes total
- Ontology loading: 30 seconds
- Research: 3-5 minutes
- ICP generation: 1-2 minutes
- PowerPoint creation: 1-2 minutes

## Continuous Improvement

- Keep reference list of verified vendor technologies by category
- Update examples quarterly to match new product names and market shifts
- Recognize pattern clusters (e.g., "spreadsheet pain" ’ FP&A, "legacy antivirus" ’ Endpoint Security)
- If input lacks specificity, generate 4 most plausible ICPs for the offering's category
