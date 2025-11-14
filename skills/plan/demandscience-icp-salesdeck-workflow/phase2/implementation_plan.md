# DemandScience ICP Skill - Implementation Plan
## Applying Claude Skills Best Practices

---

## Executive Summary

This implementation plan applies best practices from the Claude Skills notebooks to build the DemandScience ICP generation skill. The plan ensures:
- Correct API usage patterns
- Optimal file generation workflow
- Proper error handling
- Production-ready code structure

**Estimated Development Time**: 6-9 hours (per original estimate)
**Expected Skill Performance**:
- Stage 1 (ICP Research & Markdown): ~2-3 minutes
- Stage 2 (PowerPoint Generation): ~1-2 minutes
- **Total workflow**: Under 10 minutes ✅

---

## Part 1: Best Practices Extracted from Notebooks

### API Patterns (from 01_skills_introduction.ipynb)

**Critical API Requirements:**
```python
# ✅ CORRECT: Beta namespace with all required parameters
response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": skill_id, "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": prompt}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02"
    ]
)

# ❌ WRONG: Standard namespace, missing betas, no code execution
response = client.messages.create(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": prompt}]
)
```

**File Download Pattern:**
```python
# ✅ CORRECT: Use .read() method
file_content = client.beta.files.download(file_id)
with open(path, 'wb') as f:
    f.write(file_content.read())  # Use .read()

# ✅ CORRECT: Use size_bytes property
metadata = client.beta.files.retrieve_metadata(file_id)
print(f"Size: {metadata.size_bytes} bytes")  # Use size_bytes, not size

# ❌ WRONG: Attempting to use .content or .size
file_content.content  # No such attribute!
metadata.size  # No such attribute!
```

### Skill Structure (from 03_skills_custom_development.ipynb)

**Directory Structure:**
```
demandscience-icp-skill/
├── SKILL.md              # REQUIRED: Main instructions with YAML frontmatter
├── REFERENCE.md          # OPTIONAL: Additional documentation
├── EXAMPLES.md           # OPTIONAL: Usage examples
├── scripts/              # OPTIONAL: Python scripts for complex logic
│   └── icp_research.py
└── resources/            # OPTIONAL: PowerPoint template
    └── demandscience_icp_salesdeck_example_pptx_output.pptx
```

**YAML Frontmatter Requirements:**
```yaml
---
name: demandscience-icp-salesdeck
description: Generates research-validated ICPs and branded PowerPoint sales decks for DemandScience partnership requests. Extracts campaign requirements from email briefs, conducts web research, outputs Markdown for human review, then converts to GTM Fabric branded PowerPoint.
---
```

**Key Constraints:**
- `name`: Lowercase alphanumeric with hyphens, max 64 characters
- `description`: Brief summary, max 1024 characters
- Instructions: Keep under 5,000 tokens (recommended)
- Multiple .md files allowed (all loaded automatically)

### Document Generation (from 02_skills_financial_applications.ipynb)

**PowerPoint Best Practices:**
- ✅ **2-3 slides per generation** = reliable and fast (~1-2 minutes)
- ✅ **Use template cloning** for branded documents
- ✅ **Clear, specific prompts** with exact content requirements
- ✅ **Sequential pipeline** for complex multi-document workflows
- ❌ Avoid complex 10+ slide presentations (slower, less reliable)

**Example Pipeline Pattern:**
```python
# Stage 1: Research and generate Markdown
markdown_response = client.beta.messages.create(
    model=MODEL,
    container={"skills": [{"type": "custom", "skill_id": icp_skill_id, "version": "latest"}]},
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": stage1_prompt}],
    betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"]
)

# Human reviews and approves Markdown...

# Stage 2: Convert approved Markdown to PowerPoint
pptx_response = client.beta.messages.create(
    model=MODEL,
    container={
        "skills": [
            {"type": "custom", "skill_id": icp_skill_id, "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": stage2_prompt_with_markdown}],
    betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"]
)

# Download PowerPoint file
file_ids = extract_file_ids(pptx_response)
results = download_all_files(client, pptx_response, output_dir="outputs", prefix="icp_deck_")
```

### Skill Composition (from 03_skills_custom_development.ipynb)

**Combining Skills:**
```python
# ✅ Custom skill + Anthropic skill together
container={
    "skills": [
        {"type": "custom", "skill_id": "skill_xxx", "version": "latest"},  # DemandScience ICP skill
        {"type": "anthropic", "skill_id": "pptx", "version": "latest"}     # PowerPoint generation
    ]
}

# ✅ Multiple custom skills
container={
    "skills": [
        {"type": "custom", "skill_id": "skill_abc", "version": "latest"},
        {"type": "custom", "skill_id": "skill_xyz", "version": "latest"}
    ]
}
```

---

## Part 2: Implementation Roadmap

### Phase 1: Skill Creation

#### Step 1: Create Skill Directory Structure

```bash
cd /Users/catherineforrest/gtmfabric/claude-cookbooks/skills/plan/demandscience-icp-salesdeck-workflow
mkdir -p demandscience-icp-skill/scripts
mkdir -p demandscience-icp-skill/resources
```

#### Step 2: Create SKILL.md

**File**: `demandscience-icp-skill/SKILL.md`

**Content Structure:**

```markdown
---
name: demandscience-icp-salesdeck
description: Generates research-validated ICPs and branded PowerPoint sales decks for DemandScience partnership requests. Extracts campaign requirements from email briefs, conducts web research, outputs Markdown for human review, then converts to GTM Fabric branded PowerPoint.
---

# DemandScience ICP & Sales Deck Generator

## Overview

This skill automates the creation of research-validated Ideal Customer Profiles (ICPs) and branded PowerPoint sales decks for DemandScience partnership requests.

## Workflow

### Stage 1: ICP Research & Markdown Generation

**Input**: Unstructured email from DemandScience containing campaign requirements

**Process**:
1. Extract campaign requirements (DemandScience customer, products, target audience)
2. Conduct systematic web research to validate vendor names and products
3. Generate at least 3 distinct ICPs with validated information
4. Output ICPs in Markdown format for human review

**Output Format**: Plain text Markdown with structured ICP content

**Human-in-the-Loop**: Explicitly request user review and edits before proceeding

### Stage 2: PowerPoint Generation

**Input**: Human-approved/edited ICP Markdown from Stage 1

**Process**:
1. Extract DemandScience customer name from campaign brief
2. Use template from resources/demandscience_icp_salesdeck_example_pptx_output.pptx
3. Apply GTM Fabric branding specifications
4. Generate PowerPoint file following template structure

**Output**: Branded .pptx file with complete ICP deck

## ICP Content Requirements

Each ICP must include:

### Industries (max 4)
- Research-validated industry categories
- Displayed as 2×2 pill grid in PowerPoint

### Departments & Business Functions (max 3)
- Specific departments that would use the product
- Plain list format

### Key Roles / Job Titles (max 3)
- Decision-makers and influencers
- Plain list format

### Technographic Fit

**Displacement / Modernization Signals (max 4):**
- Format: `[Pain/Problem] → **[Vendor Product]**`
- Example: `Legacy EPM platforms struggling with cloud migration → **Oracle EPM Cloud**`
- Vendor names must be bold

**Expansion Signals (max 4):**
- Format: `[Readiness indicator] → **[Vendor Product]**`
- Example: `Existing Salesforce users ready for analytics → **Tableau**`
- Vendor names must be bold

## PowerPoint Template Structure

**File**: `resources/demandscience_icp_salesdeck_example_pptx_output.pptx`

### Slide 1: Cover Slide
- Header: Campaign name or DemandScience customer name
- Subheader: Product(s) being marketed
- Description: Campaign objective/goal
- Year: Current year (e.g., "2025")

### Slide 2: Cover with Customer Logo (PHASE 1)
- **Phase 1 Implementation**: Replace `{target account logo}` with **customer name as text**
- Position: Center-right (9.69", 2.95")
- **Note**: `{target account logo}` = DemandScience's customer (e.g., Kaspersky, Vena Solutions)

### Slide 3: Key Elements for E2E Solutions (STATIC)
- **Never modified** - copy as-is from template
- GTM Fabric value proposition content
- No text replacement or dynamic content

### Slide 4: Propensity Funnel (STATIC)
- **Never modified** - copy as-is from template
- GTM Fabric methodology framework
- Placeholder fields remain unpopulated

### Slides 5+: ICP Slides (One per ICP, minimum 3)
- Duplicate Slide 5 template for each ICP generated
- Populate all placeholders with ICP content
- Maintain exact branding and layout

## Branding Specifications

### Slide Dimensions
- Format: Widescreen (16:9)
- Size: 20.00" × 11.25"

### Color Palette
- Slide Background: RGB(244, 246, 251) / #F4F6FB
- Primary Purple: RGB(50, 3, 97) / #320361
- Medium Gray (Pills): RGB(153, 153, 153) / #999999
- White (Boxes): RGB(255, 255, 255) / #FFFFFF
- Black (Accents): RGB(0, 0, 0) / #000000
- Text Color: RGB(40, 45, 73) / #282D49

### Typography
- Cover Header: Arial 80pt Regular, Primary Purple
- Cover Subheader: Arial Bold 74pt, Primary Purple
- Slide Titles: Arial 36pt Regular, Primary Purple
- Section Headers: Arial 18pt Regular, Dark Blue-Gray
- Body Text: Arial 14pt Regular, Dark Blue-Gray
- Descriptions: Arial 22pt Regular, Dark Blue-Gray

### Design Elements
- Purple circular icons for section headers (unique symbol per section)
- GTM Fabric branding element (top right of slides)
- Cream/off-white card backgrounds for left column sections
- White boxes with subtle borders for right column
- Industries: 2×2 pill grid with rounded corners (unique design)

## Web Research Requirements

For each ICP:
- Validate all vendor/product names through web search
- Ensure products/solutions actually exist
- Find real competitor products in displacement signals
- Verify expansion opportunity products are legitimate
- NO placeholder or fictional vendor names allowed

## Validation Rules

**Before PowerPoint Generation:**
- ✓ Minimum 3 ICPs generated
- ✓ All vendor names validated (real products/companies)
- ✓ User has reviewed and approved Markdown
- ✓ Each ICP contains all required sections
- ✓ Content fits within template capacity limits

**PowerPoint Quality Checks:**
- ✓ All placeholder text replaced (no `{...}` remaining)
- ✓ Slides 3-4 copied unchanged from template
- ✓ Industries displayed as pills in 2×2 grid
- ✓ Vendor names bold in Technographic Fit boxes
- ✓ All purple icons and branding intact
- ✓ File opens without errors in PowerPoint/Keynote/Google Slides

## Example Usage

**User Input:**
```
From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Kaspersky XDRO

We need ICPs for Kaspersky's Extended Detection and Response Offering (XDRO)
targeting mid-market financial services firms in North America.

Products: Kaspersky XDRO, Kaspersky Endpoint Security
Target: Financial services, healthcare, retail
Use case: Competitive displacement of CrowdStrike and SentinelOne
```

**Stage 1 Output**: Markdown with 3+ validated ICPs

**Stage 2 Output**: Branded PowerPoint deck with:
- Slide 1: "Kaspersky XDRO Campaign - 2025"
- Slide 2: "Kaspersky" (text)
- Slides 3-4: Static GTM Fabric content
- Slides 5-7: 3 ICP slides with populated content

## Error Handling

**If web research fails:**
- Retry search with alternative query
- If still failing, inform user and request manual input
- Never generate fictional vendor names

**If template not found:**
- Inform user that template file is required
- Provide path: `resources/demandscience_icp_salesdeck_example_pptx_output.pptx`

**If user hasn't approved Markdown:**
- Do not proceed to Stage 2
- Explicitly wait for user confirmation

## Performance Expectations

- Stage 1 (Research & Markdown): 2-3 minutes
- Stage 2 (PowerPoint): 1-2 minutes
- **Total workflow**: Under 10 minutes ✅

## Notes

- This is a Phase 1 implementation (text-based Slide 2)
- Phase 2 will add automated logo discovery with user validation
- Template cloning preserves all vector graphics and branding
- Static slides (3-4) are never modified to maintain GTM Fabric brand consistency
```

#### Step 3: Create REFERENCE.md (Optional)

**File**: `demandscience-icp-skill/REFERENCE.md`

**Content**: Template analysis details, placeholder mapping, content transformation rules (from `pptx_template_analysis.md`)

#### Step 4: Create EXAMPLES.md (Optional)

**File**: `demandscience-icp-skill/EXAMPLES.md`

**Content**: Example email briefs, expected Markdown outputs, sample PowerPoint structures

#### Step 5: Add Template to Resources

```bash
cp demandscience_icp_salesdeck_example_pptx_output.pptx demandscience-icp-skill/resources/
```

---

### Phase 2: Skill Upload & Testing

#### Step 1: Create Upload Script

**File**: `upload_skill.py`

```python
import os
from pathlib import Path
from anthropic import Anthropic
from anthropic.lib import files_from_dir
from dotenv import load_dotenv

# Load environment
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=API_KEY)

# Skill directory
SKILL_DIR = Path(__file__).parent / "demandscience-icp-skill"

def create_skill():
    """Upload the DemandScience ICP skill."""
    try:
        skill = client.beta.skills.create(
            display_title="DemandScience ICP & Sales Deck Generator",
            files=files_from_dir(str(SKILL_DIR))
        )

        print("✅ Skill uploaded successfully!")
        print(f"   Skill ID: {skill.id}")
        print(f"   Display Title: {skill.display_title}")
        print(f"   Version: {skill.latest_version}")
        print(f"   Created: {skill.created_at}")

        # Save skill ID for future use
        with open("skill_id.txt", "w") as f:
            f.write(skill.id)

        return skill.id

    except Exception as e:
        print(f"❌ Upload failed: {e}")
        return None

if __name__ == "__main__":
    skill_id = create_skill()
```

#### Step 2: Create Test Script

**File**: `test_skill.py`

```python
import os
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment
load_dotenv()
API_KEY = os.getenv("ANTHROPIC_API_KEY")
client = Anthropic(api_key=API_KEY)

# Load skill ID
with open("skill_id.txt") as f:
    SKILL_ID = f.read().strip()

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)

def extract_file_ids(response):
    """Extract file IDs from response."""
    file_ids = []
    for content in response.content:
        if hasattr(content, 'type') and content.type == 'bash_code_execution_tool_result':
            if hasattr(content, 'content') and content.content:
                for item in content.content:
                    if hasattr(item, 'file_id') and item.file_id:
                        file_ids.append(item.file_id)
    return file_ids

def download_file(client, file_id, output_dir, prefix=""):
    """Download a single file."""
    try:
        metadata = client.beta.files.retrieve_metadata(file_id)
        filename = f"{prefix}{metadata.filename}"
        output_path = output_dir / filename

        file_content = client.beta.files.download(file_id)
        with open(output_path, 'wb') as f:
            f.write(file_content.read())

        print(f"✅ Downloaded: {filename} ({metadata.size_bytes} bytes)")
        return output_path

    except Exception as e:
        print(f"❌ Download failed: {e}")
        return None

# Test email brief
test_email = """
From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Vena Solutions

We need ICPs for Vena Solutions targeting finance teams in mid-market companies.

Products: Vena Complete Planning Platform
Target Industries: Technology, Manufacturing, Professional Services
Use Case: Replacing legacy Excel-based planning and Oracle/SAP EPM systems
Region: North America

Please generate ICPs for this campaign.
"""

print("=" * 70)
print("STAGE 1: ICP Research & Markdown Generation")
print("=" * 70)
print("\n⏱️ Expected time: 2-3 minutes\n")

# Stage 1: Generate ICPs in Markdown
stage1_response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": SKILL_ID, "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": test_email}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02"
    ]
)

# Print Markdown output
print("\nStage 1 Response:")
print("=" * 70)
for content in stage1_response.content:
    if content.type == "text":
        print(content.text)

print("\n" + "=" * 70)
print("Please review the ICPs above and approve to continue to Stage 2")
print("=" * 70)

# In production, wait for user approval here
# For testing, we'll proceed automatically

print("\n" + "=" * 70)
print("STAGE 2: PowerPoint Generation")
print("=" * 70)
print("\n⏱️ Expected time: 1-2 minutes\n")

# Extract markdown from Stage 1
markdown_content = ""
for content in stage1_response.content:
    if content.type == "text":
        markdown_content = content.text
        break

# Stage 2: Convert to PowerPoint
stage2_prompt = f"""
The user has approved the following ICPs. Please convert them to a branded PowerPoint presentation following the GTM Fabric template specifications.

Approved ICPs:
{markdown_content}

Campaign Details:
- DemandScience Customer: Vena Solutions
- Products: Vena Complete Planning Platform
- Campaign Goal: Target finance teams replacing legacy Excel and EPM systems
- Year: 2025

Generate the PowerPoint deck with:
- Slide 1: Campaign cover slide
- Slide 2: "Vena Solutions" as text (Phase 1 implementation)
- Slides 3-4: Static GTM Fabric content (copy unchanged from template)
- Slides 5+: One slide per ICP (minimum 3)

Apply all GTM Fabric branding specifications.
"""

stage2_response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": SKILL_ID, "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
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

# Print Stage 2 response
print("\nStage 2 Response:")
print("=" * 70)
for content in stage2_response.content:
    if content.type == "text":
        print(content.text)

# Download PowerPoint file
file_ids = extract_file_ids(stage2_response)
if file_ids:
    print("\n" + "=" * 70)
    print("Downloading PowerPoint file...")
    print("=" * 70)

    for file_id in file_ids:
        download_file(client, file_id, OUTPUT_DIR, prefix="vena_icp_deck_")

    print("\n✅ Test complete! Check outputs/ directory for PowerPoint file.")
else:
    print("\n⚠️ No files generated. Check response for errors.")

print("\n" + "=" * 70)
print("Token Usage:")
print(f"  Stage 1: {stage1_response.usage.input_tokens} in, {stage1_response.usage.output_tokens} out")
print(f"  Stage 2: {stage2_response.usage.input_tokens} in, {stage2_response.usage.output_tokens} out")
print(f"  Total: {stage1_response.usage.input_tokens + stage2_response.usage.input_tokens} in, {stage1_response.usage.output_tokens + stage2_response.usage.output_tokens} out")
print("=" * 70)
```

---

### Phase 3: Integration into PRD & Tech Spec

#### Updates to PRD

**Section to Add**: Implementation Requirements

```markdown
## Implementation Requirements (Based on Claude Skills Best Practices)

### API Configuration

**Required Beta Namespace:**
- Use `client.beta.messages.create()` (not `client.messages.create()`)
- Include all three beta flags: `code-execution-2025-08-25`, `files-api-2025-04-14`, `skills-2025-10-02`
- Code execution tool REQUIRED: `tools=[{"type": "code_execution_20250825", "name": "code_execution"}]`

**Skill Container:**
```python
container={
    "skills": [
        {"type": "custom", "skill_id": "demandscience-icp-skill-id", "version": "latest"},
        {"type": "anthropic", "skill_id": "pptx", "version": "latest"}  # Stage 2 only
    ]
}
```

### File Handling

**Download Pattern:**
- Use `client.beta.files.download(file_id).read()` (not `.content`)
- Use `metadata.size_bytes` (not `.size`)
- Download files immediately after generation

### Performance Expectations

- Stage 1 (ICP Research & Markdown): 2-3 minutes
- Stage 2 (PowerPoint Generation): 1-2 minutes
- Total workflow: Under 10 minutes ✅
- Token efficiency: ~90% reduction vs. manual prompting

### Skill Structure

**Directory Layout:**
```
demandscience-icp-skill/
├── SKILL.md              # Main instructions (< 5,000 tokens)
├── REFERENCE.md          # Template documentation
├── EXAMPLES.md           # Usage examples
└── resources/
    └── demandscience_icp_salesdeck_example_pptx_output.pptx
```

**YAML Frontmatter:**
- name: `demandscience-icp-salesdeck` (64 chars max, lowercase-hyphens)
- description: Brief summary (1024 chars max)
```

#### Updates to Tech Spec

**Section to Add**: API Implementation Details

```markdown
## API Implementation Details

### Stage 1: ICP Generation API Call

```python
from anthropic import Anthropic

client = Anthropic(api_key=API_KEY)

# Generate ICPs in Markdown format
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

# Extract Markdown from response
markdown_icps = ""
for content in response.content:
    if content.type == "text":
        markdown_icps = content.text
        break
```

### Stage 2: PowerPoint Generation API Call

```python
# After user approves Markdown, generate PowerPoint
pptx_response = client.beta.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "custom", "skill_id": SKILL_ID, "version": "latest"},
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": stage2_prompt_with_approved_markdown}],
    betas=[
        "code-execution-2025-08-25",
        "files-api-2025-04-14",
        "skills-2025-10-02"
    ]
)

# Download PowerPoint file
def extract_file_ids(response):
    file_ids = []
    for content in response.content:
        if hasattr(content, 'type') and content.type == 'bash_code_execution_tool_result':
            if hasattr(content, 'content') and content.content:
                for item in content.content:
                    if hasattr(item, 'file_id') and item.file_id:
                        file_ids.append(item.file_id)
    return file_ids

file_ids = extract_file_ids(pptx_response)
for file_id in file_ids:
    metadata = client.beta.files.retrieve_metadata(file_id)
    file_content = client.beta.files.download(file_id)

    with open(f"outputs/{metadata.filename}", 'wb') as f:
        f.write(file_content.read())  # Use .read(), not .content

    print(f"Downloaded: {metadata.filename} ({metadata.size_bytes} bytes)")
```

### Error Handling

**File Download Errors:**
```python
try:
    file_content = client.beta.files.download(file_id)
    with open(output_path, 'wb') as f:
        f.write(file_content.read())
except Exception as e:
    print(f"Download failed: {e}")
    # Retry logic or user notification
```

**Skill Not Found:**
```python
try:
    response = client.beta.messages.create(...)
except Exception as e:
    if "skill not found" in str(e).lower():
        print("Skill needs to be uploaded. Run upload_skill.py")
    else:
        raise e
```

### Token Usage Tracking

```python
print(f"Stage 1 Tokens: {response.usage.input_tokens} in, {response.usage.output_tokens} out")
print(f"Stage 2 Tokens: {pptx_response.usage.input_tokens} in, {pptx_response.usage.output_tokens} out")
print(f"Total: {response.usage.input_tokens + pptx_response.usage.input_tokens} tokens")
```

Expected: ~90% fewer tokens than manual prompting with full template specifications.
```

---

## Part 3: Testing & Validation Checklist

### Pre-Upload Validation

- [ ] SKILL.md exists with valid YAML frontmatter
- [ ] name field: lowercase-hyphens, ≤ 64 chars
- [ ] description field: ≤ 1024 chars
- [ ] Instructions: ≤ 5,000 tokens (estimated)
- [ ] Template file exists in resources/ directory
- [ ] All referenced files present in skill directory

### Upload Validation

- [ ] Skill uploads without errors
- [ ] Skill ID returned and saved
- [ ] display_title matches expectation
- [ ] latest_version = 1

### Stage 1 Testing (ICP Generation)

- [ ] Email brief correctly parsed
- [ ] Web research executed (verify via response content)
- [ ] Minimum 3 ICPs generated
- [ ] All vendor names are real/validated (not placeholders)
- [ ] Markdown format correct
- [ ] User review prompt displayed
- [ ] Generation time ≤ 3 minutes

### Stage 2 Testing (PowerPoint Generation)

- [ ] User approval workflow implemented
- [ ] PowerPoint file generated
- [ ] File downloads successfully
- [ ] File opens in PowerPoint without errors
- [ ] Slide 1 populated correctly
- [ ] Slide 2 has customer name as text
- [ ] Slides 3-4 unchanged from template
- [ ] Minimum 3 ICP slides present
- [ ] All placeholders replaced
- [ ] Branding intact (colors, fonts, icons)
- [ ] Industries displayed as pills (2×2 grid)
- [ ] Vendor names bold in Technographic Fit boxes
- [ ] Generation time ≤ 2 minutes

### End-to-End Workflow

- [ ] Total workflow ≤ 10 minutes
- [ ] Token usage tracked and reasonable
- [ ] Error handling works (missing template, failed research, etc.)
- [ ] File naming consistent
- [ ] Output directory structure correct

### Quality Assurance (per QA Testing Plan)

- [ ] Golden test cases executed (Vena, Kaspersky, Autodesk)
- [ ] Format checks pass (Markdown structure, PPTX validation)
- [ ] Consistency check (same input = same structure)
- [ ] Real-world validation (actual DemandScience emails)
- [ ] Feedback logged

---

## Part 4: Production Deployment Checklist

### Environment Setup

- [ ] API key configured in .env
- [ ] Python environment with anthropic SDK ≥ 0.71.0
- [ ] Output directory created
- [ ] Logging configured

### Skill Deployment

- [ ] Skill uploaded to production workspace
- [ ] Skill ID stored securely
- [ ] Version documented (v1)
- [ ] Skill tested in production environment

### Monitoring

- [ ] Token usage tracking enabled
- [ ] Error logging configured
- [ ] Performance metrics collected (generation times)
- [ ] User feedback mechanism in place

### Documentation

- [ ] README with usage instructions
- [ ] API examples documented
- [ ] Error messages documented
- [ ] Troubleshooting guide created

### Maintenance

- [ ] Git repository initialized
- [ ] .gitignore configured (exclude .env, outputs/, skill_id.txt)
- [ ] Version control workflow established
- [ ] Skill versioning strategy defined

---

## Part 5: Future Enhancements (Phase 2)

### Automated Logo Discovery

**Implementation Approach:**
```python
# Phase 2: Logo discovery and insertion
def discover_logo(customer_name):
    """Web search for company logo."""
    search_results = web_search(f"{customer_name} logo png transparent")
    logos = validate_logos(search_results)

    if logos:
        # Show user preview
        approved_logo = user_approval_workflow(logos)
        return approved_logo
    else:
        # Fallback to Phase 1 (text)
        return None

# In Stage 2 prompt:
logo_path = discover_logo("Vena Solutions")
if logo_path:
    # Insert logo image into Slide 2
    insert_logo_to_slide(pptx_file, slide_2, logo_path)
else:
    # Use text (Phase 1 behavior)
    insert_text_to_slide(pptx_file, slide_2, "Vena Solutions")
```

**Additional Time**: +30-60 seconds per workflow
**Additional Complexity**: Medium (image validation, user approval UI)
**Estimated Development**: +4-6 hours

---

## Summary

**This implementation plan provides:**

✅ Complete API patterns from Claude Skills best practices
✅ Step-by-step skill creation guide
✅ Upload and testing scripts
✅ PRD and tech spec update specifications
✅ Comprehensive testing checklist
✅ Production deployment readiness
✅ Phase 2 enhancement roadmap

**Next Steps:**

1. Review this plan with team
2. Create skill directory structure
3. Write SKILL.md content
4. Upload skill and test with golden test cases
5. Update PRD and tech spec with API implementation details
6. Deploy to production

**Estimated Timeline:**

- Skill creation: 3-4 hours
- Testing and refinement: 2-3 hours
- Documentation updates: 1-2 hours
- **Total: 6-9 hours** ✅ (matches original estimate)
