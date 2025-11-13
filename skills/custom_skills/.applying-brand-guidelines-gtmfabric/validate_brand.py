#!/usr/bin/env python3
"""
ICP Cards Design System Validator
Validates React/TypeScript code against ICP Cards visual design guidelines.
Checks colors, typography, spacing, accessibility, and component patterns.
"""

import re
from typing import List, Tuple, Dict, Any
from dataclasses import dataclass, asdict


@dataclass
class ICPDesignGuidelines:
    """ICP Cards design system guidelines"""

    # Color palette
    approved_colors: List[str] = None
    accent_primary: str = "#c084fc"

    # Typography
    font_family: str = "Arial"
    approved_font_weights: List[int] = None

    # Spacing scale (in px)
    approved_spacing: List[int] = None

    # Accessibility requirements
    min_touch_target: int = 44  # pixels
    min_contrast_ratio_body: float = 4.5
    min_contrast_ratio_large: float = 3.0

    def __post_init__(self):
        if self.approved_colors is None:
            self.approved_colors = [
                # Background colors
                "hsl(257, 47%, 4%)", "#06040f",    # Background
                "hsl(257, 35%, 8%)", "#120a1f",    # Card
                "hsl(257, 40%, 6%)", "#0e0817",    # Sidebar
                # Text colors
                "hsl(0, 0%, 95%)", "#f2f2f2",      # Primary text
                "hsl(0, 0%, 65%)", "#a6a6a6",      # Secondary text
                # Border colors
                "hsl(257, 20%, 18%)", "#3a2d4f",   # Default border
                "hsl(257, 25%, 14%)", "#261b35",   # Card border
                "hsl(257, 30%, 12%)", "#201629",   # Sidebar border
                # Accent
                "#c084fc",                          # Primary accent
            ]

        if self.approved_font_weights is None:
            self.approved_font_weights = [400, 500, 600]

        if self.approved_spacing is None:
            self.approved_spacing = [8, 12, 16, 20, 24, 32, 40, 48, 64]


@dataclass
class ValidationResult:
    """Result of design system validation"""

    passed: bool
    score: float
    violations: List[str]
    warnings: List[str]
    suggestions: List[str]
    accessibility_issues: List[str]


class ICPDesignValidator:
    """Validates React/Tailwind code against ICP design system"""

    def __init__(self, guidelines: ICPDesignGuidelines = None):
        self.guidelines = guidelines or ICPDesignGuidelines()

    def validate_colors(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Validate color usage in React/Tailwind code
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Find hex colors
        hex_pattern = r"#[0-9A-Fa-f]{6}(?:[0-9A-Fa-f]{2})?"
        found_colors = re.findall(hex_pattern, code)

        # Find HSL colors
        hsl_pattern = r"hsl\(\s*\d+\s*,\s*\d+%\s*,\s*\d+%\s*\)"
        found_colors.extend(re.findall(hsl_pattern, code, re.IGNORECASE))

        # Check each color
        for color in set(found_colors):
            # Allow accent color with opacity suffixes
            if color.startswith(self.guidelines.accent_primary):
                continue

            # Normalize hex colors for comparison (remove alpha if present)
            color_base = color[:7] if len(color) > 7 else color

            # Check if approved
            if not any(
                approved.lower() == color.lower() or
                approved.lower() == color_base.lower()
                for approved in self.guidelines.approved_colors
            ):
                violations.append(
                    f"Unapproved color '{color}' - use design system tokens or accent color"
                )

        # Check for hard-coded colors in inline styles
        inline_style_pattern = r'style=\{\{[^}]+color:\s*["\']([^"\']+)["\']'
        inline_colors = re.findall(inline_style_pattern, code)

        for color in inline_colors:
            if color not in ["inherit", "currentColor"] and not color.startswith("var("):
                if color not in self.guidelines.approved_colors and not color.startswith(self.guidelines.accent_primary):
                    warnings.append(
                        f"Inline color '{color}' - consider using CSS custom properties"
                    )

        return violations, warnings

    def validate_typography(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Validate typography usage (font family, sizes, weights)
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Check font family usage
        font_pattern = r'font-family:\s*["\']?([^;"\']+)["\']?'
        found_fonts = re.findall(font_pattern, code, re.IGNORECASE)

        for font in found_fonts:
            font_clean = font.strip().lower()
            if self.guidelines.font_family.lower() not in font_clean and "var(--font" not in font_clean:
                violations.append(
                    f"Unapproved font '{font}' - use {self.guidelines.font_family}"
                )

        # Check for non-responsive text sizes
        fixed_text_pattern = r'className="[^"]*text-(xs|sm|base|lg|xl|2xl|3xl|4xl)(?!\s+sm:|md:|lg:)[^"]*"'
        if re.search(fixed_text_pattern, code):
            # Check if there's any responsive variant nearby
            responsive_text_pattern = r'text-\w+\s+(sm|md|lg):text-'
            if not re.search(responsive_text_pattern, code):
                warnings.append(
                    "Consider using responsive typography (e.g., text-xl sm:text-3xl)"
                )

        # Check for approved font weights
        weight_pattern = r'font-weight:\s*(\d+)'
        found_weights = re.findall(weight_pattern, code)

        for weight in found_weights:
            if int(weight) not in self.guidelines.approved_font_weights:
                violations.append(
                    f"Unapproved font weight '{weight}' - use 400, 500, or 600"
                )

        return violations, warnings

    def validate_spacing(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Validate spacing usage (padding, margin, gap)
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Check for custom pixel values in inline styles
        custom_spacing_pattern = r'(padding|margin|gap):\s*["\']?(\d+)px["\']?'
        found_spacing = re.findall(custom_spacing_pattern, code, re.IGNORECASE)

        for prop, value in found_spacing:
            if int(value) not in self.guidelines.approved_spacing:
                violations.append(
                    f"Custom spacing '{value}px' for {prop} - use spacing scale: {self.guidelines.approved_spacing}"
                )

        # Check for responsive padding patterns
        padding_pattern = r'className="[^"]*p-\d+[^"]*"'
        if re.search(padding_pattern, code):
            responsive_padding = r'p-\d+\s+(sm|md|lg):p-'
            if not re.search(responsive_padding, code):
                warnings.append(
                    "Consider using responsive padding (e.g., p-6 sm:p-10)"
                )

        return violations, warnings

    def validate_component_patterns(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Validate component pattern usage
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Check for card hover effects
        if "rounded-xl" in code and "border" in code:
            if "hover:scale-" not in code:
                warnings.append(
                    "Cards should include hover:scale-[1.02] for interaction feedback"
                )

            if "transition" not in code:
                warnings.append(
                    "Cards should include transition-smooth for smooth animations"
                )

        # Check for gradient patterns
        gradient_pattern = r'linear-gradient\([^)]+\)'
        found_gradients = re.findall(gradient_pattern, code)

        approved_gradient_patterns = [
            r'135deg,\s*[#\w]+12\s+0%,\s*[#\w]+05\s+100%',  # Header
            r'135deg,\s*[#\w]+20\s+0%,\s*[#\w]+10\s+100%',  # Badge
            r'135deg,\s*[#\w]+08\s+0%,\s*[#\w]+03\s+100%',  # Subsection
        ]

        for gradient in found_gradients:
            is_approved = any(re.search(pattern, gradient) for pattern in approved_gradient_patterns)
            if not is_approved:
                warnings.append(
                    f"Custom gradient pattern - consider using design system gradients"
                )

        # Check for section headers with proper styling
        if "uppercase" in code and "tracking-wider" not in code:
            warnings.append(
                "Uppercase text should include tracking-wider for readability"
            )

        return violations, warnings

    def validate_accessibility(self, code: str) -> List[str]:
        """
        Validate accessibility requirements
        Returns: list of accessibility issues
        """
        issues = []

        # Check for focus indicators
        if "focus:" in code or "focus-visible:" in code:
            if "outline" not in code and "ring" not in code:
                issues.append(
                    "Focus states detected but no visible focus indicator (outline or ring)"
                )

        # Check for interactive elements without focus states
        button_pattern = r'<button[^>]*className="([^"]*)"'
        buttons = re.findall(button_pattern, code)

        for button_classes in buttons:
            if "focus:" not in button_classes and "focus-visible:" not in button_classes:
                issues.append(
                    "Button missing focus indicator - add focus-visible:outline"
                )

        # Check for images without alt text
        img_pattern = r'<img[^>]*(?!alt=)[^>]*>'
        if re.search(img_pattern, code):
            issues.append(
                "Image found without alt attribute - add alt text for accessibility"
            )

        # Check for animations without reduced-motion support
        if "animate-" in code or "transition" in code:
            if "prefers-reduced-motion" not in code:
                issues.append(
                    "Animations should respect prefers-reduced-motion media query"
                )

        # Check for proper heading hierarchy
        heading_pattern = r'<h([1-6])'
        headings = re.findall(heading_pattern, code)

        if headings:
            heading_levels = [int(h) for h in headings]
            for i in range(len(heading_levels) - 1):
                if heading_levels[i + 1] > heading_levels[i] + 1:
                    issues.append(
                        f"Heading hierarchy skip detected (h{heading_levels[i]} → h{heading_levels[i+1]})"
                    )

        # Check for minimum touch targets
        small_button_pattern = r'className="[^"]*(?:text-xs|text-sm)[^"]*"[^>]*>.*?<button'
        if re.search(small_button_pattern, code):
            issues.append(
                f"Ensure interactive elements meet minimum {self.guidelines.min_touch_target}px touch target"
            )

        return issues

    def validate_responsive_design(self, code: str) -> Tuple[List[str], List[str]]:
        """
        Validate responsive design patterns
        Returns: (violations, warnings)
        """
        violations = []
        warnings = []

        # Check for mobile-first approach
        desktop_only_pattern = r'className="[^"]*\s(lg|xl|2xl):[^"]*"'
        if re.search(desktop_only_pattern, code):
            mobile_pattern = r'className="[^"]*(?:text-|p-|m-|space-)[^"]*"'
            if not re.search(mobile_pattern, code):
                warnings.append(
                    "Ensure mobile-first approach - define base styles before breakpoints"
                )

        # Check for proper breakpoint usage
        if "sm:" in code or "md:" in code or "lg:" in code:
            # Good - using responsive modifiers
            pass
        else:
            if len(code) > 200:  # Only warn for substantial components
                warnings.append(
                    "Consider adding responsive variants for better mobile experience"
                )

        # Check for hidden elements
        if "hidden" in code and "sm:block" not in code and "md:block" not in code:
            warnings.append(
                "Hidden elements should specify when they become visible (e.g., hidden sm:block)"
            )

        return violations, warnings

    def calculate_score(
        self,
        violations: List[str],
        warnings: List[str],
        accessibility_issues: List[str]
    ) -> float:
        """Calculate compliance score (0-100)"""
        violation_penalty = len(violations) * 15
        warning_penalty = len(warnings) * 5
        accessibility_penalty = len(accessibility_issues) * 10

        score = max(0, 100 - violation_penalty - warning_penalty - accessibility_penalty)
        return round(score, 2)

    def generate_suggestions(
        self,
        violations: List[str],
        warnings: List[str],
        accessibility_issues: List[str]
    ) -> List[str]:
        """Generate helpful suggestions based on findings"""
        suggestions = []

        if any("color" in v.lower() for v in violations):
            suggestions.append(
                "Use CSS custom properties (var(--accent)) or approved design tokens for colors"
            )

        if any("font" in v.lower() for v in violations):
            suggestions.append(
                f"Use {self.guidelines.font_family} font family with weights 400, 500, or 600"
            )

        if any("spacing" in v.lower() for v in violations):
            suggestions.append(
                "Use Tailwind spacing scale (p-6, p-10, etc.) instead of custom pixel values"
            )

        if any("responsive" in w.lower() for w in warnings):
            suggestions.append(
                "Implement mobile-first responsive design with sm:, md:, lg: breakpoints"
            )

        if any("transition" in w.lower() for w in warnings):
            suggestions.append(
                "Add transition-smooth class and hover effects for interactive elements"
            )

        if accessibility_issues:
            suggestions.append(
                "Review accessibility checklist: focus indicators, alt text, heading hierarchy, touch targets"
            )

        return suggestions

    def validate(self, code: str) -> ValidationResult:
        """
        Perform complete design system validation
        Returns: ValidationResult
        """
        all_violations = []
        all_warnings = []

        # Run all validation checks
        color_v, color_w = self.validate_colors(code)
        all_violations.extend(color_v)
        all_warnings.extend(color_w)

        typo_v, typo_w = self.validate_typography(code)
        all_violations.extend(typo_v)
        all_warnings.extend(typo_w)

        spacing_v, spacing_w = self.validate_spacing(code)
        all_violations.extend(spacing_v)
        all_warnings.extend(spacing_w)

        component_v, component_w = self.validate_component_patterns(code)
        all_violations.extend(component_v)
        all_warnings.extend(component_w)

        responsive_v, responsive_w = self.validate_responsive_design(code)
        all_violations.extend(responsive_v)
        all_warnings.extend(responsive_w)

        accessibility_issues = self.validate_accessibility(code)

        # Calculate score and generate suggestions
        score = self.calculate_score(all_violations, all_warnings, accessibility_issues)
        suggestions = self.generate_suggestions(all_violations, all_warnings, accessibility_issues)

        return ValidationResult(
            passed=len(all_violations) == 0 and len(accessibility_issues) == 0,
            score=score,
            violations=all_violations,
            warnings=all_warnings,
            suggestions=suggestions,
            accessibility_issues=accessibility_issues,
        )


def main():
    """Example usage demonstrating design system validation"""

    # Example React component code (intentionally contains violations)
    test_code = """
    <div className="w-full max-w-7xl mx-auto bg-card rounded-xl border border-card-border">
      <div
        className="px-10 py-8 border-b-2"
        style={{
          background: 'linear-gradient(135deg, #c084fc12 0%, #c084fc05 100%)',
          borderColor: '#c084fc30'
        }}
      >
        <h1 className="text-3xl font-semibold" style={{ color: '#c084fc' }}>
          ICP Card Example
        </h1>
      </div>

      <div className="p-10 space-y-6">
        <div className="flex gap-3 flex-wrap">
          <span
            className="px-3 py-1.5 text-xs font-medium rounded-md border"
            style={{
              background: 'linear-gradient(135deg, #c084fc20 0%, #c084fc10 100%)',
              borderColor: '#c084fc40',
              color: '#c084fc'
            }}
          >
            Enterprise
          </span>
        </div>

        <button className="px-4 py-2 rounded-lg" style={{ backgroundColor: '#FF0000' }}>
          Click Me
        </button>

        <img src="logo.png" />
      </div>
    </div>
    """

    # Validate
    validator = ICPDesignValidator()
    result = validator.validate(test_code)

    # Print results
    print("=" * 70)
    print("ICP CARDS DESIGN SYSTEM VALIDATION REPORT")
    print("=" * 70)
    print(f"\nOverall Status: {'✓ PASSED' if result.passed else '✗ FAILED'}")
    print(f"Compliance Score: {result.score}/100")

    if result.violations:
        print(f"\n❌ VIOLATIONS ({len(result.violations)}):")
        for i, violation in enumerate(result.violations, 1):
            print(f"  {i}. {violation}")

    if result.warnings:
        print(f"\n⚠️  WARNINGS ({len(result.warnings)}):")
        for i, warning in enumerate(result.warnings, 1):
            print(f"  {i}. {warning}")

    if result.accessibility_issues:
        print(f"\n♿ ACCESSIBILITY ISSUES ({len(result.accessibility_issues)}):")
        for i, issue in enumerate(result.accessibility_issues, 1):
            print(f"  {i}. {issue}")

    if result.suggestions:
        print("\n💡 SUGGESTIONS:")
        for i, suggestion in enumerate(result.suggestions, 1):
            print(f"  {i}. {suggestion}")

    print("\n" + "=" * 70)

    # Return JSON for programmatic use
    return asdict(result)


if __name__ == "__main__":
    main()
