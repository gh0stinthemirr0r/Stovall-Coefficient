# Data sources and acquisition

## Population denominators

Use Census Bureau ACS data for San Diego County or explicitly constructed geographic areas. ACS table B01001 supplies age by reported sex; B12002 supplies age by sex by marital status. **Neither measures the full spectrum of gender identity or actual dating availability.** Record ACS release year, geography, table IDs, margins of error and query URLs.

- https://api.census.gov/data.html
- https://www.census.gov/programs-surveys/acs
- https://data.census.gov/table/ACSDT5Y2024.B01001
- https://data.census.gov/table/ACSDT5Y2024.B12002

## Relationship and dating evidence

Pew Research Center reports on single adults and dating preferences. Published national percentages cannot be applied mechanically to every San Diego age/gender/orientation subgroup. Inspect question wording, weighting, survey frame, collection dates, subgroup sample sizes and definition of single.

- https://www.pewresearch.org/social-trends/2020/08/20/a-profile-of-single-americans/
- https://www.pewresearch.org/short-reads/2023/02/08/for-valentines-day-5-facts-about-single-americans/

## Gender identity and orientation

Consult probability-based surveys and Williams Institute estimates, but distinguish national/state prevalence from local joint distributions. Avoid treating transgender, nonbinary and women as additive disjoint totals.

- https://williamsinstitute.law.ucla.edu/publications/trans-adults-united-states/
- https://williamsinstitute.law.ucla.edu/publications/nonbinary-lgbtq-adults-us/

## Reciprocal consideration and exposure

The ideal source is a consent-based representative survey recording both parties' age acceptance, gender preferences, relationship intent, availability and realistic encounter exposure. Dating-app interactions are selected observations influenced by ranking, platform design and access, not random samples of residents.

## Acquisition checklist

1. Pin dataset version, extraction date and geographic boundary.
2. Obtain age counts in bins compatible with filters, preferably single-year counts.
3. Store question wording and source population for every probability estimate.
4. Model uncertainty from sample design, nonresponse, transport and geography.
5. Document any unresolved cross-tabulation; report bounds or abstain rather than inventing local estimates.

Suggested provenance record: `source_id | title | author | URL/DOI | publication_date | retrieved_at | geography | population | question_wording | weights | uncertainty | limitations | license`.

A 40-mile circle centered on San Diego is not the same as San Diego County. Tract-level approximation, centroid rules, border effects and travel feasibility must be explicitly documented.
