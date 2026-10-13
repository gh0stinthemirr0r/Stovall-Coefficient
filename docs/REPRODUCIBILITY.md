# Reproducibility and publication checklist

## Minimum reproducible release

- Pin the manuscript version, repository commit, Python version and random seed.
- Include public data source URLs, vintage, API queries, variable IDs, geography, margins of error and retrieval dates.
- Include the exact statistical estimand, adult eligibility rule, optional filters, horizon and weighting method.
- Provide documented source-to-analysis transformations, schema checks and tests.
- Distinguish synthetic demonstration data from empirical inputs in filenames and output labels.
- Report missingness, survey selection, transport assumptions and uncertainty construction.
- Release only non-identifying and appropriately licensed data.
- Verify bibliography and citation metadata before submitting to a journal or preprint archive.

## Suggested workflow

1. Freeze an analysis plan and provenance manifest.
2. Download ACS counts using a pinned vintage.
3. Harmonize and validate unique cells; do not impute unsupported identities.
4. Obtain or collect defensible joint-preference evidence.
5. Estimate D/R/O with intervals and sensitivity analysis.
6. Evaluate calibration in a holdout population.
7. Produce a tagged release, reproducibility report and limitations disclosure.

## Verification commands

```bash
python -m unittest discover -s tests -v
python src/stovall.py --example
```

The included Python program is a transparent **calculation engine for known cell-level joint probabilities**, not a fitted predictive model. It cannot independently estimate attraction or demographic prevalence.
