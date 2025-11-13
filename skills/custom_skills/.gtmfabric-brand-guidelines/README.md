# GTM Fabric Brand Guidelines Skill

A simplified, documentation-based brand guidelines skill for GTM Fabric. This skill works with Claude's built-in document generation skills to apply consistent GTM Fabric branding.

## Overview

This skill provides **brand guidelines only** - no custom code required. Claude reads these guidelines and applies them when generating documents using its built-in `pptx`, `pdf`, or `xlsx` skills.

## Philosophy: Simple > Complex

Unlike traditional custom skills that include complex Python code for document generation, this skill follows the **documentation-based pattern**:

- ✅ **SKILL.md**: Comprehensive brand guidelines
- ✅ **REFERENCE.md**: Quick reference guide
- ✅ **Logo assets**: GTM Fabric logos (white & black versions)
- ❌ **No custom code**: Claude's built-in skills handle generation
- ❌ **No dependencies**: No python-pptx, reportlab, or other libraries
- ❌ **No maintenance**: Just update guidelines as brand evolves

## File Structure

```
gtmfabric-brand-guidelines/
├── SKILL.md                     # Comprehensive brand guidelines (~12 KB)
├── REFERENCE.md                 # Quick reference card (~6 KB)
├── README.md                    # This file
├── gtmfabric_logo_white.png    # Logo for dark backgrounds (256 KB)
└── gtmfabric_logo_black.png    # Logo for light backgrounds (266 KB)

Total: ~550 KB (vs 682 KB with custom code)
```

## How It Works

### 1. Claude Reads the Guidelines

When you reference this skill, Claude automatically reads `SKILL.md` and understands:
- GTM Fabric color palette (#06040f dark theme, #c084fc accent)
- Typography (Arial, specific sizes)
- Logo placement rules
- ICP presentation structure
- Vendor/product formatting (→ arrow notation)

### 2. Claude's Built-in Skills Generate Documents

Claude uses its native document generation capabilities:
- `pptx` skill → PowerPoint presentations
- `pdf` skill → PDF documents
- `xlsx` skill → Excel spreadsheets

### 3. No Custom Code Required

You don't write Python. You write **prompts**:

```python
from anthropic import Anthropic

client = Anthropic()

response = client.beta.messages.create(
    betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    container={
        "skills": [
            {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
        ]
    },
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{
        "role": "user",
        "content": """Create a PowerPoint presentation with GTM Fabric branding for these ICPs:

[ICP content here]

Apply gtmfabric-brand-guidelines:
- Dark theme (#06040f background)
- Accent purple (#c084fc) for headers
- GTM Fabric logo on all slides
- Bold vendor names with → arrows
- Arial font throughout
"""
    }]
)
```

## Usage Examples

### Example 1: ICP Presentation

```python
# Simple prompt-based approach
prompt = f"""Create a GTM Fabric ICP presentation:

**Client**: Kaspersky
**Campaign**: Enterprise Security Platform
**Date**: January 2025

## ICP #1: Enterprise Security Modernization Buyer

**Industries**: Financial Services, Healthcare, Manufacturing

**Departments**: IT Security, Infrastructure, Compliance

**Key Roles**:
- CISO
- VP IT
- Security Director

**Displacement Signals**:
Pain: Legacy endpoint security causing compliance risks
Replacing: McAfee → ePO, Symantec → Endpoint Protection, Trend Micro → Apex One

**Expansion Signals**:
Readiness: Recent cloud migration creating security gaps
Using: Microsoft → Azure, AWS, Okta

Apply gtmfabric-brand-guidelines for all branding.
"""

response = client.beta.messages.create(
    betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"],
    model="claude-sonnet-4-5-20250929",
    max_tokens=4096,
    container={"skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]},
    tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
    messages=[{"role": "user", "content": prompt}]
)
```

### Example 2: Reference Brand Guidelines

```python
# Claude can read and apply guidelines from this skill
prompt = """Review the gtmfabric-brand-guidelines and summarize:
1. What colors should I use?
2. What font is standard?
3. How should I format vendor/product names?
"""

# Claude will read SKILL.md and provide accurate answers
```

## Brand Guidelines Summary

### Colors
- **Background**: #06040f (Deep purple-black)
- **Card**: #120a1f (Elevated surfaces)
- **Accent**: #c084fc (Headers, highlights)
- **Primary Text**: #f2f2f2 (95% white)
- **Secondary Text**: #a6a6a6 (65% white)

### Typography
- **Font**: Arial (Calibri fallback)
- **H1**: 30pt, Bold
- **H2**: 24pt, Semibold
- **Body**: 14pt, Regular

### Logo
- **White version** (`gtmfabric_logo_white.png`) on dark backgrounds (primary)
- **Black version** (`gtmfabric_logo_black.png`) on light backgrounds (rare)
- **Placement**: Top-right, 0.8 inches width

### Vendor Formatting
- **Always bold**: **Salesforce** → **Sales Cloud**
- **Arrow notation**: Use → between vendor and product
- **Be specific**: Include product names, not just vendor

## ICP Slide Structure

Every ICP slide must include:

1. **ICP Badge**: "ICP #1: [Title]"
2. **Industries**: Comma-separated list
3. **Departments**: List or comma-separated
4. **Key Roles**: Job titles (CISO, VP IT, etc.)
5. **Technographic Fit**:
   - **Displacement Signals**: Pain + products to replace
   - **Expansion Signals**: Readiness + products they use

## Integration with DemandScience Workflow

Use this skill in your `demandscience-icp-salesdeck-workflow`:

```python
# Phase 1: Research & generate ICPs (Markdown)
# [Your research code here]

# Phase 2: Convert approved Markdown to PowerPoint
def generate_branded_powerpoint(icp_markdown: str, campaign_info: dict):
    prompt = f"""Create a GTM Fabric branded PowerPoint:

**Client**: {campaign_info['client_name']}
**Campaign**: {campaign_info['campaign_type']}
**Date**: {campaign_info['date']}

{icp_markdown}

Apply gtmfabric-brand-guidelines:
- Dark theme with purple accents
- GTM Fabric logo on all slides
- Bold vendor/product names with → arrows
- Card-based ICP slide layouts
- All 5 required ICP sections
"""

    response = client.beta.messages.create(
        betas=["code-execution-2025-08-25", "files-api-2025-04-14", "skills-2025-10-02"],
        model="claude-sonnet-4-5-20250929",
        max_tokens=4096,
        container={"skills": [{"type": "anthropic", "skill_id": "pptx", "version": "latest"}]},
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
        messages=[{"role": "user", "content": prompt}]
    )

    return response
```

## Advantages Over Custom Code Approach

| Aspect | This Skill (Simple) | Custom Code Skill (Complex) |
|--------|--------------------|-----------------------------|
| **File Size** | ~550 KB | ~682 KB |
| **Code Files** | 0 Python files | 5 Python files (152 KB total) |
| **Dependencies** | None | python-pptx, reportlab, etc. |
| **Maintenance** | Update guidelines only | Debug code, fix bugs |
| **Flexibility** | Claude adapts to content | Fixed templates |
| **Updates** | Edit SKILL.md | Rewrite Python code |
| **Learning Curve** | Read guidelines | Learn custom API |

## Updating Brand Guidelines

To update branding:

1. **Colors**: Edit color codes in `SKILL.md` and `REFERENCE.md`
2. **Typography**: Update font family and sizes in both files
3. **Logo**: Replace PNG files (maintain aspect ratio)
4. **Guidelines**: Add/modify sections in `SKILL.md`

No code changes required!

## Best Practices

1. **Reference the skill explicitly** in prompts: "Apply gtmfabric-brand-guidelines"
2. **Be specific** about requirements: "Dark theme, Accent Purple headers, logo top-right"
3. **Include structure**: Specify ICP sections, vendor format, etc.
4. **Verify output**: Check colors, fonts, logo placement
5. **Iterate**: Claude can adjust based on feedback

## Troubleshooting

### Logo not appearing
- Ensure PNG files are in the skill directory
- Reference the skill in your prompt
- Specify: "Include GTM Fabric logo (gtmfabric_logo_white.png) on all slides"

### Wrong colors
- Be explicit: "Use GTM Fabric colors: #06040f background, #c084fc accent"
- Reference: "Apply gtmfabric-brand-guidelines color palette"

### Wrong font
- Specify: "Use Arial font family as defined in gtmfabric-brand-guidelines"

### Missing ICP sections
- List all 5 required sections in your prompt
- Reference: "Follow ICP slide structure from gtmfabric-brand-guidelines"

## Version History

- **1.0.0** (November 2025) - Initial simplified skill
  - Brand guidelines documentation
  - Quick reference card
  - Logo assets
  - No custom code approach

## License

This design system is proprietary to GTM Fabric.

## Support

For questions:
- Review `SKILL.md` for comprehensive guidelines
- Check `REFERENCE.md` for quick reference
- Ensure logo files are present in skill directory

---

**Skill Type**: Documentation-based (no custom code)
**Works With**: Claude's built-in `pptx`, `pdf`, `xlsx` skills
**Font**: Arial (Calibri fallback)
**Theme**: Dark purple (#06040f) with accent purple (#c084fc)
**Version**: 1.0.0 (November 2025)
