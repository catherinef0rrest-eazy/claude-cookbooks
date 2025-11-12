# GTM Fabric Brand Guidelines - Light Theme Addition

## What's New

Added comprehensive **Light Theme** support to complement the existing Dark Theme.

## Theme Overview

### Dark Theme (Primary/Default)
- **Use for**: Digital presentations, client ICP decks, web applications
- **Background**: Deep Purple Black (#06040f)
- **Accent**: Light Accent Purple (#c084fc)
- **Logo**: White version (gtmfabric_logo_white.png)
- **Best for**: Modern, premium aesthetic with high visual impact

### Light Theme (Alternative/New)
- **Use for**: Print documents, PDFs, email attachments, reports
- **Background**: White (#FFFFFF)
- **Accent**: Dark Accent Purple (#8B5CF6)
- **Logo**: Black version (gtmfabric_logo_black.png)
- **Best for**: Universal compatibility and print readability

## Changes Made

### SKILL.md
1. ✅ Added "Theme Selection" section explaining when to use each theme
2. ✅ Split "Color Palette" into two sections:
   - "Color Palette - Dark Theme (Primary)"
   - "Color Palette - Light Theme (Alternative)"
3. ✅ Added semantic colors (Success, Warning, Error) for both themes
4. ✅ Updated Typography section with theme-specific color specifications
5. ✅ Updated Logo Usage to clearly specify which logo for which theme
6. ✅ Expanded PowerPoint section with both theme variants:
   - Dark Theme slide templates (4 types)
   - Light Theme slide templates (4 types)
7. ✅ Expanded PDF Documents section with theme variants
8. ✅ Expanded Excel Spreadsheets section with theme variants
9. ✅ Updated Application Instructions with theme selection guidance

### REFERENCE.md
1. ✅ Added "Theme Selection" section at the top
2. ✅ Updated "Must-Have Elements" for both themes
3. ✅ Added "Never Use" items related to theme mismatches
4. ✅ Split color reference tables:
   - Dark Theme Colors (Primary)
   - Light Theme Colors (Alternative)
5. ✅ Updated PowerPoint Slide Templates with both variants
6. ✅ Updated "Quick Checklist Before Delivery" with theme-specific checks

### README.md
- No changes needed (already comprehensive about usage patterns)

## Color Reference Quick Guide

### Dark Theme Colors
| Element | Color | Hex |
|---------|-------|-----|
| Background | Deep Purple Black | #06040f |
| Cards | Card Purple | #120a1f |
| Accent | Light Purple | #c084fc |
| Primary Text | Light Gray | #f2f2f2 |
| Secondary Text | Medium Gray | #a6a6a6 |

### Light Theme Colors
| Element | Color | Hex |
|---------|-------|-----|
| Background | White | #FFFFFF |
| Cards | Light Gray | #F8F9FA |
| Accent | Dark Purple | #8B5CF6 |
| Primary Text | Near Black | #1a1a1a |
| Secondary Text | Medium Gray | #6C757D |

## How to Use Light Theme

### In Prompts

**Explicit theme specification:**
```
"Create a GTM Fabric ICP presentation using LIGHT THEME:
- White background (#FFFFFF)
- Black logo (gtmfabric_logo_black.png)
- Dark text colors
- Follow gtmfabric-brand-guidelines"
```

### When to Choose Light Theme

✅ **Use Light Theme for:**
- Documents that will be printed
- PDF reports
- Email attachments (better compatibility)
- Environments with bright ambient lighting
- Multi-format delivery (digital + print)

✅ **Use Dark Theme for:**
- Digital-only presentations
- Client-facing ICP decks
- Web applications
- Situations where visual impact is priority
- Screen-based presentations

## Example Usage

### Dark Theme ICP Presentation (Default)
```python
response = client.beta.messages.create(
    container={"skills": [{"type": "anthropic", "skill_id": "pptx"}]},
    messages=[{"role": "user", "content": """
        Create GTM Fabric ICP presentation using DARK THEME:
        
        [ICP content]
        
        Apply gtmfabric-brand-guidelines:
        - Deep Purple Black background (#06040f)
        - White logo on all slides
        - Light Accent Purple (#c084fc) for headers
    """}]
)
```

### Light Theme ICP Presentation (Alternative)
```python
response = client.beta.messages.create(
    container={"skills": [{"type": "anthropic", "skill_id": "pptx"}]},
    messages=[{"role": "user", "content": """
        Create GTM Fabric ICP presentation using LIGHT THEME:
        
        [ICP content]
        
        Apply gtmfabric-brand-guidelines:
        - White background (#FFFFFF)
        - Black logo on all slides
        - Dark Accent Purple (#8B5CF6) for headers
    """}]
)
```

## Migration Notes

### For Existing Workflows

If you have existing workflows using the branding skill:

1. **No breaking changes**: Dark theme remains the default
2. **Explicit is better**: Always specify theme in prompts
3. **Logo selection**: Claude will use correct logo based on theme specification
4. **Backward compatible**: Existing dark theme prompts still work

### Common Mistakes to Avoid

❌ **Wrong logo for theme**
- Don't use white logo on light background
- Don't use black logo on dark background

❌ **Missing theme specification**
- Always specify "Dark Theme" or "Light Theme" in prompts
- Don't assume Claude will guess correctly

❌ **Mixed themes**
- Don't mix dark and light theme colors
- Keep theme consistent throughout document

## Accessibility Benefits

### Light Theme Advantages
- ✅ Better contrast ratios in print (16:1 for body text)
- ✅ Universal compatibility (works on any display)
- ✅ Easier on eyes in bright environments
- ✅ More familiar for traditional business documents

### Dark Theme Advantages
- ✅ Modern, premium aesthetic
- ✅ Better for dimly-lit presentation rooms
- ✅ Reduces eye strain in dark environments
- ✅ Higher visual impact and memorability

## Testing Checklist

Before delivering documents with light theme:

- [ ] Specified "Light Theme" in prompt
- [ ] White background applied (#FFFFFF)
- [ ] Black logo used (gtmfabric_logo_black.png)
- [ ] Dark Accent Purple for headers (#8B5CF6)
- [ ] Primary Text is dark (#1a1a1a)
- [ ] Light Gray for cards (#F8F9FA)
- [ ] Border Gray for borders (#DEE2E6)
- [ ] No dark theme colors present
- [ ] Print preview looks correct
- [ ] PDF renders correctly

## Questions?

See the full guidelines:
- **SKILL.md**: Complete brand guidelines with both themes
- **REFERENCE.md**: Quick reference card with theme comparison
- **README.md**: Usage examples and integration guide

---

**Version**: 1.1.0 (November 2025)
**Added**: Light Theme support
**Backward Compatible**: Yes (Dark Theme remains default)
