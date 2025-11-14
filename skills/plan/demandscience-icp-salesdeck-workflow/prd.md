
# DemandScience ICP Generation Workflow Product Requirements Document (PRD)

## Executive Summary

## Problem Definition

GTM Fabric team members (Ashwin, Liam, and Catherine) experience significant operational burden and workflow inefficiency due to the manual, time-intensive process of creating research-validated ICPs for DemandScience partnership requests.

## Value Creation Opportunity

### For GTM Fabric's DemandScience Partnership

Reducing ICP deliverable turnaround from 2-4 hours to under 5 minutes enables GTM Fabric to support 10-20x more joint sales cycles without additional headcount, strengthening their position as DemandScience's preferred data strategist versus raw-data-only competitors. This velocity improvement increases data sales attach rates across DemandScience's 1,500+ customer ABM campaigns and creates a replicable playbook for scaling similar high-touch partnerships across GTM Fabric's Workflow & Services provider ecosystem.

### For Ashwin & Catherine (Post-Acquisition)

Automating the DemandScience ICP workflow eliminates 60-70% of their repetitive tactical work (5 hours/week for Ashwin, 3 hours/week for Catherine), allowing them to redirect their ecosystem intelligence and AI expertise toward higher-leverage activities: expanding GTM Fabric's partner network, developing new EIaaS offerings, and establishing strategic credibility in the merged organization rather than being trapped in operational delivery.

## Target Users

- Ashwin & Catherine (GTM Fabric tech team members, post-Eazy acquisition)
- Liam (GTM Fabric Account Executive)

## Use Case

Joint GTM Sales Enablement - Produce research-validated ICPs for DemandScience to use in joint selling motions with GTM Fabric, positioning GTM Fabric's curated data alongside DemandScience's ABM platform to both new and existing DemandScience customers

## Solution

**High-level solution approach:**
Develop and implement a Claude skill that automates research-validated ICP creation for DemandScience partnership requests, reducing delivery time from 2-4 hours to under 5 minutes with outputs in both human-reviewable Markdown and professionally branded standalone HTML sales reports.

## User Story

### Generate Research-Validated ICPs from DemandScience Email Brief

**Story:**
As a GTM Fabric team member (Ashwin, Liam, or Catherine), I want to paste the contents of an unstructured email from DemandScience into Claude and receive research-validated ICPs output first in plain text Markdown for human-in-the-loop verification and edits, and then convert the human-verified/edited version into structured JSON format, so that I can quickly deliver professional ICP data for joint GTM motions without spending 2-4 hours on manual research and formatting.

**Given:** I receive an email from DemandScience containing campaign requirements for their technology vendor client (DemandScience Customer: e.g., Kaspersky, Vena Solutions, Autodesk)

**When:** I paste the email brief into Claude

**Then:** Claude conducts systematic web research, generates at least 3 distinct ICPs with validated vendor/product names, outputs them first as plain text Markdown for my review and editing, and upon my approval generates a complete standalone HTML sales report with embedded branding for professional presentation to DemandScience.

## Business Situation & Business Process Context

### About DemandScience

DemandScience is a Global B2B revenue marketing and data company with a revenue intelligence platform that provides:

- B2B contact data and company intelligence
- Account-Based Marketing (ABM) / Account-Based Experience (ABX) platform
- Intent data and predictive analytics
- Omnichannel marketing campaign execution
- Managed services for demand generation

### GTM Fabric's Relationship with DemandScience

GTM Fabric sells to and partners with leading Workflow and Services companies including DemandScience to provide a white glove experience ensuring data purchases are quickly operationalized for specific use cases and outcome delivery.

### The Vendor / Partnership Model

#### GTM Fabric's Role

- Provides curated data foundation (technographic data from HG Insights, firmographic data, intent data, contact data)
- Offers expert network of GTM data operators and innovators
- Delivers scalable infrastructure for data integration and orchestration

#### DemandScience's Role

- Activates and operationalizes the data for ABM campaigns
- Provides campaign execution services (email, display ads, content syndication)
- Delivers managed services for demand generation and lead generation
- Offers contact enrichment and intent signal activation
- Executes multi-channel outreach to target accounts

### Value Chain

```
GTM Fabric (Data Curator + Strategist)
           ↓
Provides curated datasets and sales business development slide decks that DemandScience
uses in a joint go-to-market effort with GTM Fabric, selling GTM Fabric's data together
with their own solutions to both new and existing DemandScience customers.
           ↓
DemandScience (Campaign Executor + Operationalizer)
           ↓
Executes ABM campaigns for technology vendors
           ↓
Target Accounts (Prospective Customers)
```
### GTM Fabric Workflow: ICP Creation for DemandScience

1. DemandScience sellers receive campaign requirements from their technology vendor clients (e.g., Kaspersky, Vena Solutions, Autodesk)
2. DemandScience emails GTM Fabric with these requirements to request ICP creation services
3. GTM Fabric creates the research-validated ICPs and delivers them to DemandScience as a professionally branded HTML sales report
4. DemandScience then uses these ICPs to execute joint go-to-market effort with GTM Fabric, selling GTM Fabric's data together with their own solutions to both new and existing DemandScience customers

## Acceptance Criteria

Human-in-the-Loop Review Process
  - Skill outputs ICPs in Markdown and explicitly requests user review
  - User can edit, refine, or approve ICP content
  - System accepts the human-verified/edited content as input for JSON conversion

JSON Output Requirements
  - Well-structured JSON with consistent schema
  - All ICP fields properly mapped and formatted
  - Valid JSON that can be parsed programmatically
  - Ready for downstream data integration

## Definition of Done

## Must Have Features (MVP)

- **Feature 1: Email Brief Parsing & ICP Research**
  - Extract campaign requirements from DemandScience email
  - Conduct systematic web research for vendor validation
  - Generate at least 3 distinct, research-validated ICPs
  - Acceptance: All ICPs contain real vendor names and validated products

- **Feature 2: Markdown Output with Human Review**
  - Output ICPs in plain text Markdown format
  - Explicitly request user review with clear prompt
  - Accept human edits and refinements
  - Acceptance: User can edit all content before JSON conversion

- **Feature 3: Structured JSON Output**
  - Convert approved Markdown to well-formatted JSON
  - Implement consistent schema for all ICP fields
  - Include campaign metadata and DemandScience customer information
  - Validate JSON structure before output
  - Acceptance: Valid, parseable JSON with complete ICP data ready for downstream integration

## Implementation Requirements (Based on Claude Skills Best Practices)

### API Configuration

**Required Beta Namespace:**
- Use `client.beta.messages.create()` (not `client.messages.create()`)
- Include all three beta flags: `code-execution-2025-08-25`, `files-api-2025-04-14`, `skills-2025-10-02`
- Code execution tool REQUIRED: `tools=[{"type": "code_execution_20250825", "name": "code_execution"}]`

**Skill Container Pattern:**
```python
# Stage 1: ICP Generation (custom skill only)
container={
    "skills": [
        {"type": "custom", "skill_id": "demandscience-icp-skill-id", "version": "latest"}
    ]
}

# Stage 2: JSON Generation (custom skill only)
container={
    "skills": [
        {"type": "custom", "skill_id": "demandscience-icp-skill-id", "version": "latest"}
    ]
}
```

### Performance Expectations

Based on implementation testing:
- **Stage 1** (ICP Research & Markdown): 2-3 minutes
- **Stage 2** (JSON Generation): <30 seconds
- **Total workflow**: Under 5 minutes ✅
- **Token usage**:
  - Stage 1: ~70,000 tokens
  - Stage 2: ~5,000 tokens
  - Total: ~75,000 tokens

### Custom Skill Structure

**Directory Layout:**
```
demandscience-icp-skill/
├── SKILL.md              # Main instructions (< 5,000 tokens recommended)
├── REFERENCE.md          # Optional: Additional documentation
└── EXAMPLES.md           # Optional: Usage examples
```

**YAML Frontmatter Requirements:**
```yaml
---
name: demandscience-icp-json
description: Generates research-validated ICPs for DemandScience partnership requests. Extracts campaign requirements from email briefs, conducts web research, outputs Markdown for human review, then converts to structured JSON.
---
```

Constraints:
- `name`: Lowercase alphanumeric with hyphens, max 64 characters
- `description`: Brief summary, max 1024 characters
- Instructions: Keep under 5,000 tokens for optimal performance

### Progressive Disclosure Architecture

Skills load in three stages to optimize token usage:

| Stage | Content | Token Cost | When Loaded |
|-------|---------|------------|-------------|
| **1. Metadata** | name & description | ~100 tokens | Always visible |
| **2. Instructions** | All .md files | <5,000 tokens | When skill is invoked |
| **3. Resources** | Template files | As needed | During execution |

## Required Tooling

- Claude API with Skills Beta support
- Web research capabilities (WebSearch or similar)
- JSON formatting and validation capabilities

## Tooling Constraints

- Claude API with Skills support
- Web research capabilities for vendor/product validation
- JSON output formatting

## Prompts Used To Accomplish This Manually 

## Example Inputs

## Example Outputs