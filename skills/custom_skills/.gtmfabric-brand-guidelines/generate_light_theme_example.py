#!/usr/bin/env python3
"""
Generate Light Theme ICP Presentation Example

This script demonstrates using Claude's pptx skill with gtmfabric-brand-guidelines
to create a light theme presentation.

Usage:
    export ANTHROPIC_API_KEY=your-api-key
    python3 generate_light_theme_example.py
"""

import os
import sys
from anthropic import Anthropic

def generate_light_theme_presentation():
    """Generate a light theme ICP presentation using Claude's pptx skill."""

    # Check for API key
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        print("❌ Error: ANTHROPIC_API_KEY environment variable not set")
        print("\nTo set it:")
        print("  export ANTHROPIC_API_KEY=your-api-key")
        print("\nOr create a .env file in the skills directory")
        sys.exit(1)

    client = Anthropic(api_key=api_key)

    # Comprehensive prompt for light theme ICP presentation
    prompt = """Create a PowerPoint presentation using GTM Fabric LIGHT THEME branding.

**CRITICAL: Use LIGHT THEME from gtmfabric-brand-guidelines**

**Presentation Details:**
- Client: TechVendor Solutions
- Campaign: Enterprise Platform GTM
- Date: January 2025

**LIGHT THEME SPECIFICATIONS (from gtmfabric-brand-guidelines):**
- Background: White (#FFFFFF)
- Logo: Black version (gtmfabric_logo_black.png) on all slides, top-right, 0.8 inches
- Accent: Dark Purple (#8B5CF6) for all headers and highlights
- Primary Text: Near Black (#1a1a1a) for body content
- Card Background: Light Gray (#F8F9FA) for content areas
- Borders: Border Gray (#DEE2E6), 1pt
- Font: Arial throughout all slides

---

**SLIDE 1: Title Slide**

Background: White (#FFFFFF)
Title: "TechVendor Solutions - Ideal Customer Profiles"
  - 30pt, Primary Text (#1a1a1a), Bold, Centered
Subtitle: "Enterprise Platform GTM Campaign"
  - 24pt, Accent Purple (#8B5CF6), Centered
Date: "January 2025"
  - 14pt, Secondary Text (#6C757D), Bottom-left
Logo: Black GTM Fabric logo, top-right, 0.8 inches
Optional: Thin accent line in Accent Purple above or below title

---

**SLIDE 2: ICP #1 - Cloud Infrastructure Modernization Buyer**

Background: White (#FFFFFF)
Logo: Black version, top-right
Page Number: Bottom-right

ICP Badge: "ICP #1: Cloud Infrastructure Modernization Buyer"
  - Pill-shaped badge with Accent Purple (#8B5CF6) background or border
  - 16pt, Semibold

Content Card: Light Gray (#F8F9FA) background, Border Gray edges, rounded corners

**Industries:** Financial Services, Healthcare, Retail
  - Header: 16pt, Accent Purple, Semibold
  - Content: 14pt, Primary Text

**Departments:** Cloud Infrastructure, Platform Engineering, DevOps

**Key Roles:**
• VP of Engineering
• Cloud Architect
• Director of Infrastructure
• DevOps Manager

**Technographic Fit**
  - Main header: 16pt, Accent Purple

**Displacement Signals:**
Pain: Legacy on-premise infrastructure creating scalability bottlenecks and high maintenance costs
Replacing: **VMware** → **vSphere**, **IBM** → **WebSphere**, **Oracle** → **Database Enterprise**

**Expansion Signals:**
Readiness: Active cloud migration initiatives and container adoption
Using: **AWS** → **EC2**, **Kubernetes**, **Docker** → **Enterprise**, **HashiCorp** → **Terraform**

---

**SLIDE 3: ICP #2 - Data Platform Consolidation Buyer**

Background: White (#FFFFFF)
Logo: Black version, top-right
Page Number: Bottom-right

ICP Badge: "ICP #2: Data Platform Consolidation Buyer"

Content Card: Light Gray background, Border Gray edges

**Industries:** Technology, E-commerce, Professional Services

**Departments:** Data Engineering, Analytics, Business Intelligence

**Key Roles:**
• Chief Data Officer
• VP Data Engineering
• Data Platform Lead
• Analytics Director

**Technographic Fit**

**Displacement Signals:**
Pain: Multiple disparate data tools causing integration complexity and data silos
Replacing: **Informatica** → **PowerCenter**, **Talend** → **Data Integration**, **Legacy ETL** → **Various tools**

**Expansion Signals:**
Readiness: Modern data stack adoption and real-time analytics requirements
Using: **Snowflake** → **Data Warehouse**, **Databricks** → **Lakehouse**, **dbt** → **Core**, **Tableau** → **Desktop**

---

**SLIDE 4: ICP #3 - Security Operations Automation Buyer**

Background: White (#FFFFFF)
Logo: Black version, top-right
Page Number: Bottom-right

ICP Badge: "ICP #3: Security Operations Automation Buyer"

Content Card: Light Gray background, Border Gray edges

**Industries:** Financial Services, Government, Healthcare

**Departments:** Security Operations, Incident Response, SOC

**Key Roles:**
• CISO
• VP Security Operations
• SOC Director
• Security Architect

**Technographic Fit**

**Displacement Signals:**
Pain: Manual security processes leading to slow incident response and alert fatigue
Replacing: **Splunk** → **Enterprise Security**, **IBM** → **QRadar**, **RSA** → **NetWitness**

**Expansion Signals:**
Readiness: Cloud security posture management and automation priorities
Using: **Palo Alto** → **Prisma Cloud**, **CrowdStrike** → **Falcon**, **Okta** → **Identity Platform**, **ServiceNow** → **Security Operations**

---

**FORMATTING REQUIREMENTS:**

1. **Light Theme Colors:**
   - All backgrounds: White (#FFFFFF)
   - All cards: Light Gray (#F8F9FA)
   - All headers: Accent Purple (#8B5CF6)
   - All body text: Primary Text (#1a1a1a)
   - All borders: Border Gray (#DEE2E6)

2. **Typography:**
   - Font: Arial throughout
   - Headers: 16pt, Semibold, Accent Purple
   - Body: 14pt, Regular, Primary Text
   - Bold ALL vendor and product names
   - Use → arrow notation consistently

3. **Layout:**
   - 0.5 inch margins on all sides
   - Card areas with 2-4pt rounded corners
   - Generous white space between sections
   - Black logo on all slides (top-right)
   - Page numbers on content slides (bottom-right)

4. **Professional Polish:**
   - Clean, modern design
   - Clear visual hierarchy
   - Consistent spacing
   - Print-ready quality

Save as: TechVendor_ICPs_LightTheme_2025-01-15.pptx
"""

    print("🎨 Generating Light Theme ICP Presentation...")
    print("⏱️  This will take 1-2 minutes (PowerPoint generation is slow)...\n")

    try:
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
            messages=[{"role": "user", "content": prompt}]
        )

        print("✅ Response received!\n")
        print(f"Stop reason: {response.stop_reason}")
        print(f"Content blocks: {len(response.content)}\n")

        # Display response content
        for i, block in enumerate(response.content):
            print(f"--- Block {i + 1} ---")
            if hasattr(block, 'type'):
                print(f"Type: {block.type}")

                if block.type == 'text':
                    text = block.text
                    if len(text) > 500:
                        print(f"Text preview: {text[:500]}...")
                    else:
                        print(f"Text: {text}")

                elif block.type == 'tool_use':
                    print(f"Tool: {block.name}")
                    if hasattr(block, 'input') and isinstance(block.input, dict):
                        print(f"Input keys: {list(block.input.keys())}")

            print()

        print("\n" + "="*60)
        print("✨ Light Theme Presentation Generation Complete!")
        print("="*60)
        print("\nThe presentation should now be available for download.")
        print("Check the response above for file information.")

        return response

    except Exception as e:
        print(f"\n❌ Error generating presentation: {e}")
        import traceback
        traceback.print_exc()
        return None


if __name__ == "__main__":
    print("="*60)
    print("GTM Fabric Light Theme ICP Presentation Generator")
    print("="*60)
    print()

    result = generate_light_theme_presentation()

    if result:
        print("\n✅ Script completed successfully!")
    else:
        print("\n❌ Script failed. Check error messages above.")
        sys.exit(1)
