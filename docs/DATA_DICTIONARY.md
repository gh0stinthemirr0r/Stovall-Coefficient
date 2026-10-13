# Data dictionary

Unit of analysis: a unique consenting adult or a mutually exclusive, disclosure-safe aggregate cell. Age is measured in completed years on a specified date. Unknown values are never assumed negative.

| Field | Type | Definition / rule |
|---|---|---|
| `cell_id` | string | Unique, non-identifying cell identifier |
| `count` | nonnegative float | Population-weighted count of distinct adults |
| `age_min`, `age_max` | integers | Inclusive bounds, minimum 18; split partially overlapping bins |
| `geography_id` | string | Reproducible boundary, such as Census GEOID |
| `as_of` | ISO date | Population/reference date |
| `gender_identity` | voluntary labels | May be multi-label; not inferred from ACS sex |
| `trans_experience` | optional | Distinct from gender identity |
| `sexual_orientation` | optional | Does not determine actual partner acceptance |
| `partner_gender_preferences` | optional | Expressed, possibly graded preferences |
| `relationship_intent` | optional multi-select | Long-term, casual, either, undecided etc. |
| `p_mutual` | [0,1] | Joint probability of availability, intent and reciprocal consideration |
| `p_encounter_given_mutual` | [0,1] | Conditional encounter-feasibility probability for stated horizon |
| `source_id` | string | Provenance identifier; required for empirical inputs |
| `design_weight` | positive | Expansion weight, when survey-based |

**Validation:** disjoint cells; no negative counts; no probabilities outside [0,1]; consistent geography, dates and horizon; documented missingness; no double counting of overlapping identities; monotonic demographic/receptive/encounter funnel. Suppressed small cells remain suppressed in published outputs.
