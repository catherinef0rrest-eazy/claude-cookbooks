---
name: applying-brand-guidelines-gtmfabric
description: Apply professional enterprise design system for ICP Cards presentation applications with dark theme, purple accents, and mobile-first responsive patterns
---

# ICP Cards Visual Design System Skill

This skill ensures consistent, professional visual design across ICP (Ideal Customer Profile) presentation applications using a sophisticated dark theme with purple accents and mobile-first responsive patterns.

## Design Philosophy

### Core Principles

**Professional Enterprise Aesthetic**:
- Clean, modern interface targeting B2B decision-makers
- Technical sophistication balanced with visual approachability
- Data-driven presentation with clear information hierarchy

**Minimal Brand Presence**:
- Purple accent color used sparingly (5-10% of visual space)
- System-focused design prioritizes content over decoration
- Generous white space for improved readability

**Mobile-First Responsive**:
- Progressive enhancement from mobile to desktop
- Touch-friendly interactions and spacing (minimum 44px targets)
- Intelligent layout adaptations across breakpoints

**Subtle Motion**:
- Purposeful animations that enhance UX without distraction
- Smooth transitions with cubic-bezier(0.4, 0, 0.2, 1) easing
- Performance-optimized transforms

## Visual Standards

### Color Palette

**Background Colors**:
- **Background**: `hsl(257, 47%, 4%)` / `#06040f` - Deep purple-black base
- **Card**: `hsl(257, 35%, 8%)` / `#120a1f` - Elevated card background
- **Sidebar**: `hsl(257, 40%, 6%)` / `#0e0817` - Sidebar background

**Foreground Colors**:
- **Primary Text**: `hsl(0, 0%, 95%)` / `#f2f2f2` - Main content
- **Secondary Text**: `hsl(0, 0%, 65%)` / `#a6a6a6` - Supporting content
- **Card Text**: `hsl(0, 0%, 95%)` / `#f2f2f2` - Card content

**Border Colors**:
- **Default Border**: `hsl(257, 20%, 18%)` / `#3a2d4f`
- **Card Border**: `hsl(257, 25%, 14%)` / `#261b35`
- **Sidebar Border**: `hsl(257, 30%, 12%)` / `#201629`

**Accent System**:
- **Primary Accent**: `#c084fc` (Light Purple)
- **Opacity Variations**: 5% (gradients), 8% (tints), 10% (badges), 12% (headers), 20% (borders), 30% (prominent), 40% (strong), 100% (full)

**Elevation States**:
- **Hover**: `rgba(255, 255, 255, 0.04)`
- **Active/Pressed**: `rgba(255, 255, 255, 0.09)`
- **Button Outline**: `rgba(255, 255, 255, 0.10)`
- **Badge Outline**: `rgba(255, 255, 255, 0.05)`

### Typography

**Primary Font**: Arial

**Fallback Stack**: `Arial, sans-serif`

**Type Scale (Mobile → Desktop)**:
- **H1 (Card Headers)**: 20px → 30px / 1.25rem → 1.875rem
- **H2 (Section Headers)**: 24px → 36px / 1.5rem → 2.25rem
- **H3 (Subsections)**: 16px / 1rem (consistent)
- **Body Text**: 14px / 0.875rem (consistent)
- **Small Text**: 12px / 0.75rem (consistent)

**Font Weights**:
- **Regular (400)**: Body text, descriptions
- **Medium (500)**: Emphasized text, labels
- **Semibold (600)**: Headers, titles, important UI

**Text Styling**:
- Letter spacing: `-0.025em` (headers), `0em` (body), `0.025em` (labels), `0.05em` (uppercase)
- Line height: `1.625` (body), `1.25` (compact)
- Font smoothing: `antialiased` globally

### Spacing Scale

**Container System**:
- Max width: `80rem / 1280px`
- Horizontal padding: `1rem` mobile, `2rem` desktop
- Vertical padding: `2rem` mobile, `4rem` desktop

**Internal Spacing**:
- `space-y-3`: 12px - Tight spacing
- `space-y-5`: 20px - Medium spacing
- `space-y-6`: 24px - Mobile sections
- `space-y-8`: 32px - Large mobile sections
- `space-y-10`: 40px - Desktop sections
- `space-y-12`: 48px - Major sections
- `space-y-16`: 64px - Desktop major sections

**Gap Spacing**:
- `gap-2`: 8px - Tight elements
- `gap-3`: 12px - Badge groups
- `gap-4`: 16px - Logo groups
- `gap-6`: 24px - Grid gaps
- `gap-8`: 32px - Mobile grid gaps
- `gap-12`: 48px - Desktop grid gaps

## Component Patterns

### Card Structure

**Base Card**:
```css
Classes: w-full max-w-7xl mx-auto bg-card rounded-xl overflow-hidden border border-card-border
Effects: transition-smooth hover:scale-[1.02]
Hover Shadow: 0 20px 60px rgba(192, 132, 252, 0.12), 0 0 30px rgba(192, 132, 252, 0.04)
```

**Card Header with Gradient**:
```css
Padding: px-6 sm:px-10 py-6 sm:py-8
Background: linear-gradient(135deg, {accentColor}12 0%, {accentColor}05 100%)
Border Bottom: 2px solid {accentColor}30
Accent Bar: w-1.5 h-16 rounded-full, gradient(to bottom, {color}, {color}cc)
```

**Card Content**:
```css
Padding: p-6 sm:p-10
Spacing: space-y-6 sm:space-y-10
```

### Badges / Role Chips

**Structure**:
```css
Padding: px-3 py-1.5 (12px × 6px)
Font: text-xs font-medium (12px, weight 500)
Radius: rounded-md (6px)
Background: linear-gradient(135deg, {accentColor}20 0%, {accentColor}10 100%)
Border: 1px solid {accentColor}40
Color: {accentColor}
```

### Section Headers

**With Underline**:
```css
Container: pb-3 border-b, borderColor: {accentColor}20
Title: text-base font-semibold uppercase tracking-wider
Color: {accentColor}
```

**With Accent Dot**:
```css
Dot: w-2 h-2 rounded-full, backgroundColor: {accentColor}
Gap: gap-3 between dot and title
```

### Dividers

**Horizontal Border**:
```css
Class: border-b
Style: borderColor: {accentColor}20
```

**Decorative Divider**:
```css
Structure: h-px w-24 gradient lines + w-2 h-2 rounded-full center dot
Gradient: from-transparent via-border to-transparent
```

**Logo Divider (Vertical)**:
```css
Dimensions: h-16 w-px
Background: linear-gradient(180deg, transparent 0%, #c084fc 50%, transparent 100%)
Shadow: 0 0 8px rgba(192, 132, 252, 0.6), 0 0 12px rgba(192, 132, 252, 0.4)
Display: hidden sm:block (desktop only)
```

### Subsection Containers

**Legacy/Expansion Indicators**:
```css
Padding: p-6
Radius: rounded-lg
Spacing: space-y-4
Background: linear-gradient(135deg, {accentColor}08 0%, {accentColor}03 100%)
Border: 1px solid {accentColor}20
```

### Indicator Items

**With Arrow Notation**:
```css
Container: p-3 rounded-md bg-card border border-border space-y-2
Description: text-sm text-foreground leading-relaxed
Tools: text-xs text-muted-foreground font-mono, prefix with "→ "
```

### Funnel Visualization

**Level Calculation**:
```javascript
widthPercent = 100 - (index × 18)
// Level 1: 100%, Level 2: 82%, Level 3: 64%, Level 4: 46%
```

**Level Styling**:
```css
Width: {widthPercent}% with margin: 0 auto
Padding: p-6
Background: linear-gradient(135deg, {accentColor}{opacity} 0%, {accentColor}{opacity-20} 100%)
Border: 2px solid {accentColor}{50 + index × 10}
Shadow: 0 4px 20px {accentColor}{20 - index × 3}, 0 0 30px {accentColor}{15 - index × 3}
Transition: transition-all duration-300
```

**Connecting Arrow**:
```svg
<svg width="24" height="24" viewBox="0 0 24 24">
  <path d="M12 5 L12 19 M12 19 L7 14 M12 19 L17 14"
        stroke="{accentColor}"
        strokeWidth="2"
        strokeLinecap="round"
        strokeLinejoin="round" />
</svg>
```

## Animation System

### Scroll Animations

**Fade In Up**:
```css
@keyframes fadeInUp {
  from: opacity: 0, transform: translateY(20px)
  to: opacity: 1, transform: translateY(0)
}
Duration: 0.6s
Easing: ease-out
```

**Usage Pattern**:
- Intersection Observer triggers animation when element enters viewport
- Adds 'animate-fade-in-up' class
- Creates staggered entrance effect with delays (0.1s, 0.2s, 0.3s, 0.4s)

### Transitions

**Smooth Transition**:
```css
Class: transition-smooth
Value: all 0.3s cubic-bezier(0.4, 0, 0.2, 1)
```

**Hover Effects**:
```css
Card Hover: hover:scale-[1.02] (2% scale increase)
Duration: 0.3s
Easing: cubic-bezier(0.4, 0, 0.2, 1)
```

### Motion Preferences

**Respect Reduced Motion**:
```css
@media (prefers-reduced-motion: reduce) {
  .animate-fade-in-up, .transition-smooth {
    animation: none;
    transition: none;
  }
}
```

## Responsive Patterns

### Breakpoint System

- **sm**: 640px - Small devices (landscape phones)
- **md**: 768px - Medium devices (tablets)
- **lg**: 1024px - Large devices (laptops)
- **xl**: 1280px - Extra large devices (desktops)

### Layout Transformations

**Typography Scaling**:
```css
text-xl sm:text-3xl (20px → 30px)
text-2xl sm:text-4xl (24px → 36px)
```

**Padding Scaling**:
```css
px-6 sm:px-10 py-6 sm:py-8 (24px → 40px × 24px → 32px)
p-6 sm:p-10 (24px → 40px all sides)
```

**Spacing Scaling**:
```css
space-y-6 sm:space-y-10 (24px → 40px vertical)
gap-8 md:gap-12 (32px → 48px grid)
```

**Layout Changes**:
```css
flex-col sm:flex-row (stack → horizontal)
grid-cols-1 md:grid-cols-2 (single → two columns)
flex flex-col md:grid md:grid-cols-[45%,55%] (flex → asymmetric grid)
```

### Component Responsiveness

**Header Logos**:
```css
Mobile: flex-col (vertical stack)
Desktop: sm:flex-row (horizontal)
Gap: gap-3 sm:gap-4 (12px → 16px)
```

**Dividers**:
```css
Visibility: hidden sm:block (desktop only)
```

**Cards**:
```css
Grid: grid-cols-1 md:grid-cols-2 gap-6
Padding: p-6 sm:p-10
```

**Funnel**:
```css
Mobile: flex flex-col
Desktop: md:grid md:grid-cols-[45%,55%]
Gap: gap-8 md:gap-12
```

## Visual Effects

### Background Effects

**Technical Grid Overlay**:
```css
Position: fixed inset-0 pointer-events-none
Background: linear-gradient grid pattern (purple #9333ea at 15% opacity)
Grid Size: 60px × 60px
Mask: radial-gradient(ellipse at center, black 20%, transparent 80%)
```

**Radial Glow**:
```css
Position: fixed inset-0 pointer-events-none
Background: radial-gradient(ellipse at 50% 20%, rgba(147, 51, 234, 0.08) 0%, transparent 50%)
```

### Header Effects

**Sticky Header**:
```css
Position: sticky top-0 z-50
Background: bg-card/80 backdrop-blur-sm
Border: border-b border-border
Shadow: shadow-sm
```

### Gradient Patterns

**Common Gradients**:
- Header: `linear-gradient(135deg, {color}12 0%, {color}05 100%)`
- Badge: `linear-gradient(135deg, {color}20 0%, {color}10 100%)`
- Subsection: `linear-gradient(135deg, {color}08 0%, {color}03 100%)`
- Vertical Bar: `linear-gradient(to bottom, {color}, {color}cc)`

### Shadow System

**Card Hover**:
```css
box-shadow: 0 20px 60px rgba(192, 132, 252, 0.12), 
            0 0 30px rgba(192, 132, 252, 0.04)
```

**Funnel Levels**:
```css
box-shadow: 0 4px 20px {color}{20 - index × 3}, 
            0 0 30px {color}{15 - index × 3}
```

## Accessibility Standards

### Color Contrast

**Requirements**:
- Primary text (95% white): ~16:1 ratio (AAA compliant)
- Secondary text (65% white): ~7:1 ratio (AA compliant)
- Minimum text size: 14px for reliable readability
- Test all accent color combinations for contrast

### Focus Indicators

**Required Pattern**:
```css
.focus-visible:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
}
```

### Semantic HTML

**Requirements**:
- Use proper heading hierarchy (h1 → h2 → h3)
- Add ARIA labels where needed
- Include skip-to-content links
- Provide alt text for all images

### Keyboard Navigation

**Standards**:
- All interactive elements must be keyboard accessible
- Tab order follows visual hierarchy
- Visible focus states on all focusable elements
- Touch targets minimum 44px × 44px

## Implementation Guidelines

### Color Application

**DO**:
```css
/* Use CSS custom properties */
className="bg-background text-foreground"

/* Use inline styles for dynamic colors */
style={{ color: accentColor, borderColor: `${accentColor}20` }}
```

**DON'T**:
```css
/* Hard-code color values */
style={{ color: '#c084fc' }}  /* Use accentColor variable instead */
```

### Typography Application

**DO**:
```css
/* Mobile-first responsive */
className="text-xl sm:text-3xl font-semibold"

/* With appropriate tracking */
className="text-base font-semibold uppercase tracking-wider"
```

**DON'T**:
```css
/* Fixed sizes without responsive variants */
className="text-3xl"  /* Add mobile size first */
```

### Spacing Application

**DO**:
```css
/* Consistent padding scale */
className="p-6 sm:p-10"

/* Vertical rhythm */
className="space-y-6 sm:space-y-10"
```

**DON'T**:
```css
/* Custom values outside scale */
className="p-7"  /* Use standard spacing scale */
```

### Component Usage

**DO**:
```css
/* Import and use Card component */
import { Card } from "@/components/ui/card"

/* Apply consistent hover effects */
className="transition-smooth hover:scale-[1.02]"
```

**DON'T**:
```css
/* Create custom containers */
<div className="custom-card">  /* Use Card component */
```

## Quality Checklist

### Before Finalizing

Always verify:
1. ✓ All colors use CSS custom properties or accentColor variable
2. ✓ Typography follows mobile-first responsive pattern
3. ✓ Spacing uses consistent scale (6, 8, 10, 12, 16)
4. ✓ Cards have proper hover effects and shadows
5. ✓ Interactive elements have 44px minimum touch targets
6. ✓ Contrast ratios meet accessibility standards
7. ✓ Animations respect prefers-reduced-motion
8. ✓ Layout works at all breakpoints (375px, 640px, 768px, 1024px, 1280px)
9. ✓ Focus indicators visible on all interactive elements
10. ✓ Semantic HTML with proper heading hierarchy

### Prohibited Patterns

Never use:
- Hard-coded hex colors (use CSS variables)
- Fixed font sizes without responsive variants
- Custom spacing values outside the design scale
- Animations without reduced-motion fallback
- Touch targets smaller than 44px
- Interactive elements without focus states

## File Structure

```
client/src/
├── components/
│   ├── ui/                  # Base UI components (Card, Button, etc.)
│   ├── Report.tsx           # Main report container
│   ├── ICPCard.tsx          # ICP card component
│   ├── PropensityFunnelV2.tsx
│   └── E2ESlide.tsx
├── hooks/
│   └── useScrollAnimation.ts
├── data/
│   └── icpCards.ts
└── index.css                # Global styles & design tokens
```

## Scripts

**Font Loading**:
```css
/* Arial is a system font, no @font-face needed */
body {
  font-family: Arial, sans-serif;
}
```

**Scroll Animation Hook**:
```typescript
// useScrollAnimation.ts
// Returns { ref, isVisible }
// Triggers when element enters viewport
// Adds 'animate-fade-in-up' class
```

## PowerPoint Generation

### Overview

The `pptx_generator.py` module provides a modern, sleek PowerPoint presentation generator using the GTM Fabric design system. It creates professional presentations with the dark purple theme, proper typography, and automatic GTM Fabric logo inclusion.

### Key Features

- **Modern Card-Based Layouts**: Clean, professional slide designs with rounded corners and subtle borders
- **GTM Fabric Branding**: Automatic logo placement with configurable positioning
- **Dark Theme**: Deep purple-black backgrounds with high-contrast text
- **Accent Color System**: Purple accent colors (#c084fc) used strategically
- **Typography**: Arial font family with proper sizing and weights
- **ICP-Specific Slides**: Pre-built templates for Ideal Customer Profile presentations

### Quick Start

```python
from pptx_generator import GTMFabricPresentationGenerator

# Initialize generator
generator = GTMFabricPresentationGenerator()

# Create presentation
prs = generator.create_presentation()

# Add title slide
generator.create_title_slide(
    prs,
    title="Your Company - Ideal Customer Profiles",
    subtitle="Cloud Platform GTM Campaign",
    date="January 2025"
)

# Add ICP slide
generator.create_icp_slide(
    prs,
    icp_number=1,
    icp_title="Enterprise Finance Modernizer",
    industries=["Manufacturing", "Retail", "Healthcare"],
    departments="Finance, FP&A, Accounting",
    key_roles=["CFO", "VP FP&A", "Finance Director"],
    displacement_signals=[{
        "pain_explanation": "Using legacy EPM systems with limited flexibility",
        "vendor_products": ["Oracle Hyperion", "SAP BPC"]
    }],
    expansion_signals=[{
        "readiness_explanation": "Recently deployed cloud ERP",
        "vendor_products": ["Workday", "NetSuite"]
    }]
)

# Save presentation
generator.save_presentation(prs, "output.pptx")
```

### Generate from JSON

For ICP campaigns, use the convenience function to generate complete presentations from JSON data:

```python
from pptx_generator import generate_icp_presentation
import json

# Load ICP data
with open('icps.json', 'r') as f:
    data = json.load(f)

# Generate presentation
generate_icp_presentation(
    campaign_info=data['campaign_info'],
    icps=data['icps'],
    output_path='client-icps.pptx'
)
```

### Slide Types

#### 1. Title Slide
- Large title with accent underline
- Subtitle in accent color
- Optional date
- GTM Fabric logo (top-right by default)
- Modern accent bar design element

#### 2. Content Slide
- Card-based content area with rounded corners
- Multiple content sections with headers
- Bullet points or plain text
- Consistent spacing and typography
- Optional page numbers

#### 3. ICP Slide
- ICP badge with number
- Industries section
- Departments & key roles
- Technographic fit section:
  - Displacement / Modernization Signals
  - Expansion Signals
- Vendor products with arrow notation (→)

### Customization Options

**Logo Positioning**:
```python
generator._add_logo(slide, position="top-right", size=0.8)
# Options: "top-right", "top-left", "bottom-right", "bottom-left"
```

**Custom Colors**:
```python
# Override default colors if needed
from pptx_generator import GTMFabricColors
from pptx.dml.color import RGBColor

colors = GTMFabricColors()
colors.accent = RGBColor(200, 150, 250)  # Custom purple
```

**Slide Dimensions**:
```python
# Default: 10" × 5.625" (16:9 standard)
prs = generator.create_presentation(slide_width=10, slide_height=5.625)

# Traditional 4:3 format
prs = generator.create_presentation(slide_width=10, slide_height=7.5)
```

### Design Guidelines for PowerPoint

When creating presentations with this tool:

1. **Keep text concise** - Slides are designed for executive audiences
2. **Use bullet points** - Maximum 3-5 bullets per section
3. **Highlight vendor names** - Products appear after arrow (→) notation
4. **Maintain hierarchy** - Headers use accent color, body uses primary text color
5. **Include page numbers** - Especially for multi-slide presentations
6. **Logo consistency** - Logo appears on all slides by default

### File Locations

- **Generator Module**: `pptx_generator.py`
- **White Logo**: `gtmfabric_logo_white.png` (used for dark theme)
- **Black Logo**: `gtmfabric_logo_black.png` (available for light backgrounds)
- **Design System**: `apply_brand.py` (color and typography tokens)

### Requirements

```bash
pip install python-pptx
```

The module requires the `python-pptx` library for PowerPoint generation.

### Best Practices

1. **Validate JSON structure** before passing to generator
2. **Keep vendor lists concise** (2-3 products max per signal)
3. **Use descriptive ICP titles** that identify the persona
4. **Test generated files** in PowerPoint/Keynote before sharing
5. **Verify logo renders** properly on all slides

### Troubleshooting

**Logo not appearing**:
- Check that `gtmfabric_logo_white.png` exists in the skill directory
- Verify file permissions allow reading the logo file
- Try specifying full path: `GTMFabricPresentationGenerator(logo_path="/full/path/to/logo.png")`

**Font not displaying correctly**:
- Arial is a standard system font on all platforms
- Falls back to sans-serif if needed

**Text overflow**:
- Reduce content length if text doesn't fit
- Use shorter vendor product names
- Break long explanations into multiple bullets

## Notes

- This design system targets enterprise B2B applications
- Dark theme optimized for extended viewing sessions
- Purple accent creates professional tech aesthetic
- Mobile-first ensures accessibility across devices (web)
- PowerPoint generation available for ICP presentations
- Animations enhance UX without overwhelming users
- System prioritizes content readability and data clarity

---

**Framework**: React + TypeScript (Web) | Python (PowerPoint)
**Styling**: Tailwind CSS + CSS Custom Properties (Web) | python-pptx (PowerPoint)
**Icons**: Lucide React
**Components**: Shadcn/ui + Radix UI primitives
**Version**: 1.0.0 (October 2025)