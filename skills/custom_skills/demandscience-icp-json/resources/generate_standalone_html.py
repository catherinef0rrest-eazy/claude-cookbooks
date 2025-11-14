#!/usr/bin/env python3
"""
Generate Complete Standalone HTML Report
For use by the demandscience-icp-json Claude Skill

This script generates a self-contained HTML file with:
- All CSS embedded
- All images embedded as data URIs
- JSON data embedded
- JavaScript renderer embedded

Usage:
    python generate_standalone_html.py input.json output.html
"""

import json
import sys
from pathlib import Path

def load_json_data(json_path):
    """Load ICP JSON data"""
    with open(json_path, 'r') as f:
        return json.load(f)

def load_embedded_assets():
    """Load embedded assets JavaScript"""
    assets_path = Path(__file__).parent / 'embedded_assets.js'
    with open(assets_path, 'r') as f:
        return f.read()

def load_css():
    """Extract CSS from index.html"""
    index_path = Path(__file__).parent / 'index.html'
    with open(index_path, 'r') as f:
        content = f.read()

    # Extract CSS between <style> tags
    start = content.find('<style>') + 7
    end = content.find('</style>')
    return content[start:end]

def load_renderer_js():
    """Load the JavaScript renderer"""
    renderer_path = Path(__file__).parent / 'icp-renderer.js'
    with open(renderer_path, 'r') as f:
        return f.read()

def generate_html(json_data):
    """Generate complete standalone HTML"""

    customer_name = json_data['campaign_metadata']['demandscience_customer']

    # Load all components
    css = load_css()
    assets_js = load_embedded_assets()
    renderer_js = load_renderer_js()

    # Adapt renderer to use embedded assets
    renderer_adapted = adapt_renderer_for_embedded_assets(renderer_js)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>ICP Sales Report - {customer_name}</title>
    <meta name="description" content="Technology intelligence report for {customer_name} demonstrating AI-powered ICP insights.">
    <style>
{css}
    </style>
</head>
<body>
    <!-- Left Sidebar -->
    <div class="sidebar">
        <div class="sidebar-content">
            <!-- Demand Science Logo at Top -->
            <div class="sidebar-top-section">
                <img id="demandscience-logo" alt="Demand Science">
            </div>

            <!-- Customer Section -->
            <div class="sidebar-customer-section">
                <div class="sidebar-customer-info">
                    <div class="sidebar-customer-name"></div>
                    <div class="sidebar-customer-label">Campaign Report</div>
                </div>
            </div>

            <!-- Campaign Goal Section -->
            <div class="sidebar-section">
                <div class="sidebar-section-header">
                    <div class="sidebar-section-title">Campaign Objective</div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-value"></div>
                </div>
            </div>

            <!-- Campaign Details Section -->
            <div class="sidebar-section">
                <div class="sidebar-section-header">
                    <div class="sidebar-section-title">Campaign Details</div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Products</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Target Region</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Generated</div>
                    <div class="sidebar-detail-value"></div>
                </div>
                <div class="sidebar-detail-item">
                    <div class="sidebar-detail-label">Total ICPs</div>
                    <div class="sidebar-detail-value"></div>
                </div>
            </div>

            <!-- GTM Fabric Logo at Bottom -->
            <div class="sidebar-bottom-section">
                <img id="gtmfabric-footer" alt="GTM Fabric" class="sidebar-bottom-logo">
            </div>
        </div>
    </div>

    <div class="main-content-wrapper">
        <div class="container">
            <!-- Propensity Funnel -->
            <div class="card" style="margin-bottom: 48px;">
                <div class="icp-header">
                    <div class="icp-icon"><img id="funnel-icon" alt="Funnel Icon"></div>
                    <h2>Propensity Funnel</h2>
                </div>

                <div class="funnel-grid">
                    <!-- Left Side: Level Details -->
                    <div>
                        <!-- Level 1 -->
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Market to Account View</h3>
                            <ul class="funnel-level-list">
                                <li>Define the ideal client profile</li>
                                <li>What does an ideal customer look like?</li>
                                <li>Who's in the right buying group?</li>
                            </ul>
                        </div>

                        <!-- Level 2 -->
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Research & Intent</h3>
                            <ul class="funnel-level-list">
                                <li>Propensity to buy (Buyer Intent)</li>
                                <li>Research shows interest</li>
                                <li>Who's researching now?</li>
                            </ul>
                        </div>

                        <!-- Level 3 -->
                        <div class="funnel-level-box">
                            <h3 class="funnel-level-title">Engagement & Outreach</h3>
                            <ul class="funnel-level-list">
                                <li>SDR contact & qualification</li>
                                <li>AE demos & sales</li>
                                <li>Who's ready to talk?</li>
                            </ul>
                        </div>
                    </div>

                    <!-- Right Side: Visual Funnel -->
                    <div class="funnel-visual">
                        <!-- Stage 1: Propensity Fit -->
                        <div class="funnel-stage" style="width: 100%; border: 3px solid #9333ea;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(147, 51, 234, 0.1) 0%, rgba(168, 85, 247, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Propensity Fit</h4>
                                <p class="funnel-stage-label">Ideal Customer Profile</p>
                            </div>
                        </div>

                        <!-- Arrow -->
                        <div class="funnel-arrow">
                            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>

                        <!-- Stage 2: Research & Intent -->
                        <div class="funnel-stage" style="width: 85%; border: 3px solid #a855f7;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(168, 85, 247, 0.1) 0%, rgba(192, 132, 252, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Research & Intent</h4>
                                <p class="funnel-stage-label">Active Buyers</p>
                            </div>
                        </div>

                        <!-- Arrow -->
                        <div class="funnel-arrow">
                            <svg width="24" height="24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                <polyline points="6 9 12 15 18 9"></polyline>
                            </svg>
                        </div>

                        <!-- Stage 3: Engagement -->
                        <div class="funnel-stage" style="width: 65%; border: 3px solid #c084fc;">
                            <div class="funnel-stage-inner" style="background: linear-gradient(135deg, rgba(192, 132, 252, 0.1) 0%, rgba(216, 180, 254, 0.1) 100%);"></div>
                            <div class="funnel-stage-content">
                                <h4 class="funnel-stage-title">Engagement</h4>
                                <p class="funnel-stage-label">Sales Qualified</p>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- ICP Cards will be inserted here by JavaScript -->
            <div id="icp-container"></div>
        </div>
    </div>

    <script>
{assets_js}

// Embedded ICP Data
const ICP_DATA = {json.dumps(json_data, indent=2)};

{renderer_adapted}

// Initialize embedded assets
function loadEmbeddedAssets() {{
    // Set logo images
    document.getElementById('demandscience-logo').src = EMBEDDED_ASSETS.logos.demandscience;
    document.getElementById('gtmfabric-footer').src = EMBEDDED_ASSETS.images.sidebar_footer;
    document.getElementById('funnel-icon').src = EMBEDDED_ASSETS.icons.gtmfabric_darkpurple;
}}

// Initialize when DOM is ready
document.addEventListener('DOMContentLoaded', () => {{
    loadEmbeddedAssets();
    const renderer = new ICPRenderer(ICP_DATA);
    renderer.init();
}});
    </script>
</body>
</html>'''

    return html

def adapt_renderer_for_embedded_assets(renderer_js):
    """Adapt renderer to use EMBEDDED_ASSETS instead of file paths"""

    # Replace image src paths with embedded asset references
    replacements = {
        'src="assets/icons/gtmfabric_darkpurple_icon.png"': 'src="${EMBEDDED_ASSETS.icons.gtmfabric_darkpurple}"',
        'src="assets/icons/industries_icon.png"': 'src="${EMBEDDED_ASSETS.icons.industries}"',
        'src="assets/icons/departmentsfunctions_icon.png"': 'src="${EMBEDDED_ASSETS.icons.departmentsfunctions}"',
        'src="assets/icons/keyroles_icon.png"': 'src="${EMBEDDED_ASSETS.icons.keyroles}"',
        'src="assets/icons/technographicFit_icon.png"': 'src="${EMBEDDED_ASSETS.icons.technographicFit}"',
    }

    adapted = renderer_js
    for old, new in replacements.items():
        adapted = adapted.replace(old, new)

    # Remove the fetch() logic and constructor parameter
    adapted = adapted.replace(
        'constructor(jsonPath = \'/data/icps.json\')',
        'constructor(data)'
    )
    adapted = adapted.replace(
        'this.jsonPath = jsonPath;',
        '// Data passed directly to constructor'
    )

    # Replace loadJSON method
    adapted = adapted.replace(
        '''async loadJSON() {
        try {
            const response = await fetch(this.jsonPath);
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            this.data = await response.json();
            this.validateData();
        } catch (error) {
            throw new Error(`Failed to load ICP data: ${error.message}`);
        }
    }''',
        '''async loadJSON() {
        // Data already loaded in constructor
        this.validateData();
    }'''
    )

    return adapted

def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_standalone_html.py input.json output.html")
        sys.exit(1)

    input_json = sys.argv[1]
    output_html = sys.argv[2]

    print(f"Loading JSON data from: {input_json}")
    json_data = load_json_data(input_json)

    print(f"Generating standalone HTML...")
    html = generate_html(json_data)

    print(f"Writing HTML to: {output_html}")
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)

    file_size = Path(output_html).stat().st_size / 1024
    print(f"\n✅ Standalone HTML generated successfully!")
    print(f"   File: {output_html}")
    print(f"   Size: {file_size:.1f} KB")
    print(f"\n📂 Open the file in any web browser to view the report.")

if __name__ == '__main__':
    main()
