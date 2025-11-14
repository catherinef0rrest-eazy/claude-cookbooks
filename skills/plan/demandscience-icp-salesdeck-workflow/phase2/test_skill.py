#!/usr/bin/env python3
"""
Test the DemandScience ICP & Sales Deck skill.

This script tests both stages of the workflow:
- Stage 1: Generate ICPs in Markdown format
- Stage 2: Convert approved ICPs to PowerPoint

Usage:
    python test_skill.py                    # Interactive mode with test email
    python test_skill.py --email-file FILE  # Use custom email file
"""

import os
import sys
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
    print("   Please run: python upload_skill.py first")
    sys.exit(1)

with open(SKILL_ID_FILE) as f:
    SKILL_ID = f.read().strip()

# Setup output directory
OUTPUT_DIR = Path(__file__).parent / "outputs"
OUTPUT_DIR.mkdir(exist_ok=True)

# Test email brief
DEFAULT_TEST_EMAIL = """From: DemandScience Partner <partner@demandscience.com>
Subject: Campaign Request - Vena Solutions

We need ICPs for Vena Solutions targeting finance teams in mid-market companies.

Products: Vena Complete Planning Platform
Target Industries: Technology, Manufacturing, Professional Services
Use Case: Replacing legacy Excel-based planning and Oracle/SAP EPM systems
Region: North America

Please generate ICPs for this campaign.
"""


def extract_file_ids(response):
    """Extract file IDs from beta API response."""
    file_ids = []
    for content in response.content:
        if hasattr(content, 'type') and content.type == 'bash_code_execution_tool_result':
            if hasattr(content, 'content') and content.content:
                for item in content.content:
                    if hasattr(item, 'file_id') and item.file_id:
                        file_ids.append(item.file_id)
    return file_ids


def download_file(client, file_id, output_dir, prefix=""):
    """Download a file using the beta Files API."""
    try:
        # Get file metadata
        metadata = client.beta.files.retrieve_metadata(file_id)

        # Construct output filename
        filename = f"{prefix}{metadata.filename}"
        output_path = Path(output_dir) / filename

        # Download file content
        file_content = client.beta.files.download(file_id)

        # Write to disk
        with open(output_path, 'wb') as f:
            f.write(file_content.read())

        print(f"   ✅ Downloaded: {filename} ({metadata.size_bytes:,} bytes)")
        return output_path

    except Exception as e:
        print(f"   ❌ Download failed for {file_id}: {e}")
        return None


def stage1_generate_icps(email_brief):
    """Stage 1: Generate ICPs in Markdown format."""
    print("\n" + "=" * 70)
    print("STAGE 1: ICP Research & Markdown Generation")
    print("=" * 70)
    print("\n⏱️  Expected time: 2-3 minutes")
    print("📧 Email brief:")
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

    # Extract Markdown
    markdown_content = ""
    for content in response.content:
        if content.type == "text":
            markdown_content = content.text

    # Display results
    print("\n" + "=" * 70)
    print("STAGE 1 COMPLETE - ICPs Generated")
    print("=" * 70)
    print(f"\n📊 Token Usage:")
    print(f"   Input:  {response.usage.input_tokens:,} tokens")
    print(f"   Output: {response.usage.output_tokens:,} tokens")
    print(f"   Total:  {response.usage.input_tokens + response.usage.output_tokens:,} tokens")

    print("\n📝 Generated ICPs (Markdown):")
    print("=" * 70)
    print(markdown_content)
    print("=" * 70)

    return markdown_content, response


def stage2_generate_powerpoint(markdown_icps, customer_name="Vena Solutions"):
    """Stage 2: Convert approved ICPs to PowerPoint."""
    print("\n" + "=" * 70)
    print("STAGE 2: PowerPoint Generation")
    print("=" * 70)
    print("\n⏱️  Expected time: 1-2 minutes")

    # Prepare Stage 2 prompt
    stage2_prompt = f"""Create a PowerPoint presentation with the following content:

SLIDE 1 - Cover Slide:
Title: "{customer_name}" (80pt Arial, color #320361)
Subtitle: "Complete Planning Platform" (74pt Arial Bold, color #320361)
Description: "Targeting finance teams replacing legacy Excel and EPM systems" (22pt Arial, color #282D49)
Year: "2025"
Background: #F4F6FB

SLIDE 2 - Customer Logo:
Large centered text: "{customer_name}" (80pt Arial, color #320361)
Background: #F4F6FB

SLIDE 3 - Key Elements for E2E Solutions:
Title: "Key Elements Required For E2E Use Case Solutions" (36pt Arial, color #320361)
Layout: 2×2 grid with four sections:
- Top Left: Neutral vendor management, Data value and harmonization, Industry-specific expertise
- Top Right: Architecture & design services, Integration capabilities, Analytical tools and platforms
- Bottom Left: Practical examples and use cases, Case studies from similar companies, Implementation blueprints
- Bottom Right: Project management services, Strategic vision and planning, Training and enablement programs
Background: #F4F6FB

SLIDE 4 - GTM Fabric Propensity Funnel:
Title: "GTM Fabric Propensity Funnel" (36pt Arial, color #320361)
Funnel visualization with three levels: TAM (top/widest), SAM (middle), SOM (bottom/narrowest)
Purple color scheme #320361
Background: #F4F6FB

Now create slides 5-7 with these ICPs:

{markdown_icps}

For each ICP slide, use this layout:
- Title: ICP name (36pt Arial, #320361)
- Left column with cream background (#F4F6FB): Industries as 2×2 pill grid (#999999 background), Departments as plain list, Key Roles as plain list
- Right column with white boxes: Displacement signals with vendor names in bold, Expansion signals with vendor names in bold
- Use Arial font, #282D49 for text
- Slide background: #F4F6FB

Please generate this PowerPoint file now.
"""

    print(f"\n🎨 Generating PowerPoint for: {customer_name}")

    # Stage 2: Generate PowerPoint
    response = client.beta.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        container={
            "skills": [
                {"type": "custom", "skill_id": SKILL_ID, "version": "latest"},
                {"type": "anthropic", "skill_id": "pptx", "version": "latest"}
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

    # Display text response
    for content in response.content:
        if content.type == "text":
            print("\n📄 Response:")
            print("-" * 70)
            print(content.text)
            print("-" * 70)

    # Download PowerPoint file
    file_ids = extract_file_ids(response)
    pptx_path = None

    if file_ids:
        print(f"\n📥 Downloading PowerPoint file...")
        for file_id in file_ids:
            pptx_path = download_file(
                client,
                file_id,
                OUTPUT_DIR,
                prefix="vena_icp_deck_"
            )
    else:
        print("\n⚠️  No files generated. Check response for errors.")

    # Display results
    print("\n" + "=" * 70)
    print("STAGE 2 COMPLETE - PowerPoint Generated")
    print("=" * 70)
    print(f"\n📊 Token Usage:")
    print(f"   Input:  {response.usage.input_tokens:,} tokens")
    print(f"   Output: {response.usage.output_tokens:,} tokens")
    print(f"   Total:  {response.usage.input_tokens + response.usage.output_tokens:,} tokens")

    if pptx_path:
        print(f"\n📂 PowerPoint saved to: {pptx_path}")

    return response, pptx_path


def main():
    """Main test workflow."""
    parser = argparse.ArgumentParser(description="Test DemandScience ICP skill")
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
    print("DemandScience ICP & Sales Deck Skill - Test")
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
    print("   You can edit the Markdown if needed.")
    print("\n❓ Approve for PowerPoint generation?")

    if args.auto_approve:
        print("   ✅ Auto-approved (--auto-approve flag)")
        approval = "yes"
    else:
        approval = input("   Type 'yes' to proceed, or anything else to exit: ")

    if approval.lower() != "yes":
        print("\n⏸️  Workflow stopped. User did not approve.")
        print(f"   ICPs saved to memory. To proceed later, run Stage 2 manually.")
        return

    # Stage 2: Generate PowerPoint
    stage2_response, pptx_path = stage2_generate_powerpoint(markdown_icps)

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

    if pptx_path:
        print(f"\n✅ Success! PowerPoint deck created:")
        print(f"   {pptx_path}")
        print(f"\n💡 Next Steps:")
        print(f"   1. Open the PowerPoint file")
        print(f"   2. Verify branding is correct")
        print(f"   3. Check that all placeholders are replaced")
        print(f"   4. Confirm static slides (3-4) are unchanged")
        print(f"   5. Review ICP content accuracy")


if __name__ == "__main__":
    main()
