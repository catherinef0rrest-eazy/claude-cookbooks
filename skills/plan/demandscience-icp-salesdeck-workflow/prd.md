
# DemandScience ICPs & Sales Deck Workflow Product Requirements Document (PRD)

## Executive Summary

## Problem Definition

GTM Fabric team members (Ashwin, Liam, and Catherine) experience significant operational burden and workflow inefficiency due to the manual, time-intensive process of creating research-validated ICPs and sales business development slide decks for DemandScience partnership requests.

## Value Creation Opportunity

### For GTM Fabric's DemandScience Partnership

Reducing ICP deliverable turnaround from 2-4 hours to under 10 minutes enables GTM Fabric to support 10-20x more joint sales cycles without additional headcount, strengthening their position as DemandScience's preferred data strategist versus raw-data-only competitors. This velocity improvement increases data sales attach rates across DemandScience's 1,500+ customer ABM campaigns and creates a replicable playbook for scaling similar high-touch partnerships across GTM Fabric's Workflow & Services provider ecosystem.

### For Ashwin & Catherine (Post-Acquisition)

Automating the DemandScience ICP workflow eliminates 60-70% of their repetitive tactical work (5 hours/week for Ashwin, 3 hours/week for Catherine), allowing them to redirect their ecosystem intelligence and AI expertise toward higher-leverage activities: expanding GTM Fabric's partner network, developing new EIaaS offerings, and establishing strategic credibility in the merged organization rather than being trapped in operational delivery.

## Target Users

- Ashwin & Catherine (GTM Fabric tech team members, post-Eazy acquisition)
- Liam (GTM Fabric Account Executive)

## Use Case

Joint GTM Sales Enablement - Produce sales business development decks for DemandScience to use in joint selling motions with GTM Fabric, positioning GTM Fabric's curated data alongside DemandScience's ABM platform to both new and existing DemandScience customers

## Solution

**High-level solution approach:**
Develop and implement Claude skill(s) that automates research-validated ICP creation and PowerPoint sales deck generation for DemandScience partnership requests, reducing delivery time from 2-4 hours to under 10 minutes.

## User Story

### Generate Research-Validated ICPs from DemandScience Email Brief

**Story:**
As a GTM Fabric team member (Ashwin, Liam, or Catherine), I want to paste the contents of an unstructured email from DemandScience into Claude and receive research-validated ICPs output first in plain text Markdown for human-in-the-loop verification and edits, and then convert the human-verified/edited version into PowerPoint format, so that I can quickly deliver professional sales enablement materials for joint GTM motions without spending 2-4 hours on manual research and formatting.

**Given:** I receive an email from DemandScience containing campaign requirements for their technology vendor client (DemandScience Customer: e.g., Kaspersky, Vena Solutions, Autodesk)

**When:** I paste the email brief into Claude

**Then:** Claude conducts systematic web research, generates a least 3 distinct ICPs with validated vendor/product names, outputs them first as plain text Markdown for my review and editing, and upon my approval builds the content into a PowerPoint presentation that successfully implements GTM Fabric branding requirements.

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
### GTM Fabric Workflow ICP Sales Business Development Slide Deck Creation for DemandScience

1. DemandScience sellers receive campaign requirements from their technology vendor clients (e.g., Kaspersky, Vena Solutions, Autodesk)
2. DemandScience emails GTM Fabric with these requirements to request ICP creation services
3. GTM Fabric creates the research-validated ICPs and delivers the ICPs to DemandScience in sales business development slide decks
4. DemandScience then uses these ICPs to execute joint go-to-market effort with GTM Fabric, selling GTM Fabric's data together with their own solutions to both new and existing DemandScience customers

## Acceptance Criteria

Human-in-the-Loop Review Process
  - Skill outputs ICPs Markdown and explicitly requests user review
  - User can edit, refine, or approve ICP content
  - System accepts the human-verified/edited content
   as input for PowerPoint generation

## Definition of Done

## Must Have Features

- **[Feature 1]**: [Description and acceptance criteria]
- **[Feature 2]**: [Description and acceptance criteria]
- **[Feature 3]**: [Description and acceptance criteria]

## Required Tooling

- Claude API with Skills Beta support
- Web research capabilities (WebSearch or similar)
- Python-pptx library for PowerPoint generation

## Tooling Constraints

- Claude API with Skills support
- Web research capabilities for vendor/product validation
- Python-pptx library for PowerPoint generation

## Prompts Used To Accomplish This Manually 

## Example Inputs

## Example Outputs