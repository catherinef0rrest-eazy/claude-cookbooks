#!/usr/bin/env python3
"""
GTM Fabric PDF Generator V2
Creates modern, sleek PDF presentations matching the CarveOutOmegaBlack design system.
Based on the ICP Cards design with dark theme, purple accents, and clean card layouts.
"""

import os
from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
from reportlab.lib.colors import Color, HexColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont


@dataclass
class GTMFabricColorsPDF:
    """GTM Fabric ICP Cards Design System Colors for PDF"""

    # Background colors (dark theme)
    background: Color = HexColor('#06040f')  # Deep purple-black
    card: Color = HexColor('#120a1f')  # Elevated card
    sidebar: Color = HexColor('#0e0817')  # Sidebar

    # Text colors
    text_primary: Color = HexColor('#f2f2f2')  # Main text (95% white)
    text_secondary: Color = HexColor('#a6a6a6')  # Secondary text (65% white)

    # Border colors
    border_default: Color = HexColor('#3a2d4f')
    border_card: Color = HexColor('#261b35')

    # Accent color
    accent: Color = HexColor('#c084fc')  # Light Purple

    # Additional utility colors
    white: Color = HexColor('#ffffff')
    black: Color = HexColor('#000000')


class GTMFabricPDFGeneratorV2:
    """Generate modern, sleek PDF presentations matching CarveOutOmegaBlack design"""

    def __init__(self, logo_path: Optional[str] = None):
        """
        Initialize PDF generator

        Args:
            logo_path: Path to GTM Fabric logo (uses white logo by default for dark theme)
        """
        self.colors = GTMFabricColorsPDF()
        self.font_family = "Helvetica"  # Built-in font

        # Page dimensions (landscape 16:9)
        self.page_width = 11 * inch  # 11 inches wide
        self.page_height = 11 * inch * (9/16)  # 16:9 ratio = 6.1875 inches

        # Set logo path
        if logo_path is None:
            # Default to white logo for dark theme
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.logo_path = os.path.join(script_dir, "gtmfabric_logo_white.png")
        else:
            self.logo_path = logo_path

        # Verify logo exists
        if not os.path.exists(self.logo_path):
            print(f"Warning: Logo not found at {self.logo_path}")
            self.logo_path = None

    def create_pdf(self, output_path: str) -> canvas.Canvas:
        """Create a new PDF canvas"""
        c = canvas.Canvas(output_path, pagesize=(self.page_width, self.page_height))
        return c

    def _apply_dark_background(self, c: canvas.Canvas):
        """Apply dark theme background to page"""
        c.setFillColor(self.colors.background)
        c.rect(0, 0, self.page_width, self.page_height, fill=1, stroke=0)

    def _add_logo(self, c: canvas.Canvas, position: str = "top-right", size: float = 0.8,
                  align_y: Optional[float] = None):
        """Add GTM Fabric logo to page

        Args:
            align_y: If provided, centers the logo vertically at this y position
        """
        if not self.logo_path:
            return

        margin = 0.5 * inch

        if align_y is not None:
            # Center logo vertically at align_y
            x = self.page_width - size * inch - margin
            y = align_y - (size * inch / 2)
        else:
            positions = {
                "top-right": (self.page_width - size * inch - margin, self.page_height - size * inch - margin),
                "top-left": (margin, self.page_height - size * inch - margin),
            }
            x, y = positions.get(position, positions["top-right"])

        try:
            c.drawImage(self.logo_path, x, y, width=size * inch, height=size * inch,
                       preserveAspectRatio=True, mask='auto')
        except Exception as e:
            print(f"Warning: Could not add logo: {e}")

    def _draw_vertical_accent_bar(self, c: canvas.Canvas, x: float, y: float, height: float):
        """Draw vertical accent bar (like in CarveOutOmegaBlack design)"""
        # Draw gradient bar (simulated with solid color since ReportLab doesn't support gradients easily)
        c.setFillColor(self.colors.accent)
        c.roundRect(x, y, 0.1 * inch, height, 0.05 * inch, fill=1, stroke=0)

    def _draw_section_header(self, c: canvas.Canvas, x: float, y: float, text: str,
                            width: float, accent_color: Optional[Color] = None):
        """Draw uppercase section header with accent underline"""
        if accent_color is None:
            accent_color = self.colors.accent

        # Header text
        c.setFont(f"{self.font_family}-Bold", 11)
        c.setFillColor(accent_color)
        c.drawString(x, y, text.upper())

        # Underline
        c.setStrokeColorRGB(accent_color.red, accent_color.green, accent_color.blue, alpha=0.3)
        c.setLineWidth(1)
        c.line(x, y - 0.1 * inch, x + width, y - 0.1 * inch)

    def _draw_card_background(self, c: canvas.Canvas, x: float, y: float,
                             width: float, height: float, accent_color: Optional[Color] = None):
        """Draw card with subtle gradient background and border"""
        if accent_color is None:
            accent_color = self.colors.accent

        # Card background
        c.setFillColor(self.colors.card)
        c.roundRect(x, y, width, height, 0.1 * inch, fill=1, stroke=0)

        # Card border
        c.setStrokeColorRGB(accent_color.red, accent_color.green, accent_color.blue, alpha=0.2)
        c.setLineWidth(1)
        c.roundRect(x, y, width, height, 0.1 * inch, fill=0, stroke=1)

    def _draw_badge(self, c: canvas.Canvas, x: float, y: float, text: str,
                   accent_color: Optional[Color] = None):
        """Draw role badge with gradient background"""
        if accent_color is None:
            accent_color = self.colors.accent

        # Measure text
        c.setFont(self.font_family, 9)
        text_width = c.stringWidth(text, self.font_family, 9)

        badge_width = text_width + 0.3 * inch
        badge_height = 0.25 * inch

        # Badge background with gradient simulation
        c.setFillColorRGB(accent_color.red, accent_color.green, accent_color.blue, alpha=0.15)
        c.roundRect(x, y, badge_width, badge_height, 0.08 * inch, fill=1, stroke=0)

        # Badge border
        c.setStrokeColorRGB(accent_color.red, accent_color.green, accent_color.blue, alpha=0.4)
        c.setLineWidth(0.5)
        c.roundRect(x, y, badge_width, badge_height, 0.08 * inch, fill=0, stroke=1)

        # Badge text
        c.setFillColor(accent_color)
        c.drawString(x + 0.15 * inch, y + 0.08 * inch, text)

        return badge_width

    def create_title_page(
        self,
        c: canvas.Canvas,
        title: str,
        subtitle: str,
        date: Optional[str] = None,
        include_logo: bool = True
    ):
        """Create modern startup UI title page with geometric grid background"""
        self._apply_dark_background(c)

        # Apply diagonal gradient overlay for modern look
        gradient_steps = 40
        start_color = HexColor('#0a0815')  # Darker purple-black
        end_color = self.colors.background  # Base background color

        for i in range(gradient_steps):
            # Diagonal gradient effect
            y = self.page_height - (i * self.page_height / gradient_steps)
            height = self.page_height / gradient_steps

            # Interpolate color
            ratio = i / gradient_steps
            r = int(start_color.red * 255 * (1 - ratio) + end_color.red * 255 * ratio)
            g = int(start_color.green * 255 * (1 - ratio) + end_color.green * 255 * ratio)
            b = int(start_color.blue * 255 * (1 - ratio) + end_color.blue * 255 * ratio)

            c.setFillColor(HexColor(f'#{r:02x}{g:02x}{b:02x}'))
            c.rect(0, y - height, self.page_width, height, fill=1, stroke=0)

        # === GEOMETRIC GRID OVERLAY ===
        # Create subtle grid pattern
        grid_color = HexColor('#1a1525')  # Subtle purple-gray
        c.setStrokeColor(grid_color)
        c.setLineWidth(0.5)
        c.setStrokeAlpha(0.3)  # Make it subtle

        # Vertical grid lines (1 inch spacing)
        for i in range(12):
            x_pos = i * inch
            c.line(x_pos, 0, x_pos, self.page_height)

        # Horizontal grid lines (1 inch spacing)
        for i in range(7):
            y_pos = i * inch
            c.line(0, y_pos, self.page_width, y_pos)

        # Reset alpha
        c.setStrokeAlpha(1.0)

        # === ACCENT ELEMENTS ===
        # Modern accent bar on left with glow effect
        c.setFillColor(self.colors.accent)
        c.setFillAlpha(0.3)  # Glow effect
        c.rect(0.25 * inch, 2.0 * inch, 0.18 * inch, 2.0 * inch, fill=1, stroke=0)

        c.setFillAlpha(1.0)  # Solid for main bar
        c.rect(0.3 * inch, 2.0 * inch, 0.08 * inch, 2.0 * inch, fill=1, stroke=0)

        # Reset alpha
        c.setFillAlpha(1.0)

        # === GTM FABRIC LOGO - Top left, prominently displayed ===
        if include_logo and self.logo_path:
            logo_width = 3.5 * inch  # Larger for better visibility
            logo_height = logo_width * 0.217  # Actual logo aspect ratio
            logo_x = 0.6 * inch
            logo_y = self.page_height - logo_height - 0.4 * inch

            try:
                c.drawImage(self.logo_path, logo_x, logo_y,
                          width=logo_width, height=logo_height,
                          preserveAspectRatio=True, mask='auto')
            except Exception as e:
                print(f"Warning: Could not add logo: {e}")

        # === CONTENT - Modern layout with asymmetric positioning ===
        content_x = 0.6 * inch
        content_width = self.page_width - 1.2 * inch

        # Title - positioned lower for modern look
        title_y = 3.8 * inch  # Lower positioning
        c.setFont(f"{self.font_family}-Bold", 44)
        c.setFillColor(self.colors.text_primary)

        # Word wrap title
        words = title.split()
        lines = []
        current_line = []

        for word in words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, f"{self.font_family}-Bold", 44) <= content_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            lines.append(' '.join(current_line))

        # Draw title lines
        y_position = title_y
        for line in lines:
            c.drawString(content_x, y_position, line)
            y_position -= 50

        # Subtitle with accent color
        y_position -= 0.2 * inch
        c.setFont(f"{self.font_family}", 22)  # Lighter weight
        c.setFillColor(self.colors.accent)  # Use accent color

        # Word wrap subtitle
        subtitle_words = subtitle.split()
        subtitle_lines = []
        current_line = []

        for word in subtitle_words:
            test_line = ' '.join(current_line + [word])
            if c.stringWidth(test_line, f"{self.font_family}", 22) <= content_width:
                current_line.append(word)
            else:
                if current_line:
                    subtitle_lines.append(' '.join(current_line))
                current_line = [word]
        if current_line:
            subtitle_lines.append(' '.join(current_line))

        for line in subtitle_lines:
            c.drawString(content_x, y_position, line)
            y_position -= 28

        # Date - minimal, bottom right
        if date:
            c.setFont(f"{self.font_family}", 12)
            c.setFillColor(self.colors.text_secondary)
            date_width = c.stringWidth(date, f"{self.font_family}", 12)
            c.drawString(self.page_width - date_width - 0.5 * inch, 0.5 * inch, date)

    def create_icp_page(
        self,
        c: canvas.Canvas,
        icp_number: int,
        icp_title: str,
        industries: List[str],
        departments: str,
        key_roles: List[str],
        displacement_signals: List[Dict[str, Any]],
        expansion_signals: List[Dict[str, Any]],
        include_logo: bool = True,
        page_number: Optional[int] = None
    ):
        """Create ICP page matching CarveOutOmegaBlack design"""
        self._apply_dark_background(c)

        # Main card
        card_x = 0.4 * inch
        card_y = 0.5 * inch
        card_width = 10.2 * inch
        card_height = 5.2 * inch

        # Card background
        self._draw_card_background(c, card_x, card_y, card_width, card_height)

        # Header with gradient background
        header_height = 0.7 * inch
        header_y = card_y + card_height - header_height

        # Header background (subtle gradient simulation)
        c.setFillColorRGB(self.colors.accent.red, self.colors.accent.green,
                         self.colors.accent.blue, alpha=0.08)
        c.rect(card_x, header_y, card_width, header_height, fill=1, stroke=0)

        # Header border
        c.setStrokeColorRGB(self.colors.accent.red, self.colors.accent.green,
                           self.colors.accent.blue, alpha=0.3)
        c.setLineWidth(2)
        c.line(card_x, header_y, card_x + card_width, header_y)

        # Title (no vertical bar)
        c.setFont(f"{self.font_family}-Bold", 22)
        c.setFillColor(self.colors.text_primary)
        c.drawString(card_x + 0.4 * inch, header_y + 0.25 * inch, icp_title)

        # Content area with increased spacing
        content_y = header_y - 0.4 * inch
        content_x = card_x + 0.4 * inch

        # Industries (if provided)
        if industries:
            industries_text = ", ".join(industries)
            c.setFont(self.font_family, 10)
            c.setFillColor(self.colors.text_secondary)
            c.drawString(content_x, content_y, f"Industries: {industries_text}")
            content_y -= 0.35 * inch

        # Departments & Functions
        self._draw_section_header(c, content_x, content_y, "DEPARTMENTS & FUNCTIONS",
                                  card_width - 0.8 * inch)
        content_y -= 0.35 * inch

        c.setFont(self.font_family, 10)
        c.setFillColor(self.colors.text_secondary)
        c.drawString(content_x, content_y, departments)
        content_y -= 0.4 * inch

        # Key Roles as badges
        if key_roles:
            badge_x = content_x
            badge_y = content_y

            for i, role in enumerate(key_roles[:6]):  # Limit to 6 roles for space
                badge_width = self._draw_badge(c, badge_x, badge_y, role)
                badge_x += badge_width + 0.2 * inch

                # Wrap to next line if needed
                if badge_x > card_x + card_width - 1.5 * inch:
                    badge_x = content_x
                    badge_y -= 0.4 * inch

            content_y = badge_y - 0.5 * inch

        # Technographic Fit header
        self._draw_section_header(c, content_x, content_y, "TECHNOGRAPHIC FIT",
                                  card_width - 0.8 * inch)
        content_y -= 0.4 * inch

        # Two-column layout for signals
        col_width = (card_width - 1.2 * inch) / 2
        left_col_x = content_x
        right_col_x = content_x + col_width + 0.4 * inch

        # Legacy Indicators (left column)
        c.setFont(f"{self.font_family}-Bold", 11)
        c.setFillColor(self.colors.text_primary)
        c.drawString(left_col_x, content_y, "Legacy Indicators")

        signal_y = content_y - 0.2 * inch
        for signal in displacement_signals[:2]:  # Limit to 2 for space
            vendors = ", ".join(signal.get("vendor_products", []))

            # Signal card
            signal_card_height = 0.5 * inch
            c.setFillColorRGB(self.colors.card.red, self.colors.card.green,
                             self.colors.card.blue, alpha=0.5)
            c.roundRect(left_col_x, signal_y - signal_card_height, col_width,
                       signal_card_height, 0.05 * inch, fill=1, stroke=1)

            # Description
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_primary)

            # Word wrap description
            desc = signal.get('pain_explanation', '')
            if len(desc) > 50:
                desc = desc[:47] + "..."
            c.drawString(left_col_x + 0.1 * inch, signal_y - 0.15 * inch, desc)

            # Tools
            c.setFont(f"{self.font_family}", 8)
            c.setFillColor(self.colors.text_secondary)
            c.drawString(left_col_x + 0.1 * inch, signal_y - 0.35 * inch, f"→ {vendors}")

            signal_y -= 0.6 * inch

        # Expansion Signals (right column)
        signal_y = content_y - 0.2 * inch
        c.setFont(f"{self.font_family}-Bold", 11)
        c.setFillColor(self.colors.text_primary)
        c.drawString(right_col_x, content_y, "Expansion Signals")

        for signal in expansion_signals[:2]:  # Limit to 2 for space
            vendors = ", ".join(signal.get("vendor_products", []))

            # Signal card
            signal_card_height = 0.5 * inch
            c.setFillColorRGB(self.colors.card.red, self.colors.card.green,
                             self.colors.card.blue, alpha=0.5)
            c.roundRect(right_col_x, signal_y - signal_card_height, col_width,
                       signal_card_height, 0.05 * inch, fill=1, stroke=1)

            # Description
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_primary)

            desc = signal.get('readiness_explanation', '')
            if len(desc) > 50:
                desc = desc[:47] + "..."
            c.drawString(right_col_x + 0.1 * inch, signal_y - 0.15 * inch, desc)

            # Tools
            c.setFont(f"{self.font_family}", 8)
            c.setFillColor(self.colors.text_secondary)
            c.drawString(right_col_x + 0.1 * inch, signal_y - 0.35 * inch, f"→ {vendors}")

            signal_y -= 0.6 * inch

        # Add logo aligned with header (drawn last so it appears on top)
        if include_logo:
            header_center_y = header_y + header_height / 2
            self._add_logo(c, position="top-right", size=1.8, align_y=header_center_y)

        # Footer
        if page_number:
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_secondary)
            footer_text = f"GTM Fabric | Page {page_number}"
            text_width = c.stringWidth(footer_text, self.font_family, 9)
            c.drawString((self.page_width - text_width) / 2, 0.3 * inch, footer_text)

    def create_e2e_slide(
        self,
        c: canvas.Canvas,
        include_logo: bool = True,
        page_number: Optional[int] = None
    ):
        """Create E2E (End-to-End) Use Case Solutions slide"""
        self._apply_dark_background(c)

        # Main card
        card_x = 0.4 * inch
        card_y = 0.5 * inch
        card_width = 10.2 * inch
        card_height = 5.2 * inch

        self._draw_card_background(c, card_x, card_y, card_width, card_height)

        # Header
        header_height = 0.6 * inch
        header_y = card_y + card_height - header_height

        c.setFillColorRGB(self.colors.accent.red, self.colors.accent.green,
                         self.colors.accent.blue, alpha=0.08)
        c.rect(card_x, header_y, card_width, header_height, fill=1, stroke=0)

        c.setStrokeColorRGB(self.colors.accent.red, self.colors.accent.green,
                           self.colors.accent.blue, alpha=0.3)
        c.setLineWidth(2)
        c.line(card_x, header_y, card_x + card_width, header_y)

        # Title
        c.setFont(f"{self.font_family}-Bold", 20)
        c.setFillColor(self.colors.text_primary)
        c.drawString(card_x + 0.4 * inch, header_y + 0.2 * inch,
                    "Key Elements Required For E2E Use Case Solutions")

        # Content area with 4 circles and center logo
        content_y = header_y - 0.5 * inch
        center_x = card_x + card_width / 2
        center_y = content_y - 1.8 * inch

        # Draw 4 circles in 2x2 grid
        circle_radius = 0.5 * inch
        circle_spacing = 3.8 * inch  # Adjusted to position circles close to center while avoiding logo overlap

        circles = [
            {"x": center_x - circle_spacing/2, "y": center_y + circle_spacing/2,
             "label": "Data &\nInsights", "color": HexColor('#3498db')},
            {"x": center_x + circle_spacing/2, "y": center_y + circle_spacing/2,
             "label": "Workflow &\nPlatforms", "color": HexColor('#27ae60')},
            {"x": center_x - circle_spacing/2, "y": center_y - circle_spacing/2,
             "label": "Experts &\nBlueprints", "color": HexColor('#e74c3c')},
            {"x": center_x + circle_spacing/2, "y": center_y - circle_spacing/2,
             "label": "Services &\nSkills", "color": HexColor('#f1c40f')},
        ]

        # Draw circles
        for circle in circles:
            # Outer circle with glow
            c.setStrokeColor(circle["color"])
            c.setLineWidth(2)
            c.circle(circle["x"], circle["y"], circle_radius, fill=0, stroke=1)

            # Inner circle
            c.setFillColorRGB(self.colors.card.red, self.colors.card.green,
                             self.colors.card.blue, alpha=0.8)
            c.circle(circle["x"], circle["y"], circle_radius - 0.1 * inch, fill=1, stroke=0)

            # Label - ensure proper centering
            lines = circle["label"].split('\n')
            c.setFont(f"{self.font_family}-Bold", 10)
            c.setFillColor(self.colors.text_primary)
            # Center text vertically in circle
            y_offset = 0.08 * inch if len(lines) > 1 else 0
            for i, line in enumerate(lines):
                text_width = c.stringWidth(line, f"{self.font_family}-Bold", 10)
                # Center horizontally and vertically
                c.drawString(circle["x"] - text_width/2,
                           circle["y"] + y_offset - i * 0.15 * inch, line)

        # Left side content (moved further left to avoid circle overlap)
        left_col_x = card_x + 0.3 * inch
        left_col_width = 2.8 * inch

        # Right side content positions
        right_col_x = center_x + 2.2 * inch
        right_col_width = 2.8 * inch

        # Top left items (aligned with top circles)
        top_left_items = [
            "Neutral vendor mgmt (source / vet / negotiate)",
            "Compelling value of complementary data",
            "Harmonization (integrated ontology)",
            "Flexible & scalable pricing model",
            "1st/2nd/3rd party data integration",
            "Data and insights licensing options",
            "Evergreen refresh and resilience",
            "Integrity assurance"
        ]

        top_y = content_y - 0.3 * inch
        y_pos = top_y
        c.setFont(self.font_family, 10)
        c.setFillColor(self.colors.text_primary)
        for item in top_left_items[:6]:  # Limit for space
            c.drawString(left_col_x, y_pos, f"• {item}")
            y_pos -= 0.18 * inch

        # Bottom left items
        bottom_left_items = [
            "Practical examples, case studies & blueprints",
            "Proof points (economic outcomes)",
            "Success factors & watch outs",
            "Board-level credibility & fluency"
        ]

        bottom_y_start = center_y - 1.0 * inch
        y_pos = bottom_y_start
        for item in bottom_left_items:
            c.drawString(left_col_x, y_pos, f"• {item}")
            y_pos -= 0.18 * inch
        bottom_y_end = y_pos + 0.18 * inch

        # Top right items
        top_right_items = [
            "Architecture & design",
            "Integration & customization",
            "Analytical tools & visualization",
            "AI reference framework (MCP)",
            "LLM training & governance",
            "Agentic processes & automation"
        ]

        y_pos = top_y
        for item in top_right_items:
            c.drawString(right_col_x, y_pos, f"• {item}")
            y_pos -= 0.18 * inch

        # Bottom right items
        bottom_right_items = [
            "Project management / oversight",
            "Strategic vision & design",
            "Process optimization & re-imagination",
            "Training & enablement",
            "Change management / comms",
            "Demand Generation / engagement",
            "Customer Success / maintenance"
        ]

        y_pos = bottom_y_start
        for item in bottom_right_items[:5]:  # Limit for space
            c.drawString(right_col_x, y_pos, f"• {item}")
            y_pos -= 0.18 * inch

        # Draw dashed cross lines AFTER text so they're visible but don't obscure
        # Extend from left edge of left text to right edge of right text
        c.setStrokeColor(HexColor('#5a4d6f'))  # Medium purple-gray for subtle visibility
        c.setLineWidth(1.5)  # Slightly thicker than default but not too bold
        c.setDash(5, 3)  # Medium dashes: 5 points on, 3 points off

        # Horizontal line through center (extends to edges of text areas)
        h_line_left = left_col_x - 0.1 * inch
        h_line_right = right_col_x + right_col_width + 0.1 * inch
        c.line(h_line_left, center_y, h_line_right, center_y)

        # Vertical line through center (extends from top to bottom of text areas)
        v_line_top = top_y + 0.15 * inch
        v_line_bottom = bottom_y_end - 0.2 * inch
        c.line(center_x, v_line_top, center_x, v_line_bottom)

        # Reset to solid line
        c.setDash()

        # Add top-right logo aligned with header (drawn after card so it's visible)
        if include_logo:
            header_center_y = header_y + header_height / 2
            self._add_logo(c, position="top-right", size=1.8, align_y=header_center_y)

        # Center logo (white GTM Fabric logo) - drawn last to be on top
        if self.logo_path and os.path.exists(self.logo_path):
            logo_size = 2.5 * inch
            try:
                c.drawImage(self.logo_path,
                           center_x - logo_size/2,
                           center_y - logo_size/2,
                           width=logo_size,
                           height=logo_size,
                           preserveAspectRatio=True,
                           mask='auto')
            except Exception as e:
                # Fallback to text if logo fails
                c.setFont(f"{self.font_family}-Bold", 14)
                c.setFillColor(self.colors.accent)
                logo_text = "GTM Fabric"
                text_width = c.stringWidth(logo_text, f"{self.font_family}-Bold", 14)
                c.drawString(center_x - text_width/2, center_y, logo_text)
        else:
            # Fallback to text if no logo
            c.setFont(f"{self.font_family}-Bold", 14)
            c.setFillColor(self.colors.accent)
            logo_text = "GTM Fabric"
            text_width = c.stringWidth(logo_text, f"{self.font_family}-Bold", 14)
            c.drawString(center_x - text_width/2, center_y, logo_text)

        # Footer
        if page_number:
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_secondary)
            footer_text = f"GTM Fabric | Page {page_number}"
            text_width = c.stringWidth(footer_text, self.font_family, 9)
            c.drawString((self.page_width - text_width) / 2, 0.3 * inch, footer_text)

    def create_propensity_funnel_slide(
        self,
        c: canvas.Canvas,
        include_logo: bool = True,
        page_number: Optional[int] = None
    ):
        """Create Propensity Funnel slide"""
        self._apply_dark_background(c)

        # Main card
        card_x = 0.4 * inch
        card_y = 0.5 * inch
        card_width = 10.2 * inch
        card_height = 5.2 * inch

        self._draw_card_background(c, card_x, card_y, card_width, card_height)

        # Header
        header_height = 0.6 * inch
        header_y = card_y + card_height - header_height

        c.setFillColorRGB(self.colors.accent.red, self.colors.accent.green,
                         self.colors.accent.blue, alpha=0.08)
        c.rect(card_x, header_y, card_width, header_height, fill=1, stroke=0)

        c.setStrokeColorRGB(self.colors.accent.red, self.colors.accent.green,
                           self.colors.accent.blue, alpha=0.3)
        c.setLineWidth(2)
        c.line(card_x, header_y, card_x + card_width, header_y)

        # Title
        c.setFont(f"{self.font_family}-Bold", 22)
        c.setFillColor(self.colors.text_primary)
        c.drawString(card_x + 0.4 * inch, header_y + 0.2 * inch, "Propensity Funnel")

        # Two-column layout
        content_y = header_y - 0.4 * inch
        left_col_x = card_x + 0.4 * inch
        left_col_width = 4.5 * inch
        right_col_x = left_col_x + left_col_width + 0.5 * inch
        right_col_width = 4.5 * inch

        # Left side - Level details
        levels = [
            {"title": "Market to Account View",
             "desc": ["TAM-SAM-SOM", "Spend Potential"]},
            {"title": "Account to Product View",
             "desc": ["Competitive Install Base", "Partner Install Base"]},
            {"title": "Product to User View",
             "desc": ["Departments To Target", "In Which Locations"]},
            {"title": "User to Contact Data",
             "desc": ["Emails, Phone Numbers", "Socials"]},
        ]

        y_pos = content_y
        for i, level in enumerate(levels):
            box_height = 0.8 * inch

            # Level box with gradient
            c.setFillColorRGB(self.colors.accent.red, self.colors.accent.green,
                             self.colors.accent.blue, alpha=0.15 - i * 0.02)
            c.roundRect(left_col_x, y_pos - box_height, left_col_width, box_height,
                       0.08 * inch, fill=1, stroke=0)

            c.setStrokeColorRGB(self.colors.accent.red, self.colors.accent.green,
                               self.colors.accent.blue, alpha=0.3 + i * 0.05)
            c.setLineWidth(1)
            c.roundRect(left_col_x, y_pos - box_height, left_col_width, box_height,
                       0.08 * inch, fill=0, stroke=1)

            # Title
            c.setFont(f"{self.font_family}-Bold", 11)
            c.setFillColor(self.colors.text_primary)
            c.drawString(left_col_x + 0.2 * inch, y_pos - 0.25 * inch, level["title"])

            # Description bullets
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_secondary)
            for j, desc in enumerate(level["desc"]):
                c.drawString(left_col_x + 0.25 * inch, y_pos - 0.45 * inch - j * 0.15 * inch,
                           f"• {desc}")

            y_pos -= box_height + 0.15 * inch

        # Right side - Funnel visualization
        funnel_levels = [
            "4.4M companies, $127bn annually",
            "11,759 using IBM QRadar",
            "724 intent: Ransomware + SIEM",
            "Contacts by Dept, Location, Seniority"
        ]

        y_pos = content_y
        for i, text in enumerate(funnel_levels):
            width_percent = 1.0 - (i * 0.18)
            box_width = right_col_width * width_percent
            box_height = 0.6 * inch
            box_x = right_col_x + (right_col_width - box_width) / 2

            # Funnel box
            c.setFillColorRGB(self.colors.accent.red, self.colors.accent.green,
                             self.colors.accent.blue, alpha=0.20 - i * 0.03)
            c.roundRect(box_x, y_pos - box_height, box_width, box_height,
                       0.08 * inch, fill=1, stroke=0)

            c.setStrokeColorRGB(self.colors.accent.red, self.colors.accent.green,
                               self.colors.accent.blue, alpha=0.5 + i * 0.1)
            c.setLineWidth(2)
            c.roundRect(box_x, y_pos - box_height, box_width, box_height,
                       0.08 * inch, fill=0, stroke=1)

            # Text (with progressive font sizing and word wrapping for narrow levels)
            # Use smaller font for narrower funnels
            if i >= 3:
                font_size = 8  # Smaller for level 4
            elif i >= 2:
                font_size = 8.5
            else:
                font_size = 9

            c.setFont(f"{self.font_family}-Bold", font_size)
            c.setFillColor(self.colors.text_primary)

            # Check if text needs wrapping (for narrow funnel levels)
            text_width = c.stringWidth(text, f"{self.font_family}-Bold", font_size)
            max_text_width = box_width - 0.3 * inch  # Increased padding for better margins

            if text_width > max_text_width:
                # Word wrap the text
                words = text.split()
                lines = []
                current_line = []

                for word in words:
                    test_line = ' '.join(current_line + [word])
                    test_width = c.stringWidth(test_line, f"{self.font_family}-Bold", font_size)
                    if test_width <= max_text_width:
                        current_line.append(word)
                    else:
                        if current_line:
                            lines.append(' '.join(current_line))
                        current_line = [word]
                if current_line:
                    lines.append(' '.join(current_line))

                # Draw wrapped lines
                line_height = 0.11 * inch  # Slightly tighter line spacing
                start_y = y_pos - 0.3 * inch + ((len(lines) - 1) * line_height / 2)
                for j, line in enumerate(lines):
                    line_width = c.stringWidth(line, f"{self.font_family}-Bold", font_size)
                    c.drawString(box_x + (box_width - line_width) / 2, start_y - j * line_height, line)
            else:
                # Single line - center it
                c.drawString(box_x + (box_width - text_width) / 2, y_pos - 0.35 * inch, text)

            # Level number
            c.setFont(self.font_family, 8)
            c.setFillColor(self.colors.text_secondary)
            level_text = f"Level {i + 1}"
            level_width = c.stringWidth(level_text, self.font_family, 8)
            c.drawString(box_x + (box_width - level_width) / 2, y_pos - 0.5 * inch, level_text)

            # Arrow between levels
            if i < len(funnel_levels) - 1:
                arrow_y = y_pos - box_height - 0.15 * inch
                c.setStrokeColor(self.colors.accent)
                c.setLineWidth(2)
                arrow_x = right_col_x + right_col_width / 2
                c.line(arrow_x, arrow_y + 0.1 * inch, arrow_x, arrow_y - 0.05 * inch)
                # Arrowhead
                c.line(arrow_x, arrow_y - 0.05 * inch, arrow_x - 0.05 * inch, arrow_y)
                c.line(arrow_x, arrow_y - 0.05 * inch, arrow_x + 0.05 * inch, arrow_y)

            y_pos -= box_height + 0.25 * inch

        # Add logo aligned with header (drawn last so it appears on top)
        if include_logo:
            header_center_y = header_y + header_height / 2
            self._add_logo(c, position="top-right", size=1.8, align_y=header_center_y)

        # Footer
        if page_number:
            c.setFont(self.font_family, 9)
            c.setFillColor(self.colors.text_secondary)
            footer_text = f"GTM Fabric | Page {page_number}"
            text_width = c.stringWidth(footer_text, self.font_family, 9)
            c.drawString((self.page_width - text_width) / 2, 0.3 * inch, footer_text)


def generate_icp_pdf_v2(
    campaign_info: Dict[str, str],
    icps: List[Dict[str, Any]],
    output_path: str,
    include_logo: bool = True
) -> str:
    """Generate complete ICP PDF with CarveOutOmegaBlack design"""
    generator = GTMFabricPDFGeneratorV2()
    c = generator.create_pdf(output_path)

    # Title page
    generator.create_title_page(
        c,
        title=f"{campaign_info['customer_name']} - Ideal Customer Profiles",
        subtitle=f"{campaign_info['solution_name']} GTM Campaign",
        date=campaign_info.get('campaign_date'),
        include_logo=include_logo
    )
    c.showPage()

    # E2E slide (page 2)
    generator.create_e2e_slide(c, include_logo=include_logo, page_number=2)
    c.showPage()

    # Propensity Funnel slide (page 3)
    generator.create_propensity_funnel_slide(c, include_logo=include_logo, page_number=3)
    c.showPage()

    # ICP pages (starting from page 4)
    for idx, icp in enumerate(icps, start=1):
        generator.create_icp_page(
            c,
            icp_number=icp['icp_number'],
            icp_title=icp['title'],
            industries=icp.get('industries', []),
            departments=icp['departments_and_functions'],
            key_roles=icp['key_roles'],
            displacement_signals=icp['technographic_fit']['displacement_signals'],
            expansion_signals=icp['technographic_fit']['expansion_signals'],
            include_logo=include_logo,
            page_number=idx + 3  # Start from page 4 (after title, E2E, and funnel)
        )
        c.showPage()

    c.save()
    print(f"✓ PDF saved to: {output_path}")
    return output_path
