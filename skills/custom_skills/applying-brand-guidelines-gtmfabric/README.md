# GTM Fabric Design System - applying-brand-guidelines-gtmfabric

A comprehensive design system skill for creating professional, modern presentations and web applications with GTM Fabric branding.

## Overview

This skill provides:
- **ICP Cards Visual Design System** for React/TypeScript web applications
- **PowerPoint Generation** for creating modern, sleek ICP presentations
- **Design Tokens** for consistent colors, typography, and spacing
- **GTM Fabric Branding** with automatic logo integration

## Features

### Web Design System (React/TypeScript)

- Dark purple theme (#06040f background, #c084fc accent)
- Mobile-first responsive patterns
- Arial font family
- Component patterns for cards, badges, headers, funnels
- Accessibility-compliant color contrast ratios
- Animation system with reduced-motion support

### PowerPoint Generation (Python)

- Modern card-based slide layouts
- Automatic GTM Fabric logo placement
- ICP-specific slide templates
- Dark theme with high-contrast text
- Professional typography and spacing
- JSON-to-PPTX conversion

## Quick Start

### PowerPoint Generation

```python
from pptx_generator import GTMFabricPresentationGenerator

# Initialize generator
generator = GTMFabricPresentationGenerator()
prs = generator.create_presentation()

# Create title slide
generator.create_title_slide(
    prs,
    title="Your Company - Ideal Customer Profiles",
    subtitle="Platform GTM Campaign",
    date="January 2025"
)

# Create ICP slide
generator.create_icp_slide(
    prs,
    icp_number=1,
    icp_title="Enterprise Buyer",
    industries=["Manufacturing", "Retail"],
    departments="Finance, IT, Operations",
    key_roles=["CFO", "CIO", "VP Operations"],
    displacement_signals=[{
        "pain_explanation": "Legacy systems causing inefficiency",
        "vendor_products": ["Oracle", "SAP"]
    }],
    expansion_signals=[{
        "readiness_explanation": "Modern cloud infrastructure",
        "vendor_products": ["AWS", "Azure"]
    }]
)

# Save
generator.save_presentation(prs, "output.pptx")
```

### Generate from JSON

```python
from pptx_generator import generate_icp_presentation
import json

with open('icps.json', 'r') as f:
    data = json.load(f)

generate_icp_presentation(
    campaign_info=data['campaign_info'],
    icps=data['icps'],
    output_path='client-icps.pptx'
)
```

## File Structure

```
applying-brand-guidelines-gtmfabric/
├── SKILL.md                    # Comprehensive design system documentation
├── README.md                   # This file
├── REFERENCE.md                # Quick reference guide
├── apply_brand.py              # Design tokens and utilities (Python)
├── validate_brand.py           # React/Tailwind code validator
├── pptx_generator.py          # PowerPoint generation module
├── example_usage.py           # Usage examples
├── gtmfabric_logo_white.png   # GTM Fabric logo for dark backgrounds
├── gtmfabric_logo_black.png   # GTM Fabric logo for light backgrounds
└── example-*.pptx             # Example presentations
```

## Design System Colors

### Background Colors (Dark Theme)
- **Background**: `#06040f` - Deep purple-black base
- **Card**: `#120a1f` - Elevated card background
- **Sidebar**: `#0e0817` - Sidebar background

### Text Colors
- **Primary Text**: `#f2f2f2` - Main content (95% white)
- **Secondary Text**: `#a6a6a6` - Supporting content (65% white)

### Accent & Borders
- **Primary Accent**: `#c084fc` - Light purple
- **Default Border**: `#3a2d4f`
- **Card Border**: `#261b35`

## Typography

- **Font Family**: Arial
- **Fallback**: Calibri → sans-serif
- **Weights**: 400 (regular), 500 (medium), 600 (semibold)

### Sizes (Mobile → Desktop)
- **H1**: 20px → 30px
- **H2**: 24px → 36px
- **H3**: 16px
- **Body**: 14px
- **Small**: 12px

## Slide Templates

### 1. Title Slide
- Large title with modern accent bar
- Subtitle in accent color
- Optional date
- GTM Fabric logo (top-right)

### 2. Content Slide
- Card-based content area
- Section headers in accent color
- Bullet points or plain text
- Page numbers

### 3. ICP Slide
- ICP badge (pill design)
- Industries section
- Departments & key roles
- Technographic fit:
  - Displacement / Modernization Signals
  - Expansion Signals
- Vendor products with arrow notation (→)

## Requirements

```bash
pip install python-pptx
```

## Examples

Run the example script to see all features:

```bash
python3 example_usage.py
```

This creates three example presentations:
1. `example-basic.pptx` - Basic title and content slides
2. `example-icp.pptx` - Complete ICP presentation
3. `example-from-json.pptx` - Generated from JSON data

## Usage in DemandScience ICP Creation Skill

This skill is designed to be used by the `demandscience-icp-creation-ppxt` skill to generate professional ICP presentations:

```python
# In demandscience-icp-creation-ppxt skill
import sys
sys.path.insert(0, '/path/to/applying-brand-guidelines-gtmfabric')

from pptx_generator import generate_icp_presentation

# Generate presentation from ICP data
generate_icp_presentation(
    campaign_info=campaign_info,
    icps=icps,
    output_path='client-icps.pptx'
)
```

## Customization

### Logo Positioning
```python
generator._add_logo(slide, position="top-right", size=0.8)
# Options: "top-right", "top-left", "bottom-right", "bottom-left"
```

### Custom Colors
```python
from pptx_generator import GTMFabricColors
from pptx.dml.color import RGBColor

colors = GTMFabricColors()
colors.accent = RGBColor(200, 150, 250)  # Custom purple
```

### Slide Dimensions
```python
# 16:9 standard (default)
prs = generator.create_presentation(slide_width=10, slide_height=5.625)

# 4:3 traditional
prs = generator.create_presentation(slide_width=10, slide_height=7.5)
```

## Design Guidelines

When creating presentations:

1. **Keep text concise** - Executive-ready content
2. **Use bullet points** - Max 3-5 bullets per section
3. **Highlight vendor names** - Products after arrow (→)
4. **Maintain hierarchy** - Headers use accent color
5. **Include page numbers** - For multi-slide presentations
6. **Test on target platform** - PowerPoint or Keynote

## Best Practices

1. **Validate JSON structure** before generating
2. **Keep vendor lists concise** (2-3 products per signal)
3. **Use descriptive ICP titles** that identify the persona
4. **Test generated files** before sharing
5. **Verify logo renders** on all slides

## Accessibility

- **Color Contrast**: 16:1 ratio for primary text (AAA), 7:1 for secondary (AA)
- **Font Size**: Minimum 14px for body text
- **Touch Targets**: 44px minimum for interactive elements
- **Focus Indicators**: 2px solid accent with 2px offset
- **Reduced Motion**: Animations respect `prefers-reduced-motion`

## Troubleshooting

### Logo not appearing
- Check `gtmfabric_logo_white.png` exists in skill directory
- Verify file permissions
- Try full path: `GTMFabricPresentationGenerator(logo_path="/full/path")`

### Font not displaying correctly
- Arial is the default font
- Falls back to Calibri → sans-serif

### Text overflow
- Reduce content length
- Use shorter vendor product names
- Break long text into multiple bullets

## Version History

- **1.0.0** (November 2025) - Initial release
  - ICP Cards design system
  - PowerPoint generation module
  - GTM Fabric logo integration
  - Example presentations

## License

This design system is proprietary to GTM Fabric.

## Support

For questions or issues:
- Review `SKILL.md` for comprehensive documentation
- Check `REFERENCE.md` for quick reference
- Run `example_usage.py` for working examples
- Review generated example presentations

---

**Framework**: React + TypeScript (Web) | Python (PowerPoint)
**Styling**: Tailwind CSS + CSS Custom Properties (Web) | python-pptx (PowerPoint)
**Font**: Arial
**Version**: 1.0.0 (November 2025)
