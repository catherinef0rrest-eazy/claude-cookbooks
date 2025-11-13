"""
ICP Cards Design System Module
Provides design tokens, utilities, and helpers for applying GTM Fabric visual design system.
Focused on React/TypeScript applications with Tailwind CSS.
"""

from typing import Dict, Any, List, Literal
from dataclasses import dataclass, field


@dataclass
class DesignTokens:
    """Core design tokens for ICP Cards design system."""

    # Background colors (dark theme)
    colors_background: Dict[str, str] = field(default_factory=lambda: {
        "base": "hsl(257, 47%, 4%)",       # #06040f - Deep purple-black
        "card": "hsl(257, 35%, 8%)",       # #120a1f - Elevated card
        "sidebar": "hsl(257, 40%, 6%)",    # #0e0817 - Sidebar
    })

    # Foreground colors
    colors_foreground: Dict[str, str] = field(default_factory=lambda: {
        "primary": "hsl(0, 0%, 95%)",      # #f2f2f2 - Main text
        "secondary": "hsl(0, 0%, 65%)",    # #a6a6a6 - Supporting text
        "card": "hsl(0, 0%, 95%)",         # #f2f2f2 - Card text
    })

    # Border colors
    colors_border: Dict[str, str] = field(default_factory=lambda: {
        "default": "hsl(257, 20%, 18%)",   # #3a2d4f
        "card": "hsl(257, 25%, 14%)",      # #261b35
        "sidebar": "hsl(257, 30%, 12%)",   # #201629
    })

    # Accent color (Light Purple)
    accent_primary: str = "#c084fc"

    # Typography
    font_primary: str = "Arial"
    font_fallback: List[str] = field(default_factory=lambda: ["sans-serif"])

    # Font sizes (mobile → desktop)
    font_sizes: Dict[str, Dict[str, str]] = field(default_factory=lambda: {
        "h1": {"mobile": "1.25rem", "desktop": "1.875rem"},  # 20px → 30px
        "h2": {"mobile": "1.5rem", "desktop": "2.25rem"},    # 24px → 36px
        "h3": {"mobile": "1rem", "desktop": "1rem"},         # 16px
        "body": {"mobile": "0.875rem", "desktop": "0.875rem"},  # 14px
        "small": {"mobile": "0.75rem", "desktop": "0.75rem"},   # 12px
    })

    # Font weights
    font_weights: Dict[str, int] = field(default_factory=lambda: {
        "regular": 400,
        "medium": 500,
        "semibold": 600,
    })

    # Spacing scale (in rem)
    spacing: Dict[str, str] = field(default_factory=lambda: {
        "xs": "0.5rem",   # 8px
        "sm": "0.75rem",  # 12px
        "md": "1rem",     # 16px
        "lg": "1.5rem",   # 24px
        "xl": "2rem",     # 32px
        "2xl": "2.5rem",  # 40px
        "3xl": "3rem",    # 48px
        "4xl": "4rem",    # 64px
    })

    # Breakpoints
    breakpoints: Dict[str, str] = field(default_factory=lambda: {
        "sm": "640px",
        "md": "768px",
        "lg": "1024px",
        "xl": "1280px",
    })


class ICPDesignSystem:
    """ICP Cards Visual Design System - Helper functions and utilities."""

    def __init__(self):
        """Initialize design system with standard tokens."""
        self.tokens = DesignTokens()

    def get_accent_with_opacity(self, opacity: int) -> str:
        """
        Get accent color with opacity suffix for Tailwind.

        Args:
            opacity: Opacity value (5, 8, 10, 12, 20, 30, 40, 100)

        Returns:
            Color with opacity suffix for use in inline styles

        Example:
            get_accent_with_opacity(20) -> "#c084fc20"
        """
        valid_opacities = [5, 8, 10, 12, 20, 30, 40, 100]
        if opacity not in valid_opacities:
            raise ValueError(f"Opacity must be one of {valid_opacities}")

        if opacity == 100:
            return self.tokens.accent_primary

        # Convert to hex opacity (e.g., 20% -> 33 in hex)
        hex_opacity = format(int(opacity * 2.55), '02x')
        return f"{self.tokens.accent_primary}{hex_opacity}"

    def get_gradient_header(self, accent_color: str) -> Dict[str, str]:
        """
        Generate card header gradient pattern.

        Args:
            accent_color: Accent color hex code

        Returns:
            Dict with background gradient CSS value
        """
        return {
            "background": f"linear-gradient(135deg, {accent_color}12 0%, {accent_color}05 100%)"
        }

    def get_gradient_badge(self, accent_color: str) -> Dict[str, str]:
        """
        Generate badge/chip gradient pattern.

        Args:
            accent_color: Accent color hex code

        Returns:
            Dict with background gradient CSS value
        """
        return {
            "background": f"linear-gradient(135deg, {accent_color}20 0%, {accent_color}10 100%)"
        }

    def get_gradient_subsection(self, accent_color: str) -> Dict[str, str]:
        """
        Generate subsection container gradient pattern.

        Args:
            accent_color: Accent color hex code

        Returns:
            Dict with background gradient CSS value
        """
        return {
            "background": f"linear-gradient(135deg, {accent_color}08 0%, {accent_color}03 100%)"
        }

    def get_card_hover_shadow(self, accent_color: str = "#c084fc") -> str:
        """
        Generate card hover shadow effect.

        Args:
            accent_color: Accent color hex code (default: purple)

        Returns:
            Box shadow CSS value
        """
        return f"0 20px 60px rgba(192, 132, 252, 0.12), 0 0 30px rgba(192, 132, 252, 0.04)"

    def get_funnel_level_width(self, index: int) -> int:
        """
        Calculate funnel level width percentage.

        Args:
            index: Zero-based funnel level index (0-3)

        Returns:
            Width percentage (100, 82, 64, 46)
        """
        return 100 - (index * 18)

    def get_funnel_level_style(self, index: int, accent_color: str) -> Dict[str, Any]:
        """
        Generate complete funnel level styling.

        Args:
            index: Zero-based funnel level index
            accent_color: Accent color hex code

        Returns:
            Dict with width, background, border, and shadow styles
        """
        width_percent = self.get_funnel_level_width(index)
        opacity = 40 - (index * 8)
        border_opacity = 50 + (index * 10)
        shadow_opacity_1 = 20 - (index * 3)
        shadow_opacity_2 = 15 - (index * 3)

        return {
            "width": f"{width_percent}%",
            "background": f"linear-gradient(135deg, {accent_color}{opacity:02d} 0%, {accent_color}{opacity-20:02d} 100%)",
            "border": f"2px solid {accent_color}{border_opacity}",
            "boxShadow": f"0 4px 20px {accent_color}{shadow_opacity_1:02d}, 0 0 30px {accent_color}{shadow_opacity_2:02d}",
        }

    def get_tailwind_classes(
        self,
        component_type: Literal["card", "badge", "section_header", "indicator"]
    ) -> str:
        """
        Get recommended Tailwind classes for common components.

        Args:
            component_type: Type of component

        Returns:
            Space-separated Tailwind class string
        """
        classes = {
            "card": "w-full max-w-7xl mx-auto bg-card rounded-xl overflow-hidden border border-card-border transition-smooth hover:scale-[1.02]",
            "badge": "px-3 py-1.5 text-xs font-medium rounded-md border",
            "section_header": "pb-3 border-b text-base font-semibold uppercase tracking-wider",
            "indicator": "p-3 rounded-md bg-card border border-border space-y-2",
        }
        return classes.get(component_type, "")

    def get_responsive_padding(self, size: Literal["small", "medium", "large"]) -> str:
        """
        Get responsive padding classes (mobile → desktop).

        Args:
            size: Padding size category

        Returns:
            Tailwind responsive padding classes
        """
        padding = {
            "small": "p-4 sm:p-6",
            "medium": "p-6 sm:p-10",
            "large": "p-8 sm:p-12",
        }
        return padding.get(size, padding["medium"])

    def get_responsive_spacing(self, size: Literal["tight", "normal", "loose"]) -> str:
        """
        Get responsive vertical spacing classes (mobile → desktop).

        Args:
            size: Spacing category

        Returns:
            Tailwind responsive space-y classes
        """
        spacing = {
            "tight": "space-y-3 sm:space-y-5",
            "normal": "space-y-6 sm:space-y-10",
            "loose": "space-y-8 sm:space-y-16",
        }
        return spacing.get(size, spacing["normal"])

    def get_responsive_text(self, level: Literal["h1", "h2", "h3", "body"]) -> str:
        """
        Get responsive typography classes (mobile → desktop).

        Args:
            level: Typography level

        Returns:
            Tailwind responsive text size classes
        """
        text = {
            "h1": "text-xl sm:text-3xl font-semibold",
            "h2": "text-2xl sm:text-4xl font-semibold",
            "h3": "text-base font-semibold",
            "body": "text-sm",
        }
        return text.get(level, text["body"])

    def generate_css_custom_properties(self) -> str:
        """
        Generate CSS custom properties for the design system.

        Returns:
            CSS :root declaration with all design tokens
        """
        css = ":root {\n"

        # Background colors
        css += "  /* Background Colors */\n"
        css += f"  --background: {self.tokens.colors_background['base']};\n"
        css += f"  --card: {self.tokens.colors_background['card']};\n"
        css += f"  --sidebar: {self.tokens.colors_background['sidebar']};\n"

        # Foreground colors
        css += "\n  /* Foreground Colors */\n"
        css += f"  --foreground: {self.tokens.colors_foreground['primary']};\n"
        css += f"  --muted-foreground: {self.tokens.colors_foreground['secondary']};\n"
        css += f"  --card-foreground: {self.tokens.colors_foreground['card']};\n"

        # Border colors
        css += "\n  /* Border Colors */\n"
        css += f"  --border: {self.tokens.colors_border['default']};\n"
        css += f"  --card-border: {self.tokens.colors_border['card']};\n"
        css += f"  --sidebar-border: {self.tokens.colors_border['sidebar']};\n"

        # Accent
        css += "\n  /* Accent */\n"
        css += f"  --accent: {self.tokens.accent_primary};\n"

        # Typography
        css += "\n  /* Typography */\n"
        css += f"  --font-primary: {self.tokens.font_primary}, {', '.join(self.tokens.font_fallback)};\n"

        css += "}\n"
        return css

    def generate_tailwind_config(self) -> Dict[str, Any]:
        """
        Generate Tailwind CSS configuration object.

        Returns:
            Dict containing theme extension for tailwind.config.js
        """
        return {
            "theme": {
                "extend": {
                    "colors": {
                        "background": self.tokens.colors_background["base"],
                        "card": self.tokens.colors_background["card"],
                        "sidebar": self.tokens.colors_background["sidebar"],
                        "foreground": self.tokens.colors_foreground["primary"],
                        "muted-foreground": self.tokens.colors_foreground["secondary"],
                        "border": self.tokens.colors_border["default"],
                        "card-border": self.tokens.colors_border["card"],
                        "accent": self.tokens.accent_primary,
                    },
                    "fontFamily": {
                        "primary": [self.tokens.font_primary] + self.tokens.font_fallback,
                    },
                    "spacing": self.tokens.spacing,
                    "screens": self.tokens.breakpoints,
                }
            }
        }

    def validate_accessibility(self, background: str, foreground: str) -> Dict[str, Any]:
        """
        Validate color contrast for accessibility (simplified).

        Args:
            background: Background color (hex or hsl)
            foreground: Foreground color (hex or hsl)

        Returns:
            Dict with validation results

        Note:
            This is a simplified validator. For production, use a proper
            contrast ratio calculator that converts HSL/hex to luminance.
        """
        # Known compliant combinations from design system
        compliant_pairs = [
            (self.tokens.colors_background["base"], self.tokens.colors_foreground["primary"]),  # ~16:1
            (self.tokens.colors_background["card"], self.tokens.colors_foreground["primary"]),  # ~16:1
            (self.tokens.colors_background["base"], self.tokens.colors_foreground["secondary"]),  # ~7:1
        ]

        is_compliant = (background, foreground) in compliant_pairs

        return {
            "passed": is_compliant,
            "level": "AAA" if is_compliant and "95%" in foreground else "AA",
            "recommendation": "Ensure minimum 4.5:1 ratio for body text, 3:1 for large text",
        }


def generate_component_example(component_type: str, accent_color: str = "#c084fc") -> Dict[str, str]:
    """
    Generate React component example with proper styling.

    Args:
        component_type: Type of component (card, badge, section_header)
        accent_color: Accent color hex code

    Returns:
        Dict with className and style props
    """
    system = ICPDesignSystem()

    if component_type == "card":
        return {
            "className": system.get_tailwind_classes("card"),
            "style": {},
        }

    elif component_type == "card_header":
        gradient = system.get_gradient_header(accent_color)
        return {
            "className": "px-6 sm:px-10 py-6 sm:py-8 border-b-2",
            "style": {
                "background": gradient["background"],
                "borderColor": f"{accent_color}30",
            },
        }

    elif component_type == "badge":
        gradient = system.get_gradient_badge(accent_color)
        return {
            "className": system.get_tailwind_classes("badge"),
            "style": {
                "background": gradient["background"],
                "borderColor": f"{accent_color}40",
                "color": accent_color,
            },
        }

    elif component_type == "section_header":
        return {
            "className": system.get_tailwind_classes("section_header"),
            "style": {
                "borderColor": f"{accent_color}20",
                "color": accent_color,
            },
        }

    else:
        return {"className": "", "style": {}}


# Example usage
if __name__ == "__main__":
    system = ICPDesignSystem()

    print("=== ICP Cards Design System ===\n")

    # Generate CSS custom properties
    print("CSS Custom Properties:")
    print(system.generate_css_custom_properties())

    # Generate component examples
    print("\nCard Header Example:")
    card_header = generate_component_example("card_header", "#c084fc")
    print(f"  className: {card_header['className']}")
    print(f"  style: {card_header['style']}")

    print("\nBadge Example:")
    badge = generate_component_example("badge", "#c084fc")
    print(f"  className: {badge['className']}")
    print(f"  style: {badge['style']}")

    print("\nFunnel Level Styling (Level 1):")
    funnel_style = system.get_funnel_level_style(1, "#c084fc")
    print(f"  {funnel_style}")

    print("\nAccessibility Check:")
    result = system.validate_accessibility(
        system.tokens.colors_background["base"],
        system.tokens.colors_foreground["primary"]
    )
    print(f"  Passed: {result['passed']}")
    print(f"  Level: {result['level']}")
