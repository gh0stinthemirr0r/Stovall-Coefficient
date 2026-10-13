# Statistical estimation and uncertainty

## Preregister the target

Before viewing outputs, specify geography, observation horizon, reference age and optional preferences, the three estimands (demographic, receptive, encounter-feasible), source vintages, and missing-data assumptions. Avoid selecting favorable parameters after seeing results.

## Construct disjoint population cells

Use age-by-geography counts and calibrate survey expansion weights to documented controls. Do not add overlapping gender identity categories. If data are insufficient to reconstruct joint cells, present partially identified ranges or withhold a point estimate.

## Estimate joint probability

Prefer direct observation of the defined joint event. Alternatively fit sequential **conditional** probability models consistent with the chain rule. Report training population, model form, interactions, subgroup support, weighting, regularization and calibration. National averages cannot automatically represent San Diego subgroups.

## Transportability

Transport source-survey estimates to San Diego only if relevant predictors are observed in both samples, positivity is plausible, and differences in unmeasured factors are examined. Reweighting does not fix unobserved selection. Report sensitivity scenarios for residual geographic variation.

## Uncertainty

Propagate ACS sampling error, survey weights, probability-estimation uncertainty, missingness, geography assignment and transport assumptions. Use replicate-weight bootstrap for design-based estimates or a coherent posterior model. Preserve dependence between parameters where possible. A simulation with 10,000 draws is computational replication, not evidence by itself. Distinguish credible intervals from confidence intervals.

## Sensitivity tests

Vary availability, dating intent, bilateral age acceptance, partner-gender preference missingness, encounter horizon, app exposure, nonresponse mechanism, boundary definitions and sample selection. Publish interval and scenario results alongside any point estimate. Never report false precision.

## Required output

For each geography and configuration, report D, R and O separately, with counts, uncertainty method, model status (empirical/model-based/synthetic/unidentified), subgroup suppression, date, denominator and source references. Ensure 0 <= O <= R <= D.
