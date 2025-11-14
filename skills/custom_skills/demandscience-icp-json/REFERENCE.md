# DemandScience ICP JSON Schema Reference

## Complete JSON Schema

### Top-Level Structure

```json
{
  "campaign_metadata": { },
  "icps": [ ]
}
```

### Campaign Metadata Object

```json
{
  "campaign_metadata": {
    "demandscience_customer": "string",      // Required: Tech vendor name
    "products": ["string"],                  // Required: Array of product names
    "campaign_goal": "string",               // Required: Campaign objective
    "target_region": "string",               // Optional: Geographic scope
    "generated_date": "YYYY-MM-DD",          // Required: ISO 8601 date
    "total_icps": integer                    // Required: Count of ICPs
  }
}
```

**Field Descriptions:**
- `demandscience_customer`: The technology vendor (DemandScience's customer)
- `products`: Array of products being marketed
- `campaign_goal`: Brief description of campaign objective
- `target_region`: Geographic region (e.g., "North America", "EMEA")
- `generated_date`: Date ICPs were generated (YYYY-MM-DD format)
- `total_icps`: Number of ICPs in the array (must match array length)

### ICP Object Structure

```json
{
  "icp_id": 1,
  "title": "string",
  "industries": ["string"],
  "departments": ["string"],
  "key_roles": ["string"],
  "technographic_fit": {
    "displacement_signals": [
      {
        "pain_point": "string",
        "vendor_products": ["string"]
      }
    ],
    "expansion_signals": [
      {
        "readiness_indicator": "string",
        "vendor_products": ["string"]
      }
    ]
  }
}
```

**Field Descriptions:**
- `icp_id`: Sequential integer starting from 1
- `title`: Descriptive ICP title from Markdown
- `industries`: Array of industry names (2-4 items, max 4)
- `departments`: Array of department names (2-3 items, max 3)
- `key_roles`: Array of job titles (2-3 items, max 3)
- `technographic_fit`: Object containing displacement and expansion signals

### Signal Objects

**Displacement Signal:**
```json
{
  "pain_point": "Business problem description",
  "vendor_products": ["Vendor Product Name"]
}
```

**Expansion Signal:**
```json
{
  "readiness_indicator": "Readiness description",
  "vendor_products": ["Vendor Product Name"]
}
```

**Signal Requirements:**
- Each ICP should have 2-4 displacement signals
- Each ICP should have 2-4 expansion signals
- `vendor_products` is always an array (even for single vendor)
- Vendor names must be validated real products

## Complete Example

```json
{
  "campaign_metadata": {
    "demandscience_customer": "Vena Solutions",
    "products": [
      "Vena Complete Planning Platform"
    ],
    "campaign_goal": "Target finance teams replacing legacy Excel and EPM systems",
    "target_region": "North America",
    "generated_date": "2025-11-13",
    "total_icps": 3
  },
  "icps": [
    {
      "icp_id": 1,
      "title": "Mid-Market Technology Companies - Excel to Cloud FP&A Transformation",
      "industries": [
        "Technology",
        "SaaS",
        "Software Services",
        "IT Services"
      ],
      "departments": [
        "Finance & Accounting",
        "Financial Planning & Analysis (FP&A)",
        "Corporate Development"
      ],
      "key_roles": [
        "CFO",
        "VP Finance",
        "FP&A Director"
      ],
      "technographic_fit": {
        "displacement_signals": [
          {
            "pain_point": "Excel-based planning causing version control chaos and formula errors",
            "vendor_products": ["Microsoft Excel"]
          },
          {
            "pain_point": "Legacy on-premise systems limiting remote collaboration and cloud adoption",
            "vendor_products": ["Oracle Hyperion"]
          },
          {
            "pain_point": "Complex EPM platforms over-engineered and too expensive for mid-market needs",
            "vendor_products": ["Oracle EPM Cloud"]
          },
          {
            "pain_point": "Acquired planning tools with forced integrations and pricing increases",
            "vendor_products": ["Workday Adaptive Planning"]
          }
        ],
        "expansion_signals": [
          {
            "readiness_indicator": "Cloud ERP deployments requiring integrated financial planning capabilities",
            "vendor_products": ["NetSuite"]
          },
          {
            "readiness_indicator": "Salesforce CRM users needing unified revenue planning and forecasting",
            "vendor_products": ["Salesforce"]
          },
          {
            "readiness_indicator": "Microsoft 365 environments ready for native Excel-based planning workflows",
            "vendor_products": ["Microsoft 365"]
          },
          {
            "readiness_indicator": "Modern BI tools deployed indicating appetite for advanced analytics",
            "vendor_products": ["Power BI"]
          }
        ]
      }
    },
    {
      "icp_id": 2,
      "title": "Manufacturing Organizations - Legacy SAP/Oracle EPM Replacement",
      "industries": [
        "Manufacturing",
        "Industrial Equipment",
        "Automotive",
        "Consumer Goods"
      ],
      "departments": [
        "Finance Operations",
        "Supply Chain Planning",
        "Production Planning"
      ],
      "key_roles": [
        "Chief Financial Officer",
        "Controller",
        "Director of Financial Planning"
      ],
      "technographic_fit": {
        "displacement_signals": [
          {
            "pain_point": "Rigid SAP BPC implementations unable to support agile planning requirements",
            "vendor_products": ["SAP BPC"]
          },
          {
            "pain_point": "Legacy SAP systems transitioning to cloud with planning gaps",
            "vendor_products": ["SAP Analytics Cloud"]
          },
          {
            "pain_point": "Expensive IBM on-premise planning platforms reaching end-of-life",
            "vendor_products": ["IBM Planning Analytics"]
          },
          {
            "pain_point": "Complex Oracle implementations requiring costly consultants for changes",
            "vendor_products": ["Oracle EPM Cloud"]
          }
        ],
        "expansion_signals": [
          {
            "readiness_indicator": "SAP S/4HANA migrations creating opportunity for modern planning layer",
            "vendor_products": ["SAP S/4HANA"]
          },
          {
            "readiness_indicator": "Cloud platform investments indicating readiness for SaaS applications",
            "vendor_products": ["Microsoft Azure"]
          },
          {
            "readiness_indicator": "Advanced analytics deployments showing data-driven culture",
            "vendor_products": ["Tableau"]
          },
          {
            "readiness_indicator": "Modern collaboration tools replacing legacy systems",
            "vendor_products": ["Microsoft Teams"]
          }
        ]
      }
    },
    {
      "icp_id": 3,
      "title": "Professional Services Firms - Multi-Entity Consolidation & Project Planning",
      "industries": [
        "Professional Services",
        "Consulting",
        "Accounting Firms",
        "Legal Services"
      ],
      "departments": [
        "Finance & Administration",
        "Practice Management",
        "Client Delivery Operations"
      ],
      "key_roles": [
        "Managing Partner",
        "Chief Operating Officer",
        "VP of Finance & Operations"
      ],
      "technographic_fit": {
        "displacement_signals": [
          {
            "pain_point": "Spreadsheet models breaking with multiple offices and regional expansion",
            "vendor_products": ["Microsoft Excel"]
          },
          {
            "pain_point": "Manual consolidation processes consuming weeks each quarter",
            "vendor_products": ["Excel Consolidation"]
          },
          {
            "pain_point": "Legacy planning tools lacking project-based revenue forecasting capabilities",
            "vendor_products": ["Host Analytics"]
          },
          {
            "pain_point": "On-premise EPM systems preventing real-time visibility across locations",
            "vendor_products": ["IBM TM1"]
          }
        ],
        "expansion_signals": [
          {
            "readiness_indicator": "Professional services automation platforms needing financial planning integration",
            "vendor_products": ["Salesforce Professional Services Cloud"]
          },
          {
            "readiness_indicator": "Cloud accounting systems requiring advanced planning capabilities",
            "vendor_products": ["NetSuite"]
          },
          {
            "readiness_indicator": "Project management tools deployed indicating need for financial project planning",
            "vendor_products": ["Microsoft Dynamics 365"]
          },
          {
            "readiness_indicator": "Business intelligence investments showing demand for planning analytics",
            "vendor_products": ["Qlik"]
          }
        ]
      }
    }
  ]
}
```

## Schema Validation Rules

### Data Types

| Field | Type | Required | Constraints |
|-------|------|----------|-------------|
| `demandscience_customer` | string | Yes | Non-empty |
| `products` | array[string] | Yes | Min 1 item |
| `campaign_goal` | string | Yes | Non-empty |
| `target_region` | string | No | - |
| `generated_date` | string | Yes | ISO 8601 (YYYY-MM-DD) |
| `total_icps` | integer | Yes | Min 3, must match array length |
| `icp_id` | integer | Yes | Sequential from 1 |
| `title` | string | Yes | Non-empty |
| `industries` | array[string] | Yes | Min 2, Max 4 |
| `departments` | array[string] | Yes | Min 2, Max 3 |
| `key_roles` | array[string] | Yes | Min 2, Max 3 |
| `pain_point` | string | Yes | Non-empty |
| `readiness_indicator` | string | Yes | Non-empty |
| `vendor_products` | array[string] | Yes | Min 1 item |

### Naming Conventions

**All field names MUST use snake_case:**
- ✅ Correct: `demandscience_customer`, `vendor_products`, `key_roles`
- ❌ Wrong: `demandScienceCustomer`, `VendorProducts`, `KeyRoles`

### Array Formatting

**All arrays must be properly formatted even for single items:**
- ✅ Correct: `["NetSuite"]`
- ❌ Wrong: `"NetSuite"`

**Examples:**
```json
"products": ["Single Product"],              // Correct
"industries": ["Technology", "Healthcare"],   // Correct
"vendor_products": ["Oracle EPM Cloud"]      // Correct
```

### Date Format

**Use ISO 8601 format (YYYY-MM-DD):**
- ✅ Correct: `"2025-11-13"`
- ❌ Wrong: `"11/13/2025"`, `"Nov 13, 2025"`

## Conversion Rules

### Markdown → JSON Mapping

**Title:**
```markdown
## ICP 1: Mid-Market Technology - Cloud FP&A Transformation
```
→
```json
"title": "Mid-Market Technology - Cloud FP&A Transformation"
```

**Industries (comma-separated → array):**
```markdown
- Technology, SaaS, Software Services, IT Services
```
→
```json
"industries": ["Technology", "SaaS", "Software Services", "IT Services"]
```

**Departments (bullets → array):**
```markdown
- Finance & Accounting
- FP&A
- Corporate Development
```
→
```json
"departments": ["Finance & Accounting", "FP&A", "Corporate Development"]
```

**Signals (split on `→`):**
```markdown
- Excel planning causing errors → **Microsoft Excel**
```
→
```json
{
  "pain_point": "Excel planning causing errors",
  "vendor_products": ["Microsoft Excel"]
}
```

**Multi-vendor signals:**
```markdown
- Legacy systems limiting collaboration → **Oracle Hyperion**, **SAP BPC**
```
→
```json
{
  "pain_point": "Legacy systems limiting collaboration",
  "vendor_products": ["Oracle Hyperion", "SAP BPC"]
}
```

## Validation Code Examples

### Python Validation

```python
import json
from datetime import datetime

def validate_icp_json(data):
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
    meta = data["campaign_metadata"]
    required_meta_fields = [
        "demandscience_customer",
        "products",
        "campaign_goal",
        "generated_date",
        "total_icps"
    ]

    for field in required_meta_fields:
        if field not in meta:
            errors.append(f"Missing campaign_metadata.{field}")

    # Validate date format
    if "generated_date" in meta:
        try:
            datetime.strptime(meta["generated_date"], "%Y-%m-%d")
        except ValueError:
            errors.append(f"Invalid date format: {meta['generated_date']}")

    # Validate ICPs array
    icps = data["icps"]
    if not isinstance(icps, list):
        errors.append("icps must be an array")
        return False, errors

    if len(icps) < 3:
        errors.append(f"Expected at least 3 ICPs, got {len(icps)}")

    if meta.get("total_icps") != len(icps):
        errors.append(f"total_icps ({meta.get('total_icps')}) doesn't match array length ({len(icps)})")

    # Validate each ICP
    required_icp_fields = [
        "icp_id", "title", "industries",
        "departments", "key_roles", "technographic_fit"
    ]

    for i, icp in enumerate(icps):
        # Check required fields
        for field in required_icp_fields:
            if field not in icp:
                errors.append(f"ICP {i+1} missing field: {field}")

        # Check ICP ID is sequential
        if icp.get("icp_id") != i + 1:
            errors.append(f"ICP {i+1} has wrong icp_id: {icp.get('icp_id')}")

        # Check array constraints
        industries = icp.get("industries", [])
        if len(industries) < 2 or len(industries) > 4:
            errors.append(f"ICP {i+1} industries must be 2-4 items, got {len(industries)}")

        departments = icp.get("departments", [])
        if len(departments) < 2 or len(departments) > 3:
            errors.append(f"ICP {i+1} departments must be 2-3 items, got {len(departments)}")

        # Check technographic_fit structure
        if "technographic_fit" in icp:
            tf = icp["technographic_fit"]

            if "displacement_signals" not in tf:
                errors.append(f"ICP {i+1} missing displacement_signals")
            if "expansion_signals" not in tf:
                errors.append(f"ICP {i+1} missing expansion_signals")

            # Validate signal structure
            for signal_type in ["displacement_signals", "expansion_signals"]:
                if signal_type in tf:
                    for j, signal in enumerate(tf[signal_type]):
                        key = "pain_point" if "displacement" in signal_type else "readiness_indicator"

                        if key not in signal:
                            errors.append(f"ICP {i+1} {signal_type}[{j}] missing {key}")

                        if "vendor_products" not in signal:
                            errors.append(f"ICP {i+1} {signal_type}[{j}] missing vendor_products")
                        elif not isinstance(signal["vendor_products"], list):
                            errors.append(f"ICP {i+1} {signal_type}[{j}] vendor_products must be array")

    if errors:
        return False, errors

    return True, ["Valid"]

# Usage
with open("icps.json") as f:
    data = json.load(f)

is_valid, messages = validate_icp_json(data)
if is_valid:
    print("✅ JSON is valid")
else:
    print("❌ Validation errors:")
    for msg in messages:
        print(f"  - {msg}")
```

## Common Errors and Solutions

### Error: Invalid JSON Syntax

**Problem:**
```json
{
  "demandscience_customer": "Vena Solutions",  // Missing comma
  "products": ["Vena Platform"]
}
```

**Solution:**
```json
{
  "demandscience_customer": "Vena Solutions",
  "products": ["Vena Platform"]
}
```

### Error: Wrong Naming Convention

**Problem:**
```json
{
  "demandScienceCustomer": "Vena Solutions",  // camelCase
  "vendorProducts": ["Oracle"]                // camelCase
}
```

**Solution:**
```json
{
  "demandscience_customer": "Vena Solutions",  // snake_case
  "vendor_products": ["Oracle"]                // snake_case
}
```

### Error: Array Not Formatted

**Problem:**
```json
{
  "industries": "Technology",            // String instead of array
  "vendor_products": "Oracle Hyperion"   // String instead of array
}
```

**Solution:**
```json
{
  "industries": ["Technology"],           // Array
  "vendor_products": ["Oracle Hyperion"]  // Array
}
```

### Error: Missing Required Fields

**Problem:**
```json
{
  "icp_id": 1,
  "title": "Some Title"
  // Missing: industries, departments, key_roles, technographic_fit
}
```

**Solution:**
```json
{
  "icp_id": 1,
  "title": "Some Title",
  "industries": ["Technology", "Healthcare"],
  "departments": ["Finance", "IT"],
  "key_roles": ["CFO", "CIO"],
  "technographic_fit": {
    "displacement_signals": [...],
    "expansion_signals": [...]
  }
}
```

## Integration Examples

### Save to File

```python
import json

# Save formatted JSON
with open("icps.json", "w") as f:
    json.dump(icps_data, f, indent=2)
```

### Load and Parse

```python
import json

# Load from file
with open("icps.json") as f:
    data = json.load(f)

# Access fields
customer = data["campaign_metadata"]["demandscience_customer"]
first_icp = data["icps"][0]
industries = first_icp["industries"]
```

### Convert to DataFrame

```python
import pandas as pd
import json

with open("icps.json") as f:
    data = json.load(f)

# Flatten ICPs to DataFrame
icps_df = pd.json_normalize(data["icps"])
print(icps_df.head())
```

### Insert into Database

```python
import json
import sqlite3

with open("icps.json") as f:
    data = json.load(f)

conn = sqlite3.connect("icps.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS icps (
        icp_id INTEGER PRIMARY KEY,
        customer TEXT,
        title TEXT,
        industries TEXT,
        departments TEXT,
        roles TEXT,
        created_date TEXT
    )
""")

# Insert ICPs
for icp in data["icps"]:
    cursor.execute("""
        INSERT INTO icps VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        icp["icp_id"],
        data["campaign_metadata"]["demandscience_customer"],
        icp["title"],
        json.dumps(icp["industries"]),
        json.dumps(icp["departments"]),
        json.dumps(icp["key_roles"]),
        data["campaign_metadata"]["generated_date"]
    ))

conn.commit()
conn.close()
```
