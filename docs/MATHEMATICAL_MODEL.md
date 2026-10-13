# Mathematical model

## Target population and unit

Let `r` be an adult reference person, `g` a specified geographic boundary, `t` a time horizon, and `i` a **distinct adult** candidate. Let `w_i` be a population expansion weight and `F_i` an optional filter, equal to one if no preference filter is enabled.

Define `U` as availability, `I` as relationship-intent compatibility, `B` as bilateral consideration based on voluntarily expressed age/gender preferences, and `H` as feasible encounter opportunity. Then:

$$SC(r,g,t,F)=\sum_i w_iF_iP(U_i\cap I_{ri}\cap B_{ri}\cap H_{ri}\mid X_i,X_r,g,t).$$

This is the expected number of distinct adults meeting a **defined joint event**, not a forecast of dates or sexual encounters. The probability is not a claim that any individual consents to contact.

## Three distinct outputs

1. **Demographic eligible pool D:** $\sum_i w_iF_i$.
2. **Mutually receptive pool R:** $\sum_i w_iF_iP(U_i\cap I_{ri}\cap B_{ri}\mid X)$.
3. **Encounter-feasible pool O:** $\sum_i w_iF_iP(U_i\cap I_{ri}\cap B_{ri}\cap H_{ri}\mid X)$.

A coherent model must satisfy $0\le O\le R\le D$. These nested results should never be merged into a single ambiguous number.

## Correct conditional factorization

The chain rule permits

$$P(U,I,B,H\mid X)=P(U\mid X)P(I\mid U,X)P(B\mid I,U,X)P(H\mid B,I,U,X).$$

Simply multiplying independent published percentages is unjustified: availability, age, intent, geography, gender and encounter exposure are correlated. The preferred model estimates the joint event directly or its *conditional* components.

## Age and reciprocity

The reference age $a_r$ and candidate age $a_i$ enter two potentially different acceptance functions: $A_{r\to i}(a_i)$ and $A_{i\to r}(a_r)$. Neither is assumed symmetric or known from age alone. Adults older than the reference person are eligible by default; adults younger than the reference person are eligible if at least 18. A user-specified interval $[L,U]$ is an **optional output filter**, not a scientific age law.

## Gender and orientation

Bilateral consideration uses expressed partner preferences, not deterministic identity-to-attraction lookup tables. Trans women are women; trans men are men; nonbinary and multi-label identities require careful, non-overlapping person-level counting. Missing preferences mean unknown, not zero. Population cells must partition unique persons, not sum overlapping identity totals.

## Grouped data and partial identification

With disjoint cells $c$, counts $N_c$, and estimated joint event probabilities $p_c$, $\widehat{SC}=\sum_cN_cp_c$. If only $p_c\in[l_c,u_c]$ is defensible, report bounds $\sum_cN_cl_c\le SC\le\sum_cN_cu_c$, subject to joint constraints. When cell age bands cross the user's filter boundary, obtain finer counts; never silently assume a uniform within-bin distribution.

## Comparison across cities

A normalized indicator $SC_{10k}=10{,}000\times SC/D$ can complement, but never replace, the absolute pool. State the denominator, horizon, source vintage and filtering choices. It is not a percentile of human desirability.
