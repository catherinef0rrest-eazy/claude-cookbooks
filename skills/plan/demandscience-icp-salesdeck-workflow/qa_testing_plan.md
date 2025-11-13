# QA Testing & Evaluation Plan
## DemandScience ICP Skill

## Overview
Simple, practical testing approach to ensure consistent, high-quality ICP outputs. Focus on the 20% of testing that catches 80% of issues.

---

## 1. Golden Test Cases (3-5 Examples)

Maintain a small set of real DemandScience briefs that represent common scenarios:

### Test Case 1: Competitive Displacement
- **Input**: Vena Solutions campaign replacing Oracle/SAP EPM
- **Expected**: 3+ ICPs with finance buyers, validated legacy products, FP&A pain points

### Test Case 2: New Market Entry
- **Input**: Kaspersky XDRO targeting mid-market financial services
- **Expected**: 3+ ICPs with security buyers, validated endpoint products, compliance drivers

### Test Case 3: Expansion/Upsell
- **Input**: Autodesk commercial license upgrades in EU
- **Expected**: 3+ ICPs with CAD users, free-to-paid motion, regional context

**Action**: Run these monthly or after significant skill changes. Keep actual outputs as reference.

---

## 2. Automated Format Checks

Simple validation checklist to verify output structure:

```
✓ Output is valid Markdown
✓ Contains at least 3 ICP sections
✓ Each ICP has: Industries, Departments, Technographic Fit
✓ Vendor names are in bold (**VendorName**)
✓ Review prompt is included at end
✓ No JSON artifacts or code fences around main content
```

**Action**: Run on every test case output. Takes 2 minutes manually.

---

## 3. Quality Spot Checks

Review 1-2 ICPs per test run for content quality:

### Research Quality
- [ ] Vendor names are real companies (Google them)
- [ ] Products still exist in 2025
- [ ] Pain points make business sense
- [ ] Industries match the solution

### Content Quality
- [ ] Each ICP is distinct (not repetitive)
- [ ] Business reasoning comes before vendor names
- [ ] Tone is executive-level (not jargon-heavy)
- [ ] No placeholder text like "[Industry]" or "[TBD]"

**Action**: 5-minute manual review per test case.

---

## 4. Consistency Check

Compare outputs from same input run twice:

- Run same test case 2-3 times
- Check: Do all runs produce 3+ ICPs?
- Check: Are vendor names consistent and real?
- Check: Is quality similar across runs?

**Red flags**:
- Drastically different ICP counts
- Made-up vendor names in some runs
- Inconsistent structure or format

**Action**: Do this quarterly or when skill logic changes.

---

## 5. Real-World Validation

Once per month, test with actual new DemandScience request:

1. Run skill on real brief
2. Before delivering to DemandScience, check:
   - [ ] All vendors are real (spot check 5-10)
   - [ ] ICPs are distinct
   - [ ] Format is clean Markdown
3. After delivery, note any feedback from DemandScience/Liam/Ashwin

**Action**: Track feedback in simple log (see below).

---

## 6. Feedback Log

Simple tracking of real-world issues:

| Date | Issue | Fix Applied | Re-tested? |
|------|-------|-------------|------------|
| 2025-11-15 | Outdated vendor "McAfee ePO" | Updated research examples | ✓ |
| | | | |

**Action**: Update quarterly or when patterns emerge.

---

## Quick Test Workflow

### Before Deploying Skill Updates:
1. Run 3 golden test cases (10 min)
2. Format check all outputs (5 min)
3. Spot check quality on 2 ICPs (5 min)
4. **Total: ~20 minutes**

### Monthly Health Check:
1. Run golden test cases
2. Consistency check (same input 2x)
3. Real-world validation with new brief
4. Review feedback log
5. **Total: ~30 minutes**

---

## Success Criteria

The skill is working well if:
- ✓ All golden test cases produce 3+ ICPs
- ✓ Format checks pass 100% of time
- ✓ No made-up vendor names in spot checks
- ✓ Real-world feedback is positive
- ✓ Outputs are consistent across runs

## Failure Triggers

Stop and fix if:
- ✗ Test case produces < 3 ICPs
- ✗ Made-up vendor names appear
- ✗ Markdown format is broken
- ✗ DemandScience reports quality issues
- ✗ Inconsistent outputs from same input

---

## Tools Needed

**Minimal setup**:
- Folder with golden test case inputs (txt files)
- Folder for test outputs (dated)
- Simple checklist (this doc)
- Feedback log (table above or simple spreadsheet)

**Optional automation**:
- Python script to validate Markdown structure
- Script to check for common issues (e.g., "[TBD]", missing bold formatting)

---

## Maintenance

- **Weekly**: None (only test before changes)
- **Monthly**: Run health check (~30 min)
- **Quarterly**: Update golden test cases if business changes, refresh vendor examples
- **As needed**: Add new test case when encounter new scenario type

---

## Notes

- Keep it simple - manual checks are fine for this volume
- Focus on catching breaking changes and quality issues
- Don't over-engineer - this skill runs maybe 5-10x/month
- Real-world feedback is the best signal
