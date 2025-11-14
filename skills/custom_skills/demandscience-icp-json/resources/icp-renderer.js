/**
 * ICP Sales Report Renderer
 * Dynamically populates HTML page with JSON data from demandscience-icp-json skill
 *
 * Data Flow:
 * 1. Fetch JSON from /data/icps.json
 * 2. Render campaign metadata in sidebar
 * 3. Dynamically generate ICP cards
 * 4. Handle variable-length arrays (industries, departments, signals, etc.)
 */

class ICPRenderer {
    constructor(jsonPath = '/data/icps.json') {
        this.jsonPath = jsonPath;
        this.data = null;
    }

    /**
     * Initialize: Load JSON and render all content
     */
    async init() {
        try {
            await this.loadJSON();
            this.renderCampaignMetadata();
            this.renderICPs();
            console.log('✅ ICP Sales Report rendered successfully');
        } catch (error) {
            this.handleError(error);
        }
    }

    /**
     * Fetch JSON data from file or API
     */
    async loadJSON() {
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
    }

    /**
     * Validate JSON structure matches expected schema
     */
    validateData() {
        if (!this.data) {
            throw new Error('No data loaded');
        }
        if (!this.data.campaign_metadata) {
            throw new Error('Missing campaign_metadata in JSON');
        }
        if (!this.data.icps || !Array.isArray(this.data.icps)) {
            throw new Error('Missing or invalid icps array in JSON');
        }
        if (this.data.icps.length === 0) {
            throw new Error('No ICPs found in JSON data');
        }
    }

    /**
     * Render campaign metadata in sidebar
     */
    renderCampaignMetadata() {
        const meta = this.data.campaign_metadata;

        // Customer name and label
        this.setTextContent('.sidebar-customer-name', meta.demandscience_customer);

        // Campaign objective
        this.setTextContent('.sidebar-section .sidebar-detail-value', meta.campaign_goal);

        // Products (join array with commas)
        const productsElement = document.querySelector('.sidebar-detail-item .sidebar-detail-value');
        if (productsElement && meta.products) {
            productsElement.textContent = meta.products.join(', ');
        }

        // Target region
        const detailItems = document.querySelectorAll('.sidebar-detail-item');
        detailItems.forEach(item => {
            const label = item.querySelector('.sidebar-detail-label');
            const value = item.querySelector('.sidebar-detail-value');
            if (!label || !value) return;

            switch (label.textContent.trim()) {
                case 'Products':
                    value.textContent = meta.products ? meta.products.join(', ') : 'N/A';
                    break;
                case 'Target Region':
                    value.textContent = meta.target_region || 'N/A';
                    break;
                case 'Generated':
                    value.textContent = this.formatDate(meta.generated_date);
                    break;
                case 'Total ICPs':
                    value.textContent = meta.total_icps || this.data.icps.length;
                    break;
            }
        });
    }

    /**
     * Render all ICP cards dynamically
     */
    renderICPs() {
        // Find the container where ICP cards should be inserted
        // They appear after the Propensity Funnel card
        const container = document.querySelector('.main-content-wrapper .container');
        if (!container) {
            throw new Error('Main content container not found');
        }

        // Remove existing ICP cards (the placeholder ones)
        const existingICPCards = container.querySelectorAll('.icp-card');
        existingICPCards.forEach(card => card.remove());

        // Generate new ICP cards from JSON data
        this.data.icps.forEach((icp, index) => {
            const icpCard = this.createICPCard(icp, index);
            container.appendChild(icpCard);
        });
    }

    /**
     * Create a single ICP card element
     */
    createICPCard(icp, index) {
        const card = document.createElement('div');
        card.className = 'icp-card';
        card.innerHTML = `
            <div class="icp-header">
                <div class="icp-icon"><img src="assets/icons/gtmfabric_darkpurple_icon.png" alt="ICP Icon"></div>
                <h2>${this.escapeHtml(icp.title)}</h2>
            </div>

            <div class="icp-grid">
                <!-- Row 1: Industries & Departments -->
                <div class="p-6" style="background: #fafbfc; border: 1px solid #e2e8f0; border-radius: 12px;">
                    <div class="icp-section">
                        <div class="icp-section-header">
                            <div class="icp-section-icon"><img src="assets/icons/industries_icon.png" alt="Industries"></div>
                            <h4 class="icp-section-title">Industries</h4>
                        </div>
                        <div class="flex" style="flex-wrap: wrap; gap: 8px; margin-top: 12px;">
                            ${this.renderIndustryBadges(icp.industries)}
                        </div>
                    </div>
                </div>

                <div class="p-6" style="background: #fafbfc; border: 1px solid #e2e8f0; border-radius: 12px;">
                    <div class="icp-section">
                        <div class="icp-section-header">
                            <div class="icp-section-icon"><img src="assets/icons/departmentsfunctions_icon.png" alt="Departments"></div>
                            <h4 class="icp-section-title">Departments & Functions</h4>
                        </div>
                        <ul class="icp-list">
                            ${this.renderList(icp.departments)}
                        </ul>
                    </div>
                </div>

                <!-- Row 2: Key Roles (spans 2 columns) -->
                <div class="p-6" style="background: #fafbfc; border: 1px solid #e2e8f0; border-radius: 12px; grid-column: span 2;">
                    <div class="icp-section">
                        <div class="icp-section-header">
                            <div class="icp-section-icon"><img src="assets/icons/keyroles_icon.png" alt="Key Roles"></div>
                            <h4 class="icp-section-title">Key Roles</h4>
                        </div>
                        <ul class="icp-list">
                            ${this.renderList(icp.key_roles)}
                        </ul>
                    </div>
                </div>

                <!-- Row 3: Technographic Fit (spans 2 columns) -->
                <div class="p-6" style="background: #fafbfc; border: 1px solid #e2e8f0; border-radius: 12px; grid-column: span 2;">
                    <div class="icp-section">
                        <div class="icp-section-header">
                            <div class="icp-section-icon"><img src="assets/icons/technographicFit_icon.png" alt="Technographic Fit"></div>
                            <h4 class="icp-section-title">Technographic Fit</h4>
                        </div>

                        <div class="grid-2" style="gap: 24px; margin-top: 16px;">
                            <div>
                                <h4 style="font-size: 16px; font-weight: 600; color: #320064; margin-bottom: 12px;">Displacement / Modernization Signals</h4>
                                ${this.renderSignals(icp.technographic_fit.displacement_signals, 'pain_point')}
                            </div>
                            <div>
                                <h4 style="font-size: 16px; font-weight: 600; color: #320064; margin-bottom: 12px;">Expansion Signals</h4>
                                ${this.renderSignals(icp.technographic_fit.expansion_signals, 'readiness_indicator')}
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        `;
        return card;
    }

    /**
     * Render industry badges
     */
    renderIndustryBadges(industries) {
        if (!industries || industries.length === 0) {
            return '<span class="industry-badge">No industries specified</span>';
        }
        return industries
            .map(industry => `<span class="industry-badge">${this.escapeHtml(industry)}</span>`)
            .join('');
    }

    /**
     * Render a simple list
     */
    renderList(items) {
        if (!items || items.length === 0) {
            return '<li>No items specified</li>';
        }
        return items
            .map(item => `<li>${this.escapeHtml(item)}</li>`)
            .join('');
    }

    /**
     * Render technographic signals
     */
    renderSignals(signals, textField) {
        if (!signals || signals.length === 0) {
            return '<div class="signal-item">No signals specified</div>';
        }
        return signals
            .map(signal => `<div class="signal-item">${this.escapeHtml(signal[textField])}</div>`)
            .join('');
    }

    /**
     * Format date string
     */
    formatDate(dateString) {
        if (!dateString) return 'N/A';
        try {
            const date = new Date(dateString);
            return date.toLocaleDateString('en-US', {
                year: 'numeric',
                month: 'long',
                day: 'numeric'
            });
        } catch (error) {
            return dateString;
        }
    }

    /**
     * Safely set text content
     */
    setTextContent(selector, text) {
        const element = document.querySelector(selector);
        if (element) {
            element.textContent = text || 'N/A';
        }
    }

    /**
     * Escape HTML to prevent XSS
     */
    escapeHtml(text) {
        if (!text) return '';
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    /**
     * Handle errors gracefully
     */
    handleError(error) {
        console.error('❌ ICP Renderer Error:', error);

        // Display user-friendly error message
        const container = document.querySelector('.main-content-wrapper .container');
        if (container) {
            container.innerHTML = `
                <div class="card" style="background: #fef2f2; border-color: #fecaca;">
                    <h2 style="color: #991b1b; margin-bottom: 16px;">⚠️ Failed to Load ICP Data</h2>
                    <p style="color: #7f1d1d; margin-bottom: 12px;"><strong>Error:</strong> ${this.escapeHtml(error.message)}</p>
                    <p style="color: #7f1d1d; font-size: 16px;">Please ensure:</p>
                    <ul style="color: #7f1d1d; font-size: 16px; margin-left: 24px;">
                        <li>The JSON file exists at <code>/data/icps.json</code></li>
                        <li>The JSON is valid and matches the expected schema</li>
                        <li>The server is running and serving static files correctly</li>
                    </ul>
                </div>
            `;
        }
    }
}

// Initialize renderer when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    const renderer = new ICPRenderer();
    renderer.init();
});
