#!/usr/bin/env python3
"""
Upload the DemandScience ICP JSON skill to Claude.

This script uploads the custom skill to your Claude workspace.
Run this once to create the skill, then use test_skill.py to test it.
"""

import os
import sys
from pathlib import Path
from anthropic import Anthropic
from anthropic.lib import files_from_dir
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

API_KEY = os.getenv("ANTHROPIC_API_KEY")
if not API_KEY:
    print("❌ Error: ANTHROPIC_API_KEY not found in environment")
    print("   Please set your API key in .env file")
    sys.exit(1)

# Initialize client
client = Anthropic(api_key=API_KEY)

# Skill directory
SKILL_DIR = Path(__file__).parent

def upload_skill():
    """Upload the DemandScience ICP JSON skill."""
    print("=" * 70)
    print("DemandScience ICP JSON Skill - Upload")
    print("=" * 70)

    # Verify SKILL.md exists
    skill_md = SKILL_DIR / "SKILL.md"
    if not skill_md.exists():
        print(f"\n❌ Error: SKILL.md not found: {skill_md}")
        sys.exit(1)

    print(f"\n📁 Skill directory: {SKILL_DIR}")
    print(f"✓ SKILL.md found")

    # List all files being uploaded
    print("\n📦 Files to upload:")
    for file_path in SKILL_DIR.rglob("*"):
        if file_path.is_file() and not file_path.name.endswith('.py'):
            rel_path = file_path.relative_to(SKILL_DIR)
            size = file_path.stat().st_size
            if size > 1024 * 1024:
                size_str = f"{size / 1024 / 1024:.1f} MB"
            elif size > 1024:
                size_str = f"{size / 1024:.1f} KB"
            else:
                size_str = f"{size} bytes"
            print(f"   - {rel_path} ({size_str})")

    print("\n🚀 Uploading skill...")

    try:
        # Upload skill
        skill = client.beta.skills.create(
            display_title="DemandScience ICP JSON Generator",
            files=files_from_dir(str(SKILL_DIR))
        )

        print("\n" + "=" * 70)
        print("✅ SKILL UPLOADED SUCCESSFULLY!")
        print("=" * 70)
        print(f"\n📋 Skill Details:")
        print(f"   Skill ID: {skill.id}")
        print(f"   Display Title: {skill.display_title}")
        print(f"   Version: {skill.latest_version}")
        print(f"   Created: {skill.created_at}")
        print(f"   Source: {skill.source}")

        # Save skill ID for future use
        skill_id_file = SKILL_DIR / "skill_id.txt"
        with open(skill_id_file, "w") as f:
            f.write(skill.id)

        print(f"\n💾 Skill ID saved to: {skill_id_file}")
        print("\n🎯 Next Steps:")
        print("   1. Run: python test_skill.py")
        print("   2. Provide a test email brief")
        print("   3. Review generated ICPs")
        print("   4. Approve for JSON conversion")

        return skill.id

    except Exception as e:
        print(f"\n❌ Upload failed: {e}")

        if "cannot reuse an existing display_title" in str(e):
            print("\n💡 Solution: A skill with this name already exists.")
            print("   Option 1: Delete the existing skill first")
            print("   Option 2: Use a different display_title in the upload call")

            # List existing skills
            try:
                existing = client.beta.skills.list(source="custom")
                if existing.data:
                    print("\n📚 Existing custom skills:")
                    for s in existing.data:
                        print(f"   - {s.display_title} (ID: {s.id})")
            except:
                pass

        sys.exit(1)

if __name__ == "__main__":
    skill_id = upload_skill()
