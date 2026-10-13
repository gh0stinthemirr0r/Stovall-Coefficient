# The Stovall Coefficient

## A Gender-Inclusive, Orientation-Aware, Age-Conditioned Framework for Estimating Reciprocal Dating Opportunity

**Methodological research proposal · Version 2.0 · October 12, 2026**  
**Proposed author:** Aaron Stovall (attribution to be confirmed before publication)  
**Status:** Conceptual framework; not peer reviewed; not empirically validated  
**Historical inspiration:** The fictional Wolowitz coefficient from *The Big Bang Theory*

## Abstract

The fictional Wolowitz coefficient, presented in *The Big Bang Theory* as a comic adaptation of the Drake equation, asks how many potential romantic or sexual partners might exist in a local population. The original expression is not scientifically valid. We propose the **Stovall Coefficient (SC)** as a generalizable framework for estimating an adult reference individual's expected local pool of potentially reciprocally interested dating partners. This revision removes assumptions that the reference individual is a heterosexual man or that candidate partners are cisgender women. It models age, gender identity, sexual orientation, expressed partner-gender preferences, relationship intent, relationship availability, and encounter opportunity as conceptually distinct attributes. It supports cisgender, transgender, nonbinary, gender-fluid, and other self-described identities without presuming attraction from identity labels alone. Age preferences are bilateral and age filters optional; adults older than the reference person are never automatically excluded. The proposed estimand uses mutually exclusive population cells or individual-level survey weights to avoid double counting people with overlapping identities. Because fine-grained joint distributions and validated bilateral-preference estimates are not currently assembled for San Diego County, the paper reports no numerical dating-pool estimates. We specify an estimand, measurement plan, uncertainty framework, fairness and privacy safeguards, and validation strategy.

**Keywords:** dating markets; reciprocal choice; gender identity; sexual orientation; nonbinary; transgender; demographic estimation; age preferences; uncertainty; population modeling.

## 1. Historical motivation: from Wolowitz to Stovall

In *The Big Bang Theory*, season 2, episode 20, “The Hofstadter Isotope,” Howard Wolowitz offers a humorous modification of the Drake equation for estimating potential partners within a geographic radius. The dialogue describes a “Wolowitz coefficient” using “neediness times dress size squared.” These factors are fictional, subjective, and not defensible predictors of reciprocal romantic interest. The Stovall Coefficient retains only the motivating question: **how large is the population of adults who might plausibly consider one another for dating, within a specified area and time horizon?** It replaces comic stereotypes with explicitly defined statistical quantities. It is not a measure of any person's worth, desirability, or entitlement to contact.

## 2. Research question and target estimand

Given a consenting adult reference person `r`, geographic boundary `g`, observation time `t`, and optionally specified preferences, estimate the expected number of *distinct adults* in `g` who satisfy reciprocal consideration and feasible opportunity criteria during `t`.

The result is an **expected opportunity-pool size**, not a count of people who consented to date the reference individual. The framework should separately report (a) the demographically eligible pool, (b) the potentially mutually receptive pool, and (c) the encounter-feasible pool. An actual encounter, match, relationship, or sexual activity is not predicted by the coefficient alone.

## 3. Identity and preference model

The reference person and each candidate can, where voluntarily reported, have the following separate attributes:

- **Age:** age in completed years, derived from birth date when available; only adults aged 18+ are in scope.
- **Gender identity:** self-described, potentially multiple labels, including woman, man, nonbinary, gender-fluid, agender, and other identities; a participant may decline to answer.
- **Transgender/cisgender experience:** an optional separate attribute; not a gender category mutually exclusive with woman or man. A trans woman is a woman and a trans man is a man.
- **Sexual orientation:** self-described, potentially including straight, gay, lesbian, bisexual, pansexual, queer, asexual-spectrum, and other terms. An orientation label is **not** substituted for an observed partner-acceptance probability.
- **Partner-gender preferences:** an optional set or graded response indicating which gender identities the individual would consider dating. This is distinct from the person's own identity and orientation.
- **Age preferences:** optional lower/upper bounds and/or an estimated age-acceptance function, permitting both younger and older adult partners.
- **Relationship intent:** optional categories such as long-term, casual, either, undecided, or not currently seeking dates; multiple compatible selections are permitted.
- **Relationship availability:** whether the individual considers themself available for the relevant dating arrangement; marital status alone is insufficient.
- **Encounter context:** realistic distance, accessibility, and opportunity to meet during a defined interval.

Neither transgender status nor nonbinary identity is itself evidence of willingness or unwillingness to date someone. No categorical exclusion or penalty is assigned solely on these identities. The model can represent preferences without endorsing discriminatory treatment or inferring private traits about identifiable people.

## 4. Formal mathematical specification

Let `i` index **distinct adult residents**, `w_i` be an appropriate population survey/calibration weight (or 1 for a fully enumerated population), and `r` denote the reference person. Define:

- `G_i(g,t)` = indicator that person `i` belongs to the geographic and time-defined population;
- `F_i(r)` = optional user-selected adult-age and other explicit eligibility filter, equal to 1 when disabled;
- `U_i` = indicator or probability of relationship availability;
- `D_i(k)` = indicator or probability of actively seeking a compatible relationship-intent category `k`;
- `B(r,i)` = probability that both parties would consider the other's stated gender identity and age, conditional on their preferences;
- `H(r,i,t)` = probability of feasible contact within the specified horizon;
- `C(r,i,k)` = conditional probability that relationship intentions and any additional explicitly selected constraints are compatible.

The conceptual estimand is

\[
\mathrm{SC}(r,g,t,k,F)=\sum_{i\in\mathcal{P}_{18+}}w_i\,G_i(g,t)F_i(r)\,\Pr\!\left(U_i\cap D_i(k)\cap B(r,i)\cap H(r,i,t)\cap C(r,i,k)\mid X_i,X_r,g,t\right).
\]

Here `X_i` and `X_r` contain the relevant, voluntarily reported covariates. **The joint conditional probability is the primary definition.** The individual factors must not be multiplied as though statistically independent. A factorized implementation is permissible only as a documented chain of conditional probabilities (or a calibrated joint predictive model). This avoids systematic bias from correlations between age, gender, orientation, partnership, and dating intent.

When only grouped demographic data are available, replace the individual sum with a sum over **mutually exclusive cells** `c`, each with a population count `N_c` and an estimated joint probability `p_c`:

\[
\widehat{\mathrm{SC}}=\sum_{c\in\mathcal C}N_c\,F_c\,\widehat p_c.
\]

Cell partitions must count each person once. For example, “women,” “transgender people,” and “nonbinary people” must **not** be naively added as separate totals because these categories can overlap. Multi-label identity can be represented in covariates without summing overlapping marginal populations. When data do not support a unique cross-classification, report partial identification bounds or explicitly labeled scenarios rather than fabricated precise estimates.

### 4.1 Reciprocal age acceptance

Let `a_r` be the reference person's age and `a_i` a candidate's age. Define `A_{i→r}(a_r,a_i)` and `A_{r→i}(a_i,a_r)` as the two age-consideration components. Both are evaluated, but neither is assumed to be symmetric or independent. A candidate older than the reference person is eligible by default, as is a younger adult candidate. The reference person's preferred age range is an **optional filter applied to output**, not a biological rule.

### 4.2 Reciprocal gender and orientation compatibility

Define a dyadic preference function `Q(r,i)` from the two individuals' *expressed partner preferences*, not from a fixed matrix mapping labels to supposedly inevitable attractions. For example, a bisexual person may consider multiple genders, a straight trans woman may seek men, and a nonbinary person may describe preferences in terms not captured by binary gender categories. When preference information is absent, `Q` is **unknown**, not zero. Statistical imputation must preserve this uncertainty and disclose its assumptions.

### 4.3 Intent and optional filters

Relationship-intent filtering defaults to **unrestricted**, meaning the model does not exclude someone for preferring long-term or casual dating. A user may request long-term, casual, either, or other clearly defined intent compatibility. A filter may change the eligible pool; it should not silently rewrite the reference person's identity or the candidate's preferences.

## 5. San Diego County illustrative configuration

The original illustrative case is retained as one configuration rather than the universal model:

| Parameter | Illustrative setting |
|---|---|
| Geography | San Diego County, California |
| Reference age | 42 as of October 12, 2026 (birth date April 5, 1984) |
| Reference gender | Optional, self-described; not inferred from name or age |
| Candidate genders | Women, men, nonbinary and other self-described genders; selectable or unrestricted |
| Preferred candidate age | 25–58 (optional) |
| Dating older adults | Included, through age 58 in this example |
| Relationship intent | Unrestricted by default |
| Reference orientation / partner preference | Voluntarily supplied; unknown otherwise |
| Empirical SC estimate | **Not yet estimable from the assembled evidence** |

Other configurations can represent a woman seeking women, a man seeking men, a trans person seeking any chosen genders, a nonbinary person seeking partners of any gender, or a person open to all genders. Gender is not inferred from the reference person's name, appearance, or prior examples.

## 6. Data sources and measurement strategy

**Demography:** Use U.S. Census Bureau American Community Survey (ACS) age and geographic population data as the principal baseline. The ACS does **not** directly measure gender identity and sexual orientation, so its binary sex categories cannot simply be relabeled as comprehensive gender-identity counts [1].

**Gender identity and sexual orientation:** Consult specialized probability surveys and research, including the Williams Institute's 2025 transgender population estimates and research on nonbinary adults [2,3]. These are not interchangeable with San Diego County age-by-gender-by-orientation joint counts. National or state estimates must be transported to a local population only with documented assumptions, uncertainty, and appropriate calibration.

**Dating and relationship intent:** Pew Research Center's surveys of single adults provide evidence on dating interest and relationship intentions, but published aggregates may be too coarse for particular gender and orientation intersections [4,5]. Do not apply a national all-women or all-men dating-interest percentage to transgender, nonbinary, or other subgroups without evidence.

**Reciprocity:** The ideal source is a representative, voluntary, privacy-preserving survey that directly asks about age acceptance, partner-gender preferences, relationship intent, and dating availability. Observed opt-in interaction data may help calibrate a model but are subject to selection, platform, and exposure biases. An orientation label alone is never proof of interest in a particular person.

**Missingness:** Include “prefer not to say,” missing, and uncertain categories. Use sensitivity analysis or multiple imputation only when assumptions are defensible. Do not treat nonresponse as heterosexual, cisgender, or uninterested by default.

## 7. Statistical estimation and uncertainty

1. Specify the geographic boundary, observation horizon, reference profile, target age range, and optional filters before estimation.
2. Obtain age-specific adult population totals and reconcile overlapping identity classifications.
3. Estimate joint or sequential *conditional* probabilities of availability, dating intent, reciprocal age and gender consideration, and encounter feasibility.
4. Where direct joint observations are unavailable, construct transparently labeled scenarios and partial-identification bounds; do not claim a measured local coefficient.
5. Propagate demographic sampling error, survey weights, parameter uncertainty, and transportability uncertainty using posterior simulation or design-based bootstrap as appropriate. A Monte Carlo sample size such as 10,000 draws is a computational setting, not a substitute for evidence.
6. Report median or mean estimates, uncertainty intervals, effective sample sizes, model assumptions, and a breakdown by age band and selected partner-gender category when disclosure-safe.
7. Provide a normalized opportunity index per 10,000 adults **alongside**, not instead of, the absolute estimated pool; specify the normalization denominator.

A nominal 95% simulation interval is not a frequentist confidence interval unless its construction supports that interpretation. Avoid spurious precision.

## 8. Validation and fairness evaluation

Prospective validation would compare predictions with voluntarily observed aggregate reciprocal consideration or match outcomes in a defined sampling frame, using held-out geographic regions or time periods. Assess calibration, interval coverage, selection bias, and sensitivity to encounter-channel exposure. Evaluate errors by age, gender identity, and orientation only when subgroup sample sizes permit meaningful analysis. Publish no small-cell counts that risk reidentification. Differences in model outputs must be explained by observed or transparently modeled population/preference factors, not unsupported identity-based penalties.

The model must be auditable: record dataset versions, survey question wording, population definitions, code version, filter selections, and uncertainty assumptions. Do not claim that a favorable coefficient implies an individual's consent or willingness to be contacted.

## 9. Limitations and ethical considerations

The main limitation is lack of high-resolution, representative joint data on age, gender identity, orientation, partnership, dating intent, bilateral acceptance, and encounter opportunity. Sexual orientation and gender identity are not interchangeable; neither determines an individual's preferences with certainty. Survey classifications and identities evolve. Many data sources exclude or inadequately represent smaller groups. A fully general model therefore needs user-defined identities and partner-preference inputs, calibrated local evidence, and explicit unknowns. No output should rank the worth or attractiveness of protected identity groups. Do not collect identifiable sexual orientation or transgender status without informed consent, a clear purpose, security controls, and a defensible retention policy.

## 10. Conclusion

The Stovall Coefficient generalizes the Wolowitz thought experiment into a proposed **gender-inclusive, orientation-aware, reciprocal adult dating opportunity estimator**. Its distinctive feature is not an assumed universal formula for attraction, but a transparent estimand combining unique population counts with conditional dyadic preferences, optional age and relationship-intent filters, geographic reach, and quantified uncertainty. The model explicitly allows older and younger adult partners and accommodates overlapping gender identities without double counting. Empirical validation remains necessary before the coefficient can be described as a predictive scientific instrument.

## References

1. Census Reporter. *Sexual Orientation and Gender Identity*. https://censusreporter.org/topics/sexual-orientation-gender-identity/ (accessed October 12, 2026).
2. Williams Institute, UCLA School of Law. (2025). *How Many Adults and Youth Identify as Transgender in the United States?* https://williamsinstitute.law.ucla.edu/publications/trans-adults-united-states/
3. Wilson, B. D. M., & Meyer, I. H. (2021). *Nonbinary LGBTQ Adults in the United States*. Williams Institute. https://williamsinstitute.law.ucla.edu/publications/nonbinary-lgbtq-adults-us/
4. Brown, A. (2020). *A profile of single Americans*. Pew Research Center. https://www.pewresearch.org/social-trends/2020/08/20/a-profile-of-single-americans/
5. Pew Research Center. (2023). *5 facts about single Americans for Valentine's Day*. https://www.pewresearch.org/short-reads/2023/02/08/for-valentines-day-5-facts-about-single-americans/
6. *The Big Bang Theory*. (2009). Season 2, episode 20, “The Hofstadter Isotope.” Historical fictional reference; not empirical evidence.

## Citation and reuse

Suggested citation: Stovall, A. (2026). *The Stovall Coefficient: A Gender-Inclusive, Orientation-Aware, Age-Conditioned Framework for Estimating Reciprocal Dating Opportunity* (Version 2.0, methodological research proposal). GitHub repository manuscript, publication location pending.

**Publication note:** Before external submission, verify all bibliographic metadata, select a license, archive a versioned release, provide reproducible code and data provenance, and distinguish the proposal from peer-reviewed empirical research.
