# Tech Spec Update Content
## Ready-to-Integrate Specifications

This document contains the exact content to replace placeholders in `tech_spec.md` based on template analysis.

---

## 1. Replace "GTM Fabric Branding Requirements" Placeholder

**Location**: tech_spec.md, Section "## GTM Fabric Branding Requirements"

**Replace This**:
```markdown
**[PLACEHOLDER: TO BE UPDATED AFTER REVERSE ENGINEERING GTM FABRIC PPTX TEMPLATE]**

This section will include:
- Color palette specifications
- Typography guidelines
- Logo usage and placement rules
- Slide layout requirements
- Custom skill implementation details

These specifications will be extracted from the GTM Fabric branded PowerPoint template.
```

**With This**:

```markdown
### Slide Dimensions
- **Format**: Widescreen (16:9 aspect ratio)
- **Size**: 20.00" × 11.25"

### Color Palette

**Extracted from PPTX File Analysis:**

| Color Name | RGB Values | Hex Code | Usage |
|------------|------------|----------|-------|
| **Slide Background** | RGB(244, 246, 251) | #F4F6FB | Overall slide background (Light Blue-Gray) |
| **Primary Purple** | RGB(50, 3, 97) | #320361 | Section icons, slide titles, circular icons |
| **Medium Gray** | RGB(153, 153, 153) | #999999 | Industry pill backgrounds (2×2 grid) |
| **White** | RGB(255, 255, 255) | #FFFFFF | Icon backgrounds, Technographic Fit boxes |
| **Black** | RGB(0, 0, 0) | #000000 | Technographic Fit box accents/borders |
| **Dark Blue-Gray** | RGB(40, 45, 73) | #282D49 | Text color (body text, descriptions) |

**Note:** The slide background #F4F6FB may appear lavender/cream in PDFs or certain displays.

### Typography

| Element | Font | Size | Weight | Color |
|---------|------|------|--------|-------|
| Cover Header | Arial | 80pt | Regular | Primary Purple (#320361) |
| Cover Subheader | Arial Bold | 74pt | Bold | Primary Purple (#320361) |
| Slide Titles | Arial | 36pt | Regular | Primary Purple (#320361) |
| Section Headers | Arial | 18pt | Regular | Dark Blue-Gray (#282D49) |
| Body Text / Bullets | Arial | 14pt | Regular | Dark Blue-Gray (#282D49) |
| Descriptions | Arial | 22pt | Regular | Dark Blue-Gray (#282D49) |

### Template Structure (5 Slides)

**Slide 1**: Cover Slide
- Campaign title page with Header, Subheader, Description, Year

**Slide 2**: Cover Slide with Target Account Logo
- Alternative cover with customer branding placeholder

**Slide 3**: Key Elements for E2E Solutions
- GTM Fabric value proposition (4 quadrants)
- Fixed content showing GTM Fabric's service offerings

**Slide 4**: Propensity Funnel
- Market segmentation methodology visualization
- TAM-SAM-SOM framework display

**Slide 5**: ICP Template (Repeatable for each ICP)
- This slide is duplicated for each ICP generated
- Contains all ICP content sections (see below)

### Slide 5 - ICP Template Layout

**Top Bar:**
- Left: Purple icon + ICP Title (36pt, Purple)
- Right: GTM Fabric branding

**Left Column** (Cream/off-white background cards):

1. **Industries Section**
   - Purple circular icon (factory/building symbol)
   - Section header: "Industries" (18pt)
   - **Unique pill/chip design**: 4 rounded pills in 2×2 grid
   - Light gray pill backgrounds with rounded corners
   - Placeholder: `{industry value}` × 4

2. **Departments & Functions Section**
   - Purple circular icon (gear/cog symbol)
   - Section header: "Departments & Functions" (18pt)
   - Simple list format (not pills)
   - Placeholder: `{department value}` × 3

3. **Key Roles Section**
   - Purple circular icon (people/user symbol)
   - Section header: "Key Roles" (18pt)
   - Simple list format (not pills)
   - Placeholder: `{role value}` × 3

**Right Column** (White boxes with light borders):

4. **Technographic Fit Section**
   - Purple circular icon (bar chart/analytics symbol)
   - Section header: "Technographic Fit" (18pt)

   **Upper Box**:
   - Gray subheader: "Displacement / Modernization Signals"
   - Placeholder: `{displacement modernization signal value}` × 4 lines

   **Lower Box**:
   - Gray subheader: "Expansion Signals"
   - Placeholder: `{expansion signal value}` × 4 lines

### Design Elements

**Consistent Across All Slides:**
- Purple circular icons for section headers (unique symbol per section)
- GTM Fabric branding element (top right of slides)
- Cream/off-white card backgrounds for left column sections
- White boxes with subtle borders for right column
- Consistent spacing and typography hierarchy

**Unique to Industries Section:**
- Pill/chip visual treatment (only section with this design)
- 2×2 grid layout for visual impact
- Rounded corners on pills
- Interactive/clickable visual appearance
```

---

## 2. Replace "Stage 2 Output: PowerPoint Presentation" Placeholder

**Location**: tech_spec.md, Section "### Stage 2 Output: PowerPoint Presentation"

**Replace This**:
```markdown
**[PLACEHOLDER: TO BE UPDATED AFTER REVERSE ENGINEERING GTM FABRIC PPTX TEMPLATE]**

After user approval of Markdown ICPs, this section will detail:
- How to call the custom GTM Fabric branded pptx skill
- Slide structure and layout specifications
- Content mapping from Markdown to PowerPoint slides
- Specific formatting and design requirements

This section will be populated once the GTM Fabric pptx template has been reverse engineered and the custom skill has been created.
```

**With This**:

```markdown
After user approves Markdown ICPs, convert them to PowerPoint using the existing template structure:

**File**: `demandscience_icp_salesdeck_example_pptx_output.pptx`

**Deck Structure**:

1. **Slide 1**: Cover slide
   - **Header**: Campaign name or DemandScience customer name
   - **Subheader**: Product(s) being marketed
   - **Description**: Campaign objective/goal
   - **Year**: Current year (e.g., "2025")

2. **Slide 2**: (Optional) Cover with DemandScience customer name/logo
   - **Terminology Note**: `{target account logo}` = DemandScience's customer (e.g., Kaspersky, Vena Solutions)
   - **Phase 1**: Replace placeholder with customer name as text
   - **Phase 2** (Future): Replace with actual logo image
   - Position: Center-right (9.69", 2.95")

3. **Slide 3**: Key Elements for E2E Solutions (STATIC)
   - **Never modified** - GTM Fabric value proposition content
   - Copy as-is from template without any text replacement
   - Shows 4 quadrants of GTM Fabric offerings
   - Header: "Key Elements Required For E2E Use Case Solutions"

4. **Slide 4**: Propensity Funnel (STATIC)
   - **Never modified** - GTM Fabric methodology framework
   - Copy as-is from template without any text replacement
   - Placeholder fields remain unpopulated by this skill
   - Market segmentation visualization

5-N. **Slides 5+**: One slide per ICP
   - Duplicate Slide 5 template for each ICP
   - Minimum 3 ICP slides (per tech spec requirement)

**ICP Slide Content Mapping** (Markdown → PowerPoint):

| Markdown Element | PowerPoint Element | Format Details |
|------------------|-------------------|----------------|
| `## ICP [N]: [Title]` | Top bar title | 36pt Purple, replaces "Descriptive ICP Title" |
| `### Industries` | Industries pill grid | 2×2 pills (4 max), rounded corners, light gray background |
| `[Industry 1, Industry 2, ...]` | `{industry value}` placeholders | Up to 4 industries, comma-separated in Markdown → individual pills |
| `### Departments & Business Functions` | Departments section | Plain text list (3 max) |
| `**Key Job Roles / Job Titles:**` | Key Roles section | Plain text list (3 max) |
| `**Displacement / Modernization Signals:**` | Technographic Fit - Upper box | Format: "Pain → **Vendor**" (4 lines max) |
| `**Expansion Signals:**` | Technographic Fit - Lower box | Format: "Readiness → **Vendor**" (4 lines max) |

**Content Transformation Rules:**

1. **Industries (Markdown → Pills)**:
   - Input: `- Industry1, Industry2, Industry3`
   - Output: 4 pills in 2×2 grid with industry names
   - If < 4 industries: Leave extra pills empty or remove
   - If > 4 industries: Use first 4 or combine related ones

2. **Departments & Roles (List Format)**:
   - Direct text replacement in template placeholders
   - Maximum 3 items each (per template design)
   - If more items: Combine or prioritize top 3

3. **Technographic Signals (Formatted Lists)**:
   - Preserve "→" arrow and **bold vendor names**
   - Each line: `[Pain/Readiness explanation] → **[Vendor Product]**`
   - Maximum 4 lines per box (per template capacity)
   - If more signals: Prioritize most impactful ones

**Placeholder Replacement Strategy:**

```python
# Pseudo-code for population logic
template_placeholders = {
    "Descriptive ICP Title": icp_data['title'],
    "{industry value}": icp_data['industries'][0:4],  # Max 4
    "{department value}": icp_data['departments'][0:3],  # Max 3
    "{role value}": icp_data['roles'][0:3],  # Max 3
    "{displacement modernization signal value}": icp_data['displacement_signals'][0:4],  # Max 4
    "{expansion signal value}": icp_data['expansion_signals'][0:4]  # Max 4
}
```

**Implementation Method:**

**Option A: Template Cloning (Recommended)**
1. Load `demandscience_icp_salesdeck_example_pptx_output.pptx` as base
2. Update Slide 1 with campaign-specific information
3. For each ICP:
   - Duplicate Slide 5 from template
   - Find all placeholder text shapes
   - Replace placeholders with actual ICP content
   - Preserve all formatting, colors, and design elements
4. Delete original Slide 5 (template)
5. Save as new .pptx file

**Option B: Python-pptx Direct Manipulation**
1. Use python-pptx library
2. Iterate through Slide 5 shapes
3. Match shapes by text content (placeholder patterns)
4. Replace text while preserving rich formatting
5. Handle special cases:
   - Industries pills (may be grouped shapes or table cells)
   - Bold vendor names in Technographic Fit boxes
   - Multi-line content in signal boxes

**Required Libraries:**
```bash
pip install python-pptx
```

**Quality Validation:**
- All placeholder text must be replaced (no `{...}` remaining)
- Industries pills must maintain rounded corner design
- Vendor names must be bold in Technographic Fit boxes
- All purple icons and branding elements must be intact
- File must open without errors in PowerPoint, Keynote, and Google Slides
```

---

## 3. Update Evaluation Criteria - Stage 2

**Location**: tech_spec.md, Section "### Stage 2: PowerPoint Generation"

**Replace This**:
```markdown
### Stage 2: PowerPoint Generation
**[PLACEHOLDER: TO BE UPDATED AFTER REVERSE ENGINEERING GTM FABRIC PPTX TEMPLATE]**
- Custom skill implementation validated
- GTM Fabric branding applied correctly
- All ICP content accurately transferred from Markdown
- Slide structure follows template specifications
```

**With This**:

```markdown
### Stage 2: PowerPoint Generation

**Deck Structure:**
- ✓ PowerPoint file uses exact template structure
- ✓ Deck contains 4 fixed slides + N ICP slides (N ≥ 3)
- ✓ Slide 1 (Cover) populated with campaign information
- ✓ Slides 3-4 (GTM Fabric value prop, Propensity Funnel) unchanged from template
- ✓ Slides 5+ (ICP slides) duplicated and populated correctly

**Branding & Design:**
- ✓ All colors match template specifications (Purple #320361, Dark Blue-Gray #282D49)
- ✓ Typography consistent (Arial font family, correct sizes)
- ✓ Purple circular icons intact for all sections
- ✓ GTM Fabric branding elements present on all slides
- ✓ Cream/off-white card backgrounds preserved on left column
- ✓ White boxes with borders preserved on right column
- ✓ Industries pills maintain rounded corner design (2×2 grid)

**Content Transfer Accuracy:**
- ✓ ICP Title correctly placed in top bar
- ✓ Industries (max 4) displayed as pills in 2×2 grid
- ✓ Departments & Functions (max 3) listed correctly
- ✓ Key Roles (max 3) listed correctly
- ✓ Displacement/Modernization Signals (max 4) formatted correctly with arrows and bold vendors
- ✓ Expansion Signals (max 4) formatted correctly with arrows and bold vendors
- ✓ All vendor names in Technographic Fit boxes are **bold**
- ✓ No placeholder text remaining (no `{...}` patterns)

**File Quality:**
- ✓ File opens without errors in Microsoft PowerPoint
- ✓ File opens without errors in Apple Keynote
- ✓ File opens without errors in Google Slides
- ✓ Visual design is indistinguishable from manually populated template
- ✓ All shapes and formatting preserved (no broken elements)
- ✓ File size reasonable (< 10MB for typical 3-7 ICP deck)
```

---

## 4. Add Reference to Template Analysis Document

**Location**: tech_spec.md, After "## Quality Assurance & Testing" section

**Add This New Section**:

```markdown
---

## Template Documentation

For comprehensive PowerPoint template analysis, design specifications, and implementation details, see:

**[PowerPoint Template Analysis](./pptx_template_analysis.md)**

This document includes:
- Complete slide-by-slide breakdown with exact positioning
- Detailed branding specifications (colors, fonts, layouts)
- ICP slide template structure and placeholder mapping
- Visual design insights from template screenshot
- Implementation roadmap and technical approach
- Content transformation rules and best practices
```

---

## Summary of Changes

**Confirmed Findings from Template Analysis:**

✓ Template is complete and ready to use (no modifications needed)
✓ All 5 required sections present on ICP slide:
  - Industries (unique 2×2 pill grid design)
  - Departments & Functions
  - Key Roles
  - Displacement/Modernization Signals
  - Expansion Signals

✓ Placeholder capacity:
  - Industries: 4 values
  - Departments: 3 values
  - Roles: 3 values
  - Displacement Signals: 4 lines
  - Expansion Signals: 4 lines

✓ Branding: Complete purple theme with consistent icons, colors, typography

**Implementation Approach:**
- Clone template and replace placeholders (simplest, preserves design exactly)
- Focus on text replacement only (no template modifications needed)
- Industries pill grid is most complex element (special handling required)

**Estimated Implementation Time:** 4-6 hours for population script + 2-3 hours testing = **6-9 hours total**

**Revised from original estimate of 10-15 hours** (no template modification needed)
