#!/usr/bin/env python3
"""
Example usage of GTM Fabric PowerPoint Generator
Demonstrates creating modern, sleek ICP presentations
"""

import json
import sys
import os

# Add current directory to path for imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pptx_generator import GTMFabricPresentationGenerator, generate_icp_presentation


def example_1_basic_presentation():
    """Example 1: Create a basic presentation with title and content slides"""
    print("\n=== Example 1: Basic Presentation ===\n")

    generator = GTMFabricPresentationGenerator()
    prs = generator.create_presentation()

    # Title slide
    generator.create_title_slide(
        prs,
        title="GTM Fabric Design System",
        subtitle="Modern PowerPoint Generation",
        date="January 2025"
    )

    # Content slide
    generator.create_content_slide(
        prs,
        title="Key Features",
        content_sections=[
            {
                "header": "Design System",
                "items": [
                    "Dark purple theme with accent colors",
                    "Modern card-based layouts",
                    "GTM Fabric branding with logo"
                ],
                "style": "bullets"
            },
            {
                "header": "Typography",
                "items": [
                    "Arial font family",
                    "Responsive sizing",
                    "High contrast for readability"
                ],
                "style": "bullets"
            }
        ],
        page_number=2
    )

    # Save
    output_path = os.path.join(os.path.dirname(__file__), "example-basic.pptx")
    generator.save_presentation(prs, output_path)
    print(f"Created: {output_path}\n")


def example_2_icp_presentation():
    """Example 2: Create ICP presentation from scratch"""
    print("\n=== Example 2: ICP Presentation ===\n")

    generator = GTMFabricPresentationGenerator()
    prs = generator.create_presentation()

    # Title slide
    generator.create_title_slide(
        prs,
        title="Example Company - Ideal Customer Profiles",
        subtitle="Cloud Platform GTM Campaign",
        date="January 2025"
    )

    # ICP 1
    generator.create_icp_slide(
        prs,
        icp_number=1,
        icp_title="Enterprise Finance Modernizer",
        industries=["Manufacturing", "Retail", "Healthcare"],
        departments="Finance, FP&A, Accounting",
        key_roles=["CFO", "VP FP&A", "Finance Director", "Controller"],
        displacement_signals=[
            {
                "pain_explanation": "Using legacy EPM systems with limited flexibility and high maintenance costs",
                "vendor_products": ["Oracle Hyperion", "SAP BPC", "IBM Cognos TM1"]
            },
            {
                "pain_explanation": "Managing disconnected Excel workbooks causing data quality issues",
                "vendor_products": ["Microsoft Excel", "Google Sheets"]
            }
        ],
        expansion_signals=[
            {
                "readiness_explanation": "Recently deployed cloud ERP for unified financial data",
                "vendor_products": ["Workday Financials", "NetSuite", "Oracle Cloud ERP"]
            },
            {
                "readiness_explanation": "Using modern BI tools for operational dashboards",
                "vendor_products": ["Power BI", "Tableau", "Looker"]
            }
        ],
        page_number=2
    )

    # ICP 2
    generator.create_icp_slide(
        prs,
        icp_number=2,
        icp_title="IT Infrastructure Director",
        industries=["Technology", "Financial Services", "Telecom"],
        departments="IT Operations, Infrastructure, Cloud Architecture",
        key_roles=["CIO", "VP Infrastructure", "Cloud Architect", "IT Director"],
        displacement_signals=[
            {
                "pain_explanation": "Running legacy on-premises infrastructure with high operational costs",
                "vendor_products": ["VMware vSphere", "Citrix XenServer"]
            },
            {
                "pain_explanation": "Using outdated monitoring tools lacking cloud visibility",
                "vendor_products": ["Nagios", "PRTG Network Monitor"]
            }
        ],
        expansion_signals=[
            {
                "readiness_explanation": "Migrating workloads to public cloud platforms",
                "vendor_products": ["AWS", "Azure", "Google Cloud"]
            },
            {
                "readiness_explanation": "Implementing modern observability platforms",
                "vendor_products": ["Datadog", "New Relic", "Splunk"]
            }
        ],
        page_number=3
    )

    # Save
    output_path = os.path.join(os.path.dirname(__file__), "example-icp.pptx")
    generator.save_presentation(prs, output_path)
    print(f"Created: {output_path}\n")


def example_3_from_json():
    """Example 3: Generate presentation from JSON file"""
    print("\n=== Example 3: From JSON Data ===\n")

    # Sample JSON data
    data = {
        "campaign_info": {
            "customer_name": "Sample Technology Vendor",
            "solution_name": "Cloud Security Platform",
            "campaign_date": "2025-01-10"
        },
        "icps": [
            {
                "icp_number": 1,
                "title": "Security Operations Center Leader",
                "industries": ["Financial Services", "Healthcare", "Government"],
                "departments_and_functions": "Security Operations, Threat Intelligence, Incident Response",
                "key_roles": [
                    "CISO",
                    "Head of Security Operations",
                    "SOC Manager",
                    "Security Architect"
                ],
                "technographic_fit": {
                    "displacement_signals": [
                        {
                            "pain_explanation": "Managing multiple disconnected security tools without centralized visibility",
                            "vendor_products": ["Splunk ES", "QRadar", "ArcSight"]
                        }
                    ],
                    "expansion_signals": [
                        {
                            "readiness_explanation": "Recently deployed cloud infrastructure requiring unified security monitoring",
                            "vendor_products": ["AWS Security Hub", "Azure Sentinel"]
                        }
                    ]
                }
            },
            {
                "icp_number": 2,
                "title": "Cloud Infrastructure Security Lead",
                "industries": ["Technology", "E-commerce", "SaaS"],
                "departments_and_functions": "Cloud Security, DevSecOps, Platform Engineering",
                "key_roles": [
                    "VP Cloud Security",
                    "Head of DevSecOps",
                    "Cloud Architect",
                    "Security Engineer"
                ],
                "technographic_fit": {
                    "displacement_signals": [
                        {
                            "pain_explanation": "Using legacy security tools not designed for cloud-native environments",
                            "vendor_products": ["Trend Micro Deep Security", "McAfee MVISION"]
                        }
                    ],
                    "expansion_signals": [
                        {
                            "readiness_explanation": "Adopting containerization and microservices architectures",
                            "vendor_products": ["Kubernetes", "Docker", "ECS"]
                        }
                    ]
                }
            }
        ]
    }

    # Save JSON to file
    json_path = os.path.join(os.path.dirname(__file__), "example-data.json")
    with open(json_path, 'w') as f:
        json.dump(data, f, indent=2)
    print(f"Created JSON: {json_path}")

    # Generate presentation from JSON
    output_path = os.path.join(os.path.dirname(__file__), "example-from-json.pptx")
    generate_icp_presentation(
        campaign_info=data['campaign_info'],
        icps=data['icps'],
        output_path=output_path
    )
    print(f"Created: {output_path}\n")


def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("GTM Fabric PowerPoint Generator - Examples")
    print("=" * 70)

    # Example 1: Basic presentation
    example_1_basic_presentation()

    # Example 2: ICP presentation from scratch
    example_2_icp_presentation()

    # Example 3: Generate from JSON
    example_3_from_json()

    print("=" * 70)
    print("All examples completed!")
    print("=" * 70 + "\n")


if __name__ == "__main__":
    main()
