# DemandScience ICP Generation Skill

Automates research-validated ICP creation for DemandScience partnership requests with standalone HTML sales report output.

## Quick Start

### 1. Upload the Skill

```bash
cd /path/to/demandscience-icp-json
python upload_skill.py
```

### 2. Test the Skill

```bash
python test_skill.py
```

## What This Skill Does

Creates research-validated Ideal Customer Profiles (ICPs) for DemandScience campaigns in two stages:

**Stage 1**: Email brief → Web research → Markdown ICPs (with human review)
**Stage 2**: Approved Markdown → Standalone HTML Report (with embedded branding)

## Workflow

```
┌─────────────────────────────────────────────────────────────┐
│  User pastes DemandScience email brief                     │
└─────────────────────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 1: Research & Generate ICPs                         │
│  • Web research for vendors/competitors                     │
│  • Generate 3+ distinct ICPs                                │
│  • Output Markdown for review                               │
│  • Time: 2-3 minutes                                        │
└─────────────────────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│  HUMAN REVIEW GATE                                          │
│  User can:                                                  │
│  • Edit vendor names, pain points                           │
│  • Adjust industries, departments, roles                    │
│  • Refine technographic signals                             │
│  • Approve for HTML report generation                       │
└─────────────────────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│  STAGE 2: Generate Standalone HTML Report                  │
│  • Parse approved Markdown to JSON (internal)               │
│  • Load resources (CSS, assets, renderer)                   │
│  • Generate complete HTML file                              │
│  • Time: 30-60 seconds                                      │
└─────────────────────────────────────┬───────────────────────┘
                                      │
                                      ▼
┌─────────────────────────────────────────────────────────────┐
│  OUTPUT: Standalone HTML file ready to download & share    │
│  Size: ~485 KB | Works offline | All branding embedded     │
└─────────────────────────────────────────────────────────────┘
```

## Input Format

Paste an email brief from DemandScience containing:

**Required:**
- DemandScience Customer name (the tech vendor)
- Products being marketed
- Campaign goal or use case

**Optional but helpful:**
- Target industries
- Target region
- Competitive displacement targets
- Company size filters

### Example Input

```
From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Vena Solutions

We need ICPs for Vena Solutions targeting finance teams in mid-market companies.

Products: Vena Complete Planning Platform
Target Industries: Technology, Manufacturing, Professional Services
Use Case: Replacing legacy Excel-based planning and Oracle/SAP EPM systems
Region: North America

Please generate ICPs for this campaign.
```

## Output Format

### Stage 1: Markdown

```markdown
# Research-Validated ICPs for Vena Solutions

## ICP 1: Mid-Market Technology - Cloud FP&A Transformation

### Industries
- Technology, SaaS, Software Services, IT Services

### Departments & Business Functions
- Finance & Accounting
- FP&A (Financial Planning & Analysis)
- Corporate Development

**Key Job Roles / Job Titles:**
- CFO
- VP Finance
- FP&A Director

### Technographic Fit

**Displacement / Modernization Signals:**
- Excel-based planning causing version control issues → **Microsoft Excel**
- Legacy EPM systems too complex for mid-market → **Oracle Hyperion**
- Manual consolidation taking weeks → **Excel Spreadsheets**
- On-premise tools limiting remote collaboration → **IBM Planning Analytics**

**Expansion Signals:**
- Salesforce CRM users needing revenue planning → **Salesforce**
- Microsoft 365 ready for Excel integration → **Microsoft Power BI**
- Cloud infrastructure investments → **Snowflake**
- Recent NetSuite ERP implementations → **NetSuite**

---
[ICPs 2 and 3...]
```

### Stage 2: Standalone HTML Report

**Output**: Complete, self-contained HTML file that can be opened in any browser

**Features**:
- ✅ All branding embedded (GTM Fabric + DemandScience logos)
- ✅ Professional design with sidebar and Propensity Funnel
- ✅ Dynamic ICP cards (handles variable # of ICPs)
- ✅ Works completely offline (no server needed)
- ✅ Responsive design (mobile + desktop)
- ✅ Ready to share via email or cloud storage

**File Structure**:
```html
<!DOCTYPE html>
<html>
<head>
    <title>ICP Sales Report - Vena Solutions</title>
    <style>
        /* Complete CSS embedded (23 KB) */
    </style>
</head>
<body>
    <!-- Sidebar with campaign metadata -->
    <!-- Propensity Funnel visualization -->
    <!-- Dynamic ICP cards -->

    <script>
        // Embedded assets (logos, icons as base64 - 376 KB)
        const EMBEDDED_ASSETS = {...};

        // Embedded ICP data
        const ICP_DATA = {...};

        // Renderer code
        class ICPRenderer {...}
    </script>
</body>
</html>
```

**File Size**: ~485 KB (complete with all assets and data)

**Usage**:
1. User copies HTML from skill output
2. Saves to `.html` file
3. Opens in browser (Chrome, Firefox, Safari, Edge)
4. Shares with DemandScience or stakeholders

## Performance

- **Stage 1**: 2-3 minutes (research + ICP generation)
- **Stage 2**: 30-60 seconds (HTML generation with embedded assets)
- **Total**: Under 5 minutes ✅

**Token Usage:**
- Stage 1: ~60,000-70,000 tokens (research-heavy)
- Stage 2: Minimal tokens (template-based generation)
- Total: ~60,000-75,000 tokens

**Output Size:**
- HTML file: ~485 KB
- Includes: CSS (23 KB) + Assets (376 KB) + Data (~15 KB) + JavaScript (11 KB)

## Key Features

### Research-Validated Vendors
- Web research validates all vendor/product names
- No fictional or outdated vendors
- Current market intelligence (2025)

### Human-in-the-Loop
- Markdown review before HTML generation
- Edit any content before finalizing
- Ensures accuracy and relevance

### Standalone HTML Report
- Complete self-contained file
- All branding and assets embedded
- Works offline, no server needed
- Professional sales presentation format
- Easy to share and distribute

### Quality Validation
- Minimum 3 distinct ICPs
- Maximum capacity limits (4 industries, 3 departments, 3 roles)
- All vendor names preserved exactly
- Valid HTML with proper escaping
- File size < 600 KB

## API Usage

### Stage 1: Generate ICPs

```python
from anthropic import Anthropic

client = Anthropic(api_key=API_KEY)

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": SKILL_ID, "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": email_brief}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02"
    ]
)

# Extract Markdown ICPs
markdown_icps = response.content[0].text
print(markdown_icps)
```

### Stage 2: Generate HTML Report

```python
# After user approves
stage2_prompt = f"""
The user has approved the following ICPs. Please generate the standalone HTML report.

{markdown_icps}

Campaign Details:
- DemandScience Customer: Vena Solutions
- Products: Vena Complete Planning Platform
- Campaign Goal: Target finance teams replacing legacy Excel and EPM
- Target Region: North America
- Year: 2025
"""

response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": SKILL_ID, "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": stage2_prompt}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02"
    ]
)

# Extract HTML
text = response.content[0].text
html_start = text.find("```html") + 7
html_end = text.find("```", html_start)
html_content = text[html_start:html_end].strip()

# Save to file
with open("icp-report-vena-2025-11-13.html", "w") as f:
    f.write(html_content)

print(f"HTML report saved: {len(html_content) / 1024:.1f} KB")
```

## Testing

### Prerequisites

1. **Python Environment**
   - Python 3.8 or higher
   - Virtual environment (recommended)

2. **Dependencies**
   ```bash
   pip install anthropic python-dotenv
   ```

3. **API Key**
   - Create `.env` file with `ANTHROPIC_API_KEY=your-key-here`

### Step 1: Upload the Skill

```bash
python upload_skill.py
```

This will upload SKILL.md, README.md, and REFERENCE.md and save the skill ID to `skill_id.txt`.

### Step 2: Run Basic Test

```bash
python test_skill.py
```

This runs the default Vena Solutions test with human review between Stage 1 and Stage 2.

### Step 3: Run with Auto-Approval

```bash
python test_skill.py --auto-approve
```

Runs both stages without manual approval (good for quick testing).

### Step 4: Test with Custom Input

```bash
python test_skill.py --email-file my_test.txt --auto-approve
```

See `test_inputs.txt` for 6 ready-to-use test scenarios:
1. Vena Solutions (Financial Planning)
2. Kaspersky (Cybersecurity)
3. Autodesk (Software Licensing)
4. HubSpot (Marketing Automation)
5. Snowflake (Data Warehouse)
6. KnowBe4 (Security Awareness)

### Test Outputs

Outputs are saved to `test_outputs/`:
- `icps_stage1.md` - Markdown ICPs from Stage 1
- `icps_stage2.json` - Validated JSON output from Stage 2

### Common Errors

**Error: "skill_id.txt not found"**
- Solution: Run `python upload_skill.py` first

**Error: "ANTHROPIC_API_KEY not found"**
- Solution: Create `.env` file with your API key

**Error: "Skill cannot reuse an existing display_title"**
- Solution: Delete existing skill or change `display_title` in `upload_skill.py`

**JSON Parsing Failed**
- Solution: Check Stage 2 response in terminal output

## Use Cases

- **DemandScience Partnership Requests**: Primary use case
- **ABM Campaign Planning**: Generate target profiles for campaigns
- **Sales Enablement**: Create buyer personas for sales teams
- **Data Integration**: Structured output for CRM/marketing platforms
- **Market Research**: Validate target markets with real vendor data

## Validation

The skill includes built-in quality checks:

**Stage 1 (Markdown)**:
- ✓ Research completed via WebSearch
- ✓ At least 3 distinct ICPs
- ✓ All vendor names validated
- ✓ Capacity limits enforced
- ✓ Business-first language

**Stage 2 (JSON)**:
- ✓ Valid JSON syntax
- ✓ Complete schema
- ✓ All required fields present
- ✓ snake_case naming
- ✓ Arrays properly formatted

## Troubleshooting

### Research Fails
- Check internet connectivity
- Verify WebSearch tool is available
- Try alternative search terms

### JSON Invalid
- Check for special characters in text
- Verify all arrays use `["item"]` format
- Ensure proper escaping of quotes

### Missing Fields
- Verify all required campaign details in brief
- Check ICP structure matches schema
- Ensure vendor names extracted correctly

## Files

```
demandscience-icp-json/
├── SKILL.md              # Main skill instructions
├── README.md             # This file - usage & testing guide
├── REFERENCE.md          # JSON schema reference
├── upload_skill.py       # Upload skill to Claude API
├── test_skill.py         # Two-stage test script with validation
└── test_inputs.txt       # 6 example campaign briefs
```

## Support

For issues or questions:
1. Check the tech_spec.md in the plan folder
2. Review example inputs and outputs
3. Validate JSON schema requirements

## Version History

- **v1.0.0** (2025-11-13): Initial release
  - Two-stage workflow with human review
  - Research-validated vendor names
  - Structured JSON output
  - Under 5-minute total workflow
