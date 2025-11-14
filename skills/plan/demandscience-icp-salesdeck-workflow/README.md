# DemandScience ICP & Sales Deck Skill

Automated generation of research-validated ICPs and branded PowerPoint sales decks for DemandScience partnership requests.

## Quick Start

### 1. Prerequisites

- Python 3.8+
- Anthropic API key with Skills beta access
- Anthropic SDK ≥ 0.71.0

### 2. Setup

```bash
# Install dependencies (if not already installed)
pip install anthropic python-dotenv

# Ensure ANTHROPIC_API_KEY is set in environment or .env file
export ANTHROPIC_API_KEY="your-api-key"
```

### 3. Upload the Skill

```bash
python upload_skill.py
```

This will:
- Validate skill files (SKILL.md, template)
- Upload skill to your Claude workspace
- Save skill ID to `skill_id.txt`

### 4. Test the Skill

```bash
python test_skill.py
```

This will:
- **Stage 1**: Generate research-validated ICPs in Markdown (2-3 minutes)
- Display ICPs for your review
- **Stage 2**: Convert approved ICPs to PowerPoint (1-2 minutes)
- Download PowerPoint file to `outputs/` directory

### 5. Review Output

Open the generated PowerPoint file in `outputs/` and verify:
- ✓ Branding matches GTM Fabric specifications
- ✓ All placeholders replaced
- ✓ Slides 3-4 unchanged from template
- ✓ Minimum 3 ICP slides present
- ✓ Vendor names bold in Technographic Fit boxes

---

## Directory Structure

```
demandscience-icp-salesdeck-workflow/
├── demandscience-icp-skill/        # Custom skill directory
│   ├── SKILL.md                    # Skill instructions
│   └── resources/
│       └── demandscience_icp_salesdeck_example_pptx_output.pptx
├── upload_skill.py                 # Upload skill to Claude
├── test_skill.py                   # Test skill workflow
├── skill_id.txt                    # Generated skill ID (after upload)
├── outputs/                        # Generated PowerPoint files
├── prd.md                          # Product requirements
├── tech_spec.md                    # Technical specification
├── implementation_plan.md          # Implementation guide
└── qa_testing_plan.md              # QA procedures
```

---

## Workflow

### Two-Stage Process

**Stage 1: ICP Generation**
- User provides DemandScience email brief
- Skill conducts web research to validate vendors
- Generates 3+ ICPs in Markdown format
- User reviews and approves

**Stage 2: PowerPoint Generation**
- Skill converts approved Markdown to PowerPoint
- Applies GTM Fabric branding
- Generates branded .pptx file

**Total Time**: < 10 minutes ✅

---

## Usage Options

### Default Test Email

```bash
python test_skill.py
```

Uses built-in Vena Solutions example email.

### Custom Email File

```bash
python test_skill.py --email-file my_email.txt
```

### Stage 1 Only (Skip PowerPoint)

```bash
python test_skill.py --skip-stage2
```

---

## Example Email Brief

```
From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Kaspersky XDRO

We need ICPs for Kaspersky's Extended Detection and Response Offering (XDRO)
targeting mid-market financial services firms in North America.

Products: Kaspersky XDRO, Kaspersky Endpoint Security
Target: Financial services, healthcare, retail
Use case: Competitive displacement of CrowdStrike and SentinelOne
```

---

## Output Format

### Stage 1: Markdown

```markdown
# Research-Validated ICPs for Kaspersky XDRO

## ICP 1: Mid-Market Financial Services - Endpoint Security Modernization

### Industries
- Financial Services, Banking, Insurance, Wealth Management

### Departments & Business Functions
- Information Security
- IT Operations
- Risk Management

**Key Job Roles / Job Titles:**
- CISO
- VP Information Security
- IT Security Director

### Technographic Fit

**Displacement / Modernization Signals:**
- Legacy endpoint protection reaching end-of-life → **Symantec Endpoint Protection**
- Traditional AV struggling with advanced threats → **McAfee Endpoint Security**
...
```

### Stage 2: PowerPoint

- **Slide 1**: Campaign cover (customer name, products, year)
- **Slide 2**: Customer name as text ("Kaspersky")
- **Slides 3-4**: Static GTM Fabric content
- **Slides 5+**: One slide per ICP (minimum 3)

---

## Troubleshooting

### Skill Upload Fails

**Error**: "cannot reuse an existing display_title"

**Solution**: Delete existing skill or use different display_title

```python
# List existing skills
from anthropic import Anthropic
client = Anthropic()
skills = client.beta.skills.list(source="custom")
for skill in skills.data:
    print(f"{skill.display_title}: {skill.id}")
```

### File Download Fails

**Error**: "BinaryAPIResponse object has no attribute 'content'"

**Solution**: Code already uses `.read()` method (correct approach)

### PowerPoint Not Generated

**Possible causes**:
1. Template file missing from `demandscience-icp-skill/resources/`
2. User didn't approve Stage 1 Markdown
3. API timeout (retry)

---

## Golden Test Cases

Use these for QA validation:

1. **Vena Solutions** - FP&A planning, Oracle/SAP replacement
2. **Kaspersky XDRO** - Endpoint security, CrowdStrike displacement
3. **Autodesk** - CAD/design tools, license upgrades

---

## Performance Benchmarks

Based on testing:

| Stage | Expected Time | Token Range | Success Rate |
|-------|---------------|-------------|--------------|
| Stage 1 (ICP Markdown) | 2-3 minutes | 3,000-5,000 | 95%+ |
| Stage 2 (PowerPoint) | 1-2 minutes | 2,000-3,000 | 98%+ |
| **Total Workflow** | **<10 minutes** | **5,000-8,000** | **93%+** |

---

## Phase 2 Features (Future)

Not yet implemented:
- Automated logo discovery via web search
- Logo quality validation (resolution, format, background)
- User approval workflow for logos
- Inserting actual logo images into Slide 2

**Current Phase 1**: Slide 2 uses customer name as text only.

---

## Documentation

- `prd.md` - Product requirements document
- `tech_spec.md` - Technical specification with API details
- `implementation_plan.md` - Complete implementation guide
- `qa_testing_plan.md` - QA testing procedures
- `pptx_template_analysis.md` - Template reverse engineering
- `phase_1_vs_phase_2.md` - Feature comparison

---

## Support

For issues or questions:
1. Check error messages in console output
2. Review `tech_spec.md` API Implementation Details section
3. Verify ANTHROPIC_API_KEY is set correctly
4. Ensure Anthropic SDK ≥ 0.71.0 installed

---

## Version

**Current Version**: 1.0 (Phase 1)
- ✅ Email brief parsing
- ✅ Web research for vendor validation
- ✅ Markdown ICP generation (minimum 3)
- ✅ Human-in-the-loop review
- ✅ Branded PowerPoint generation
- ✅ Static slides preserved (Slides 3-4)
- ✅ Customer name as text on Slide 2

**Last Updated**: 2025-11-12
