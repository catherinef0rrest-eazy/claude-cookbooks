# ICP Cards Design System - Quick Reference

## Color Palette Quick Reference

### Background Colors (Dark Theme)
| Name | HSL | Hex | Usage |
|------|-----|-----|-------|
| Background | `hsl(257, 47%, 4%)` | `#06040f` | Main page background |
| Card | `hsl(257, 35%, 8%)` | `#120a1f` | Elevated card surfaces |
| Sidebar | `hsl(257, 40%, 6%)` | `#0e0817` | Sidebar background |

### Text Colors
| Name | HSL | Hex | Usage |
|------|-----|-----|-------|
| Primary Text | `hsl(0, 0%, 95%)` | `#f2f2f2` | Main content text |
| Secondary Text | `hsl(0, 0%, 65%)` | `#a6a6a6` | Supporting text |
| Card Text | `hsl(0, 0%, 95%)` | `#f2f2f2` | Text on cards |

### Border Colors
| Name | HSL | Hex | Usage |
|------|-----|-----|-------|
| Default Border | `hsl(257, 20%, 18%)` | `#3a2d4f` | Standard borders |
| Card Border | `hsl(257, 25%, 14%)` | `#261b35` | Card borders |
| Sidebar Border | `hsl(257, 30%, 12%)` | `#201629` | Sidebar borders |

### Accent Color
**Primary Accent**: `#c084fc` (Light Purple)

**Opacity Variations**:
- 5%: Subtle gradients (`#c084fc0d`)
- 8%: Tints (`#c084fc14`)
- 10%: Badges (`#c084fc1a`)
- 12%: Headers (`#c084fc1f`)
- 20%: Borders (`#c084fc33`)
- 30%: Prominent (`#c084fc4d`)
- 40%: Strong (`#c084fc66`)
- 100%: Full color (`#c084fc`)

## Typography

**Font Family**: Epilogue (Variable weight 100-900)
**Fallback**: `Epilogue, sans-serif`

### Type Scale (Mobile → Desktop)
| Element | Mobile | Desktop | Classes |
|---------|--------|---------|---------|
| H1 | 20px (1.25rem) | 30px (1.875rem) | `text-xl sm:text-3xl` |
| H2 | 24px (1.5rem) | 36px (2.25rem) | `text-2xl sm:text-4xl` |
| H3 | 16px (1rem) | 16px (1rem) | `text-base` |
| Body | 14px (0.875rem) | 14px (0.875rem) | `text-sm` |
| Small | 12px (0.75rem) | 12px (0.75rem) | `text-xs` |

### Font Weights
- **Regular (400)**: Body text
- **Medium (500)**: Labels, emphasized text
- **Semibold (600)**: Headers, titles

### Letter Spacing
- Headers: `-0.025em`
- Body: `0em`
- Labels: `0.025em`
- Uppercase: `0.05em` (use `tracking-wider`)

## Spacing Scale

| Name | Value | Pixels | Usage |
|------|-------|--------|-------|
| xs | 0.5rem | 8px | Tight gaps |
| sm | 0.75rem | 12px | Badge spacing |
| md | 1rem | 16px | Standard gaps |
| lg | 1.5rem | 24px | Section spacing |
| xl | 2rem | 32px | Large sections |
| 2xl | 2.5rem | 40px | Desktop padding |
| 3xl | 3rem | 48px | Major sections |
| 4xl | 4rem | 64px | Desktop major sections |

### Common Spacing Patterns
```css
/* Vertical spacing */
space-y-3   → 12px (tight)
space-y-6   → 24px (mobile sections)
space-y-10  → 40px (desktop sections)

/* Gaps */
gap-3   → 12px (badges)
gap-4   → 16px (logos)
gap-6   → 24px (grids)
gap-12  → 48px (desktop grids)

/* Padding (responsive) */
p-6 sm:p-10      → 24px → 40px
px-6 sm:px-10    → 24px → 40px (horizontal)
py-6 sm:py-8     → 24px → 32px (vertical)
```

## Component Patterns

### Card
```jsx
<div className="w-full max-w-7xl mx-auto bg-card rounded-xl overflow-hidden border border-card-border transition-smooth hover:scale-[1.02]">
  {/* Card content */}
</div>
```

**Hover Shadow**: `0 20px 60px rgba(192, 132, 252, 0.12), 0 0 30px rgba(192, 132, 252, 0.04)`

### Card Header
```jsx
<div
  className="px-6 sm:px-10 py-6 sm:py-8 border-b-2"
  style={{
    background: 'linear-gradient(135deg, #c084fc12 0%, #c084fc05 100%)',
    borderColor: '#c084fc30'
  }}
>
  {/* Header content */}
</div>
```

### Badge / Role Chip
```jsx
<span
  className="px-3 py-1.5 text-xs font-medium rounded-md border"
  style={{
    background: 'linear-gradient(135deg, #c084fc20 0%, #c084fc10 100%)',
    borderColor: '#c084fc40',
    color: '#c084fc'
  }}
>
  Badge Text
</span>
```

### Section Header
```jsx
<div
  className="pb-3 border-b text-base font-semibold uppercase tracking-wider"
  style={{
    borderColor: '#c084fc20',
    color: '#c084fc'
  }}
>
  Section Title
</div>
```

### Subsection Container
```jsx
<div
  className="p-6 rounded-lg space-y-4 border"
  style={{
    background: 'linear-gradient(135deg, #c084fc08 0%, #c084fc03 100%)',
    borderColor: '#c084fc20'
  }}
>
  {/* Subsection content */}
</div>
```

## Gradient Patterns

| Use Case | Pattern |
|----------|---------|
| Card Header | `linear-gradient(135deg, {color}12 0%, {color}05 100%)` |
| Badge | `linear-gradient(135deg, {color}20 0%, {color}10 100%)` |
| Subsection | `linear-gradient(135deg, {color}08 0%, {color}03 100%)` |
| Vertical Bar | `linear-gradient(to bottom, {color}, {color}cc)` |
| Logo Divider | `linear-gradient(180deg, transparent 0%, #c084fc 50%, transparent 100%)` |

## Responsive Breakpoints

| Name | Value | Device Type |
|------|-------|-------------|
| sm | 640px | Landscape phones |
| md | 768px | Tablets |
| lg | 1024px | Laptops |
| xl | 1280px | Desktops |

### Responsive Patterns
```css
/* Typography */
text-xl sm:text-3xl           → 20px → 30px
text-2xl sm:text-4xl          → 24px → 36px

/* Padding */
p-6 sm:p-10                   → 24px → 40px
px-6 sm:px-10 py-6 sm:py-8    → mixed scaling

/* Spacing */
space-y-6 sm:space-y-10       → 24px → 40px
gap-8 md:gap-12               → 32px → 48px

/* Layout */
flex-col sm:flex-row          → vertical → horizontal
grid-cols-1 md:grid-cols-2    → 1 column → 2 columns
hidden sm:block               → hide mobile, show desktop
```

## Animation System

### Transitions
```css
/* Standard smooth transition */
.transition-smooth {
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
}

/* Hover scale */
.hover\:scale-\[1\.02\]:hover {
  transform: scale(1.02);
}
```

### Fade In Up Animation
```css
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(20px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in-up {
  animation: fadeInUp 0.6s ease-out;
}
```

### Stagger Delays
- First element: `animation-delay: 0.1s`
- Second element: `animation-delay: 0.2s`
- Third element: `animation-delay: 0.3s`
- Fourth element: `animation-delay: 0.4s`

## Funnel Visualization

### Width Calculation
```javascript
widthPercent = 100 - (index × 18)
// Level 0: 100%
// Level 1: 82%
// Level 2: 64%
// Level 3: 46%
```

### Level Styling Formula
```javascript
{
  width: `${100 - (index × 18)}%`,
  background: `linear-gradient(135deg, {color}${40 - (index × 8)} 0%, {color}${20 - (index × 8)} 100%)`,
  border: `2px solid {color}${50 + (index × 10)}`,
  boxShadow: `0 4px 20px {color}${20 - (index × 3)}, 0 0 30px {color}${15 - (index × 3)}`
}
```

## Accessibility Checklist

### Color Contrast Requirements
✓ Primary text (95% white): ~16:1 ratio (AAA)
✓ Secondary text (65% white): ~7:1 ratio (AA)
✓ Minimum text size: 14px
✓ Test accent combinations

### Interactive Elements
✓ Minimum touch target: 44px × 44px
✓ Focus indicators: 2px solid accent with 2px offset
✓ Keyboard accessible
✓ Visible focus states

### Semantic HTML
✓ Proper heading hierarchy (h1 → h2 → h3)
✓ ARIA labels where needed
✓ Alt text for images

### Motion
✓ Respect `prefers-reduced-motion`
```css
@media (prefers-reduced-motion: reduce) {
  .animate-fade-in-up,
  .transition-smooth {
    animation: none;
    transition: none;
  }
}
```

## Common Mistakes to Avoid

❌ **DON'T** use hard-coded purple colors
✅ **DO** use CSS custom properties or accent variable

❌ **DON'T** use fixed font sizes without responsive variants
✅ **DO** use mobile-first responsive classes

❌ **DON'T** use custom spacing values outside the scale
✅ **DO** stick to the spacing scale (6, 8, 10, 12, 16)

❌ **DON'T** create animations without reduced-motion fallback
✅ **DO** respect `prefers-reduced-motion`

❌ **DON'T** make touch targets smaller than 44px
✅ **DO** ensure minimum 44px × 44px for interactive elements

## Python Helper Usage

```python
from apply_brand import ICPDesignSystem, generate_component_example

# Initialize system
system = ICPDesignSystem()

# Get accent with opacity
accent_20 = system.get_accent_with_opacity(20)  # "#c084fc33"

# Generate gradients
header_gradient = system.get_gradient_header("#c084fc")
# → {"background": "linear-gradient(135deg, #c084fc12 0%, #c084fc05 100%)"}

# Get Tailwind classes
card_classes = system.get_tailwind_classes("card")
# → "w-full max-w-7xl mx-auto bg-card rounded-xl..."

# Get responsive utilities
padding = system.get_responsive_padding("medium")  # "p-6 sm:p-10"
spacing = system.get_responsive_spacing("normal")  # "space-y-6 sm:space-y-10"
text = system.get_responsive_text("h1")  # "text-xl sm:text-3xl font-semibold"

# Generate CSS custom properties
css = system.generate_css_custom_properties()

# Generate Tailwind config
tailwind_config = system.generate_tailwind_config()

# Validate accessibility
result = system.validate_accessibility(
    system.tokens.colors_background["base"],
    system.tokens.colors_foreground["primary"]
)
```

## File Structure Reference

```
client/src/
├── components/
│   ├── ui/                  # Base UI components
│   ├── Report.tsx           # Main report container
│   ├── ICPCard.tsx          # ICP card component
│   └── PropensityFunnelV2.tsx
├── hooks/
│   └── useScrollAnimation.ts
├── data/
│   └── icpCards.ts
└── index.css                # Global styles & tokens
```

## CSS Custom Properties Template

```css
:root {
  /* Background Colors */
  --background: hsl(257, 47%, 4%);
  --card: hsl(257, 35%, 8%);
  --sidebar: hsl(257, 40%, 6%);

  /* Foreground Colors */
  --foreground: hsl(0, 0%, 95%);
  --muted-foreground: hsl(0, 0%, 65%);
  --card-foreground: hsl(0, 0%, 95%);

  /* Border Colors */
  --border: hsl(257, 20%, 18%);
  --card-border: hsl(257, 25%, 14%);
  --sidebar-border: hsl(257, 30%, 12%);

  /* Accent */
  --accent: #c084fc;

  /* Typography */
  --font-primary: Epilogue, sans-serif;
}
```

---

**Framework**: React + TypeScript
**Styling**: Tailwind CSS + CSS Custom Properties
**Icons**: Lucide React
**Components**: Shadcn/ui + Radix UI
**Version**: 1.0.0 (October 2025)
