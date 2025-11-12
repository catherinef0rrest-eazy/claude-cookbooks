#!/usr/bin/env python3
"""
Example: Using GTM Fabric Brand Guidelines with Claude's Built-in Skills

This demonstrates the simplified approach:
- No custom PowerPoint generation code
- No python-pptx dependency
- Just prompts + Claude's built-in pptx skill
"""

import os
from anthropic import Anthropic

# Initialize Claude client
client = Anthropic(api_key=os.environ.get("ANTHROPIC_API_KEY"))


def example_1_simple_icp_presentation():
    """
    Example 1: Generate ICP PowerPoint using brand guidelines

    This uses Claude's built-in pptx skill + gtmfabric-brand-guidelines
    """

    print("Example 1: Creating ICP Presentation with Brand Guidelines")
    print("=" * 60)

    icp_content = """Create a GTM Fabric branded PowerPoint presentation:

**Client**: Kaspersky
**Campaign**: Enterprise Security Platform GTM
**Date**: January 2025

## ICP #1: Enterprise Security Modernization Buyer

**Industries**: Financial Services, Healthcare, Manufacturing

**Departments**: IT Security, Infrastructure, Compliance

**Key Roles**:
- CISO (Chief Information Security Officer)
- VP IT
- Security Director
- IT Director

**Displacement Signals** (Modernization Opportunities):
- **Pain**: Legacy endpoint security solutions causing compliance risks and operational inefficiencies
- **Replacing**:
  - McAfee → ePO
  - Symantec → Endpoint Protection
  - Trend Micro → Apex One

**Expansion Signals** (Technology Readiness):
- **Readiness**: Recent cloud migration creating new security requirements and integration opportunities
- **Using**:
  - Microsoft → Azure
  - AWS
  - Okta → Identity Platform
  - CrowdStrike → Falcon


## ICP #2: Mid-Market Cloud Security Buyer

**Industries**: Technology, Professional Services, E-commerce

**Departments**: IT, DevOps, Security

**Key Roles**:
- VP Engineering
- IT Manager
- DevOps Lead
- Security Manager

**Displacement Signals**:
- **Pain**: Basic antivirus insufficient for modern threats and cloud workloads
- **Replacing**:
  - Norton → Business Security
  - Avast → Business Security
  - Windows → Defender

**Expansion Signals**:
- **Readiness**: Adopting cloud-native architecture and modern DevOps practices
- **Using**:
  - AWS
  - GitHub → Enterprise
  - Slack
  - Atlassian → Jira


Apply gtmfabric-brand-guidelines:
- Dark theme (#06040f background)
- Accent purple (#c084fc) for all headers and highlights
- GTM Fabric white logo (gtmfabric_logo_white.png) on all slides, top-right, 0.8 inches
- Arial font throughout
- Bold ALL vendor and product names
- Use → arrow notation for all vendor/product relationships
- Card-based layout with Card Purple (#120a1f) content areas
- All 5 required ICP sections on each ICP slide
- Title slide + 2 ICP slides + thank you slide
"""

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
        messages=[{"role": "user", "content": icp_content}]
    )

    print(f"Response received with {len(response.content)} content blocks")

    # Extract file if generated
    for block in response.content:
        if hasattr(block, 'type') and block.type == 'tool_use':
            print(f"Tool used: {block.name}")
        elif hasattr(block, 'text'):
            print(f"Text response: {block.text[:200]}...")

    print("\nExample 1 complete!")
    print("=" * 60)
    return response


def example_2_brand_guidelines_query():
    """
    Example 2: Query the brand guidelines

    Claude can read and interpret the SKILL.md
    """

    print("\nExample 2: Querying Brand Guidelines")
    print("=" * 60)

    query = """Review the gtmfabric-brand-guidelines skill and answer:

1. What is the primary background color (hex code)?
2. What is the accent color (hex code)?
3. What font should be used?
4. Where should the logo be placed on slides?
5. How should vendor/product names be formatted?
6. What are the 5 required sections for an ICP slide?
"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{"role": "user", "content": query}]
    )

    print("Claude's response based on brand guidelines:")
    print(response.content[0].text)
    print("\nExample 2 complete!")
    print("=" * 60)
    return response


def example_3_validate_content():
    """
    Example 3: Validate content against brand guidelines
    """

    print("\nExample 3: Validate Content Against Guidelines")
    print("=" * 60)

    content_to_validate = """I created a PowerPoint with:
- White background
- Blue color (#0000FF) for headers
- Times New Roman font
- Logo in bottom-left corner
- Vendor names like "Salesforce" without product names
"""

    validation_prompt = f"""Review this content against gtmfabric-brand-guidelines:

{content_to_validate}

Identify all violations and suggest corrections.
"""

    response = client.messages.create(
        model="claude-sonnet-4-5-20250929",
        max_tokens=1024,
        messages=[{"role": "user", "content": validation_prompt}]
    )

    print("Validation results:")
    print(response.content[0].text)
    print("\nExample 3 complete!")
    print("=" * 60)
    return response


def example_4_workflow_integration():
    """
    Example 4: Demonstrate integration with DemandScience workflow
    """

    print("\nExample 4: DemandScience Workflow Integration")
    print("=" * 60)

    # Simulated Phase 1 output (Markdown ICPs after human review)
    approved_icp_markdown = """# Kaspersky - Enterprise Security Platform Campaign
Date: January 2025

## ICP #1: Enterprise Security Modernization Buyer

**Industries**: Financial Services, Healthcare, Manufacturing

**Departments**: IT Security, Infrastructure, Compliance

**Key Roles**: CISO, VP IT, Security Director

**Displacement Signals**:
Pain: Legacy endpoint security causing compliance risks
Replacing: McAfee → ePO, Symantec → Endpoint Protection

**Expansion Signals**:
Readiness: Cloud migration creating security gaps
Using: Microsoft → Azure, AWS, Okta
"""

    # Phase 2: Convert to PowerPoint with branding
    campaign_info = {
        "client_name": "Kaspersky",
        "campaign_type": "Enterprise Security Platform",
        "date": "January 2025"
    }

    prompt = f"""Create GTM Fabric branded PowerPoint from this approved ICP content:

**Client**: {campaign_info['client_name']}
**Campaign**: {campaign_info['campaign_type']}
**Date**: {campaign_info['date']}

{approved_icp_markdown}

Apply gtmfabric-brand-guidelines for all formatting, colors, fonts, logo placement, and structure.
"""

    print("Workflow: Phase 1 (Research) → Human Review → Phase 2 (PowerPoint)")
    print(f"Campaign: {campaign_info['client_name']} - {campaign_info['campaign_type']}")
    print("\nThis demonstrates how the simplified skill integrates with your workflow:")
    print("1. Phase 1 generates Markdown ICPs")
    print("2. Human reviews and edits")
    print("3. Phase 2 converts to branded PowerPoint via prompt")
    print("4. No custom Python code needed!")

    print("\nExample 4 complete!")
    print("=" * 60)


if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("GTM Fabric Brand Guidelines - Simplified Approach Examples")
    print("=" * 60)
    print("\nThese examples demonstrate using brand guidelines with Claude's")
    print("built-in skills instead of custom code.\n")

    # Run examples
    # Note: Example 1 requires API key and generates actual files
    # Uncomment to run:

    # example_1_simple_icp_presentation()
    # example_2_brand_guidelines_query()
    # example_3_validate_content()
    example_4_workflow_integration()

    print("\n" + "=" * 60)
    print("All examples complete!")
    print("=" * 60)
    print("\nKey takeaways:")
    print("✓ No custom PowerPoint generation code")
    print("✓ No python-pptx dependency")
    print("✓ Just prompts + Claude's built-in pptx skill")
    print("✓ Brand guidelines in SKILL.md are automatically applied")
    print("✓ Simpler, more maintainable, more flexible")
    print("=" * 60)
