# GTM Fabric Brand Guidelines - Quick Reference

## Theme Selection

GTM Fabric supports **two themes** - specify which one in your prompts:

### Dark Theme (Primary/Default)
- Digital presentations, client ICP decks
- Modern, premium aesthetic
- High visual impact

### Light Theme (Alternative)
- Print documents, PDFs, email attachments
- Better readability in print
- Universal compatibility

## Must-Have Elements

### Dark Theme
✅ GTM Fabric white logo (gtmfabric_logo_white.png)
✅ Deep Purple Black background (#06040f)
✅ Light Accent Purple highlights (#c084fc)
✅ Arial font family
✅ Bold vendor/product names with → arrows

### Light Theme
✅ GTM Fabric black logo (gtmfabric_logo_black.png)
✅ White background (#FFFFFF)
✅ Dark Accent Purple highlights (#8B5CF6)
✅ Arial font family
✅ Bold vendor/product names with → arrows

## Never Use
❌ Wrong logo for theme (white on light, black on dark)
❌ Bright, saturated colors that clash with theme
❌ Non-Arial fonts (except Calibri fallback)
❌ Stretched or distorted logos
❌ Generic vendor references without product names
❌ Missing theme specification in prompts

## Color Reference

### Dark Theme Colors (Primary)
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| Deep Purple Black | #06040f | 6, 4, 15 | Main background |
| Card Purple | #120a1f | 18, 10, 31 | Card backgrounds |
| Accent Purple | #c084fc | 192, 132, 252 | Headers, highlights |
| Primary Text | #f2f2f2 | 242, 242, 242 | Main content |
| Secondary Text | #a6a6a6 | 166, 166, 166 | Supporting text |
| White | #FFFFFF | 255, 255, 255 | Emphasis text |
| Default Border | #3a2d4f | 58, 45, 79 | Borders |
| Card Border | #261b35 | 38, 27, 53 | Card edges |

### Light Theme Colors (Alternative)
| Color Name | Hex Code | RGB | Usage |
|------------|----------|-----|-------|
| White | #FFFFFF | 255, 255, 255 | Main background |
| Light Gray | #F8F9FA | 248, 249, 250 | Card backgrounds |
| Pale Purple | #FAF8FC | 250, 248, 252 | Tinted backgrounds |
| Accent Purple | #8B5CF6 | 139, 92, 246 | Headers, highlights |
| Primary Text | #1a1a1a | 26, 26, 26 | Main content |
| Secondary Text | #6C757D | 108, 117, 125 | Supporting text |
| Dark Gray | #343A40 | 52, 58, 64 | Strong emphasis |
| Border Gray | #DEE2E6 | 222, 226, 230 | Standard borders |
| Light Border | #E9ECEF | 233, 236, 239 | Subtle borders |

## Typography Quick Reference

### Font Sizes
- **H1 (Titles)**: 30pt, Bold
- **H2 (Sections)**: 24pt, Semibold
- **H3 (Subsections)**: 16pt, Medium
- **Body**: 14pt, Regular
- **Small**: 12pt, Regular

### Font Family
- **Primary**: Arial
- **Fallback**: Calibri, sans-serif
- **Weights**: 400 (regular), 500 (medium), 600 (semibold)

## Logo Usage

### Logo Files
- **Dark Theme**: `gtmfabric_logo_white.png` (on dark backgrounds)
- **Light Theme**: `gtmfabric_logo_black.png` (on light backgrounds)

### Placement
- **PowerPoint**: Top-right, 0.8 inches width
- **PDF**: Top-left (header)
- **Clear space**: 0.25 inches minimum padding

## PowerPoint Slide Templates

### Dark Theme (Primary)

**Title Slide**
```
Background: Deep Purple Black (#06040f)
Title: 30pt, White (#FFFFFF), Bold
Subtitle: 24pt, Accent Purple (#c084fc)
Logo: Top-right, white version
```

**ICP Slide**
```
Background: Deep Purple Black (#06040f)
Card: Card Purple (#120a1f)
ICP Badge: Accent Purple (#c084fc) with 30% opacity
Headers: 16pt, Accent Purple (#c084fc)
Body: 14pt, Primary Text (#f2f2f2)
Vendor Format: **Bold** → Product
Logo: Top-right, white version
```

**Content Slide**
```
Background: Deep Purple Black (#06040f)
Title: 24pt, Accent Purple (#c084fc)
Card: Card Purple (#120a1f), rounded corners
Body: 14pt, Primary Text (#f2f2f2)
Logo: Top-right, white version
```

### Light Theme (Alternative)

**Title Slide**
```
Background: White (#FFFFFF)
Title: 30pt, Primary Text (#1a1a1a), Bold
Subtitle: 24pt, Accent Purple (#8B5CF6)
Accent Bar: Thin line, Accent Purple
Logo: Top-right, black version
```

**ICP Slide**
```
Background: White (#FFFFFF)
Card: Light Gray (#F8F9FA)
ICP Badge: Accent Purple (#8B5CF6) background
Headers: 16pt, Accent Purple (#8B5CF6)
Body: 14pt, Primary Text (#1a1a1a)
Borders: Border Gray (#DEE2E6)
Vendor Format: **Bold** → Product
Logo: Top-right, black version
```

**Content Slide**
```
Background: White (#FFFFFF)
Title: 24pt, Accent Purple (#8B5CF6)
Card: Light Gray (#F8F9FA), rounded corners
Body: 14pt, Primary Text (#1a1a1a)
Borders: Border Gray (#DEE2E6)
Logo: Top-right, black version
```

## ICP Slide Structure

### Required Sections (in order):

1. **ICP Badge/Title**
   - Pill-shaped badge
   - Format: "ICP #1: [Descriptive Title]"
   - Example: "ICP #1: Enterprise Security Modernization Buyer"

2. **Industries**
   - Header: "Industries"
   - Format: Comma-separated list
   - Example: "Financial Services, Healthcare, Manufacturing"

3. **Departments**
   - Header: "Departments"
   - Format: Comma-separated or bullets
   - Example: "IT Security, Infrastructure, Compliance"

4. **Key Roles**
   - Header: "Key Roles"
   - Format: Job titles, bullets or comma-separated
   - Example: "CISO, VP IT, Security Director"

5. **Technographic Fit**
   - **5a. Displacement Signals**
     - Header: "Displacement Signals" or "Modernization Signals"
     - Pain explanation + vendor products
     - Example:
       ```
       Pain: Legacy systems causing compliance risks
       Replacing: McAfee → ePO, Symantec → Endpoint Protection
       ```

   - **5b. Expansion Signals**
     - Header: "Expansion Signals"
     - Readiness explanation + vendor products
     - Example:
       ```
       Readiness: Recent cloud migration
       Using: AWS, Microsoft → Azure, Okta
       ```

## Vendor/Product Formatting

### Standard Format
**Always use arrow notation**: `Vendor → Product`

### Examples (Correct)
✅ Salesforce → Sales Cloud
✅ Microsoft → Azure
✅ Oracle → NetSuite
✅ SAP → S/4HANA

### Examples (Incorrect)
❌ Salesforce (too vague)
❌ Sales Cloud (missing vendor)
❌ Salesforce - Sales Cloud (wrong separator)
❌ Salesforce | Sales Cloud (wrong separator)

### Bold All Vendor/Product Names
- In PowerPoint: Apply bold formatting
- In text: **Salesforce** → **Sales Cloud**
- Makes content more scannable

## Common Mistakes to Avoid

1. **Wrong Background**: Using white or light colors instead of #06040f
2. **Wrong Purple**: Using generic purple instead of Accent Purple #c084fc
3. **Missing Logo**: Always include gtmfabric_logo_white.png on slides
4. **Stretched Logo**: Always maintain aspect ratio
5. **Wrong Font**: Avoid non-Arial fonts (Calibri is acceptable fallback)
6. **Vendor Format**: Forgetting → arrows or bold formatting
7. **Too Much Text**: Keep slides concise (5-6 bullets max)
8. **Missing Sections**: ICP slides need all 5 required sections

## Accessibility Standards

### Color Contrast
- Primary text on dark background: 16:1 ratio (AAA)
- Secondary text on dark background: 7:1 ratio (AA)
- Accent Purple on dark: 8:1 ratio (AA+)

### Font Sizes
- Minimum body text: 14pt (presentations), 11pt (documents)
- Minimum caption: 12pt (presentations), 9pt (documents)

## File Naming Conventions

### Standard Format
```
ClientName_DocumentType_YYYY-MM-DD.ext
```

### Examples
- `Kaspersky_ICPs_2025-01-15.pptx`
- `VenaSolutions_ICPs_2025-01-20.pptx`
- `Autodesk_ICPs_2025-02-01.pptx`

## Content Guidelines

### Tone
- **Professional**: Enterprise B2B
- **Technical**: Data-driven, precise
- **Clear**: Avoid jargon
- **Strategic**: Focus on insights

### Data Formatting
- **Numbers**: 1,000 (comma separators)
- **Currency**: $1,234.56
- **Percentages**: 45.5% (one decimal)
- **Dates**: January 15, 2025

## Quick Checklist Before Delivery

### Theme-Specific Checks

**If Dark Theme:**
- [ ] Deep Purple Black background (#06040f) applied
- [ ] GTM Fabric WHITE logo on all slides (top-right)
- [ ] Light Accent Purple (#c084fc) used for headers
- [ ] Primary Text color (#f2f2f2) for body content
- [ ] Card Purple (#120a1f) for content cards

**If Light Theme:**
- [ ] White background (#FFFFFF) applied
- [ ] GTM Fabric BLACK logo on all slides (top-right)
- [ ] Dark Accent Purple (#8B5CF6) used for headers
- [ ] Primary Text color (#1a1a1a) for body content
- [ ] Light Gray (#F8F9FA) for content cards

### Universal Checks (Both Themes)
- [ ] Correct logo for theme (white for dark, black for light)
- [ ] Arial font used throughout
- [ ] All vendor/product names are **bold**
- [ ] Arrow notation (→) used for all products
- [ ] ICP slides have all 5 required sections
- [ ] Page numbers on content slides
- [ ] No typos or grammatical errors
- [ ] File named correctly (ClientName_ICPs_YYYY-MM-DD.pptx)
- [ ] Theme specified in prompt and correctly applied

## Support Resources

- **Full Guidelines**: See SKILL.md
- **Logo Assets**: gtmfabric_logo_white.png (primary), gtmfabric_logo_black.png
- **Color Palette**: Dark theme with purple accents
- **Font**: Arial (Calibri fallback)

---

**Version**: 1.0.0 (November 2025)
**Company**: GTM Fabric
**Tagline**: "Unified Data. Expert Strategy."
