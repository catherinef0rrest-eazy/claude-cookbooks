#!/usr/bin/env python3
"""
Test the DemandScience ICP JSON skill.

This script tests the full two-stage workflow:
- Stage 1: Generate research-validated ICPs in Markdown
- Stage 2: Convert approved Markdown to JSON
"""

import os
import sys
import json
import argparse
from pathlib import Path
from anthropic import Anthropic
from dotenv import load_dotenv

# Load environment
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("❌ Error: ANTHROPIC_API_KEY not found in environment")
    sys.exit(1)

client = Anthropic(api_key=API_KEY)

# Load skill ID
SKILL_ID_FILE = Path(__file__).parent / "skill_id.txt"
if not SKILL_ID_FILE.exists():
    print("❌ Error: skill_id.txt not found")
    print("   Skill must be uploaded first: python upload_skill.py")
    sys.exit(1)

with open(SKILL_ID_FILE) as f:
    SKILL_ID = f.read().strip()

# Output directory
OUTPUT_DIR = Path(__file__).parent / "test_outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Default test email
DEFAULT_TEST_EMAIL = """From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Vena Solutions

We need ICPs for Vena Solutions targeting finance teams in mid-market companies.

Products: Vena Complete Planning Platform
Target Industries: Technology, Manufacturing, Professional Services
Use Case: Replacing legacy Excel-based planning and Oracle/SAP EPM systems
Region: North America

Please generate ICPs for this campaign.
"""


def stage1_generate_icps(email_brief):
    """Stage 1: Generate research-validated ICPs in Markdown."""
    print("\n" + "=" * 70)
    print("STAGE 1: ICP Research & Markdown Generation")
    print("=" * 70)
    print("\n⏱️  Expected time: 2-3 minutes")
    print(f"📧 Email brief:")
    print("-" * 70)
    print(email_brief)
    print("-" * 70)

    print("\n🔬 Generating research-validated ICPs...")

    # Stage 1: Generate ICPs
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        container={
            "skills": [
                {"type": "custom", "skill_id": SKILL_ID, "version": "latest"}
            ]
        },
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
        messages=[{"role": "user", "content": email_brief}],
        betas=[
            "code-execution-2025-08-25",
            "files-api-2025-04-14",
            "skills-2025-10-02"
        ]
    )

    # Extract Markdown content
    markdown_content = ""
    for content in response.content:
        if content.type == "text":
            markdown_content += content.text

    # Display results
    print("\n" + "=" * 70)
    print("STAGE 1 COMPLETE - ICPs Generated")
    print("=" * 70)
    print(f"\n📊 Token Usage:")
    print(f"   Input:  {response.usage.input_tokens:,} tokens")
    print(f"   Output: {response.usage.output_tokens:,} tokens")
    print(f"   Total:  {response.usage.input_tokens + response.usage.output_tokens:,} tokens")

    print(f"\n📝 Generated ICPs (Markdown):")
    print("=" * 70)
    print(markdown_content)
    print("=" * 70)

    # Save Markdown to file
    markdown_file = OUTPUT_DIR / "icps_stage1.md"
    with open(markdown_file, "w") as f:
        f.write(markdown_content)
    print(f"\n💾 Markdown saved to: {markdown_file}")

    return markdown_content, response


def stage2_generate_json(markdown_icps, customer_name="Vena Solutions", products=None, campaign_goal=None, region=None):
    """Stage 2: Convert approved Markdown to JSON."""
    print("\n" + "=" * 70)
    print("STAGE 2: JSON Conversion")
    print("=" * 70)
    print("\n⏱️  Expected time: <30 seconds")

    if products is None:
        products = ["Vena Complete Planning Platform"]
    if campaign_goal is None:
        campaign_goal = "Target finance teams replacing legacy Excel and EPM systems"
    if region is None:
        region = "North America"

    # Prepare Stage 2 prompt
    stage2_prompt = f"""The user has approved the following ICPs. Please convert them to structured JSON format.

Approved ICPs:
{markdown_icps}

Campaign Details:
- DemandScience Customer: {customer_name}
- Products: {', '.join(products)}
- Campaign Goal: {campaign_goal}
- Target Region: {region}
- Year: 2025

Generate well-formatted JSON with:
- campaign_metadata object with all campaign details
- icps array containing all ICPs with proper structure
- All fields following snake_case naming convention
- Valid JSON syntax with proper escaping

Output the JSON in a ```json code block.
"""

    print(f"\n🔄 Converting to JSON for: {customer_name}")

    # Stage 2: Generate JSON
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        container={
            "skills": [
                {"type": "custom", "skill_id": SKILL_ID, "version": "latest"}
            ]
        },
        tools=[{"type": "code_execution_20250825", "name": "code_execution"}],
        messages=[{"role": "user", "content": stage2_prompt}],
        betas=[
            "code-execution-2025-08-25",
            "files-api-2025-04-14",
            "skills-2025-10-02"
        ]
    )

    # Extract JSON from response
    text_content = ""
    for content in response.content:
        if content.type == "text":
            text_content = content.text

    # Parse JSON from code block or raw text
    json_data = None
    try:
        if "```json" in text_content:
            json_start = text_content.find("```json") + 7
            json_end = text_content.find("```", json_start)
            json_str = text_content[json_start:json_end].strip()
        elif "{" in text_content:
            json_start = text_content.find("{")
            json_end = text_content.rfind("}") + 1
            json_str = text_content[json_start:json_end]
        else:
            raise ValueError("No JSON found in response")

        json_data = json.loads(json_str)
    except (json.JSONDecodeError, ValueError) as e:
        print(f"\n⚠️  JSON parsing failed: {e}")
        print(f"\nRaw response:")
        print(text_content[:500] + "...")

    # Display results
    print("\n" + "=" * 70)
    print("STAGE 2 COMPLETE - JSON Generated")
    print("=" * 70)
    print(f"\n📊 Token Usage:")
    print(f"   Input:  {response.usage.input_tokens:,} tokens")
    print(f"   Output: {response.usage.output_tokens:,} tokens")
    print(f"   Total:  {response.usage.input_tokens + response.usage.output_tokens:,} tokens")

    if json_data:
        # Save JSON to file
        json_file = OUTPUT_DIR / "icps_stage2.json"
        with open(json_file, "w") as f:
            json.dump(json_data, f, indent=2)

        print(f"\n✅ JSON saved to: {json_file}")
        print(f"\n📋 JSON Summary:")
        print(f"   Customer: {json_data.get('campaign_metadata', {}).get('demandscience_customer', 'N/A')}")
        print(f"   Total ICPs: {json_data.get('campaign_metadata', {}).get('total_icps', 0)}")

        # Validate JSON structure
        is_valid, errors = validate_json(json_data)
        if is_valid:
            print(f"\n✅ JSON validation passed")
        else:
            print(f"\n⚠️  JSON validation warnings:")
            for error in errors:
                print(f"   - {error}")

    return json_data, response


def validate_json(data):
    """Validate ICP JSON structure."""
    errors = []

    # Check top-level structure
    if "campaign_metadata" not in data:
        errors.append("Missing campaign_metadata")
    if "icps" not in data:
        errors.append("Missing icps array")

    if errors:
        return False, errors

    # Validate campaign metadata
    meta = data.get("campaign_metadata", {})
    required_meta_fields = ["demandscience_customer", "products", "campaign_goal", "generated_date", "total_icps"]

    for field in required_meta_fields:
        if field not in meta:
            errors.append(f"Missing campaign_metadata.{field}")

    # Validate ICPs array
    icps = data.get("icps", [])
    if not isinstance(icps, list):
        errors.append("icps must be an array")
        return False, errors

    if len(icps) < 3:
        errors.append(f"Expected at least 3 ICPs, got {len(icps)}")

    # Check each ICP
    required_icp_fields = ["icp_id", "title", "industries", "departments", "key_roles", "technographic_fit"]

    for i, icp in enumerate(icps):
        for field in required_icp_fields:
            if field not in icp:
                errors.append(f"ICP {i+1} missing field: {field}")

    if errors:
        return False, errors

    return True, ["Valid"]


def main():
    """Main test workflow."""
    parser = argparse.ArgumentParser(description="Test DemandScience ICP JSON skill")
    parser.add_argument("--email-file", help="Path to email brief file (optional)")
    parser.add_argument("--skip-stage2", action="store_true", help="Only run Stage 1")
    parser.add_argument("--auto-approve", action="store_true", help="Auto-approve ICPs for Stage 2 (non-interactive)")
    args = parser.parse_args()

    # Load email brief
    if args.email_file:
        with open(args.email_file) as f:
            email_brief = f.read()
    else:
        email_brief = DEFAULT_TEST_EMAIL

    print("=" * 70)
    print("DemandScience ICP JSON Skill - Test")
    print("=" * 70)
    print(f"\n🆔 Skill ID: {SKILL_ID}")
    print(f"📁 Output Directory: {OUTPUT_DIR}")

    # Stage 1: Generate ICPs
    markdown_icps, stage1_response = stage1_generate_icps(email_brief)

    if args.skip_stage2:
        print("\n⏭️  Skipping Stage 2 (--skip-stage2 flag)")
        return

    # Human-in-the-loop approval
    print("\n" + "=" * 70)
    print("HUMAN REVIEW REQUIRED")
    print("=" * 70)
    print("\n👀 Please review the ICPs above.")
    print("   You can edit the Markdown in: test_outputs/icps_stage1.md")
    print("\n❓ Approve for JSON conversion?")

    if args.auto_approve:
        print("   ✅ Auto-approved (--auto-approve flag)")
        approval = "yes"
    else:
        approval = input("   Type 'yes' to proceed, or anything else to exit: ")

    if approval.lower() != "yes":
        print("\n⏸️  Workflow stopped. User did not approve.")
        print(f"   ICPs saved to: {OUTPUT_DIR}/icps_stage1.md")
        print(f"   To proceed later, edit the Markdown and run Stage 2 manually.")
        return

    # Stage 2: Generate JSON
    json_data, stage2_response = stage2_generate_json(markdown_icps)

    # Final summary
    print("\n" + "=" * 70)
    print("TEST COMPLETE - Full Workflow Success")
    print("=" * 70)

    total_input = stage1_response.usage.input_tokens + stage2_response.usage.input_tokens
    total_output = stage1_response.usage.output_tokens + stage2_response.usage.output_tokens

    print(f"\n📊 Total Token Usage:")
    print(f"   Stage 1: {stage1_response.usage.input_tokens:,} in, {stage1_response.usage.output_tokens:,} out")
    print(f"   Stage 2: {stage2_response.usage.input_tokens:,} in, {stage2_response.usage.output_tokens:,} out")
    print(f"   Total:   {total_input:,} in, {total_output:,} out")
    print(f"   Grand Total: {total_input + total_output:,} tokens")

    if json_data:
        print(f"\n✅ Success! JSON output created:")
        print(f"   Markdown: {OUTPUT_DIR}/icps_stage1.md")
        print(f"   JSON:     {OUTPUT_DIR}/icps_stage2.json")
        print(f"\n💡 Next Steps:")
        print(f"   1. Review the JSON structure")
        print(f"   2. Validate the ICP data")
        print(f"   3. Use JSON for downstream integration")


if __name__ == "__main__":
    main()
