"""Stovall Coefficient: transparent cell-level calculation, not an empirical model.

Inputs are disjoint adult population cells with already-estimated joint probabilities.
No demographic, identity, or attraction probabilities are inferred by this program.
"""
from __future__ import annotations
import argparse
from dataclasses import dataclass
from datetime import date
from math import isfinite
from typing import Iterable

@dataclass(frozen=True)
class Cell:
    cell_id: str
    age_min: int
    age_max: int
    count: float
    p_mutual: float
    p_encounter_given_mutual: float

    def validate(self) -> None:
        if not self.cell_id or self.age_min < 18 or self.age_max < self.age_min:
            raise ValueError(f"Invalid adult cell: {self.cell_id!r}")
        if not isfinite(self.count) or self.count < 0:
            raise ValueError("count must be finite and nonnegative")
        for name in ("p_mutual", "p_encounter_given_mutual"):
            p = getattr(self, name)
            if not isfinite(p) or not 0 <= p <= 1:
                raise ValueError(f"{name} must be finite and within [0,1]")

@dataclass(frozen=True)
class Result:
    demographic: float
    receptive: float
    encounter_feasible: float
    cells_used: int

    @property
    def per_10000_eligible(self) -> float:
        return 10000 * self.encounter_feasible / self.demographic if self.demographic else 0.0

def age_on(birth_date: date, as_of: date) -> int:
    if birth_date > as_of:
        raise ValueError("Birth date cannot be in the future")
    return as_of.year - birth_date.year - ((as_of.month, as_of.day) < (birth_date.month, birth_date.day))

def calculate(cells: Iterable[Cell], age_filter: tuple[int, int] | None = None) -> Result:
    """Compute D/R/O; cells crossing filter boundaries must be split upstream.

    Each cell must count distinct persons exactly once; overlap cannot be detected
    automatically. A probability is an input, not an estimated output.
    """
    if age_filter is not None:
        lo, hi = age_filter
        if lo < 18 or hi < lo:
            raise ValueError("Invalid adult age filter")
    seen: set[str] = set()
    d = r = o = 0.0
    n = 0
    for c in cells:
        c.validate()
        if c.cell_id in seen:
            raise ValueError(f"Duplicate cell ID: {c.cell_id}")
        seen.add(c.cell_id)
        if age_filter is not None:
            lo, hi = age_filter
            if c.age_max < lo or c.age_min > hi:
                continue
            if c.age_min < lo or c.age_max > hi:
                raise ValueError(f"Cell {c.cell_id} straddles filter; split using observed age counts")
        d += c.count
        r += c.count * c.p_mutual
        o += c.count * c.p_mutual * c.p_encounter_given_mutual
        n += 1
    if not (-1e-9 <= o <= r + 1e-9 <= d + 1e-9):
        raise AssertionError("Population funnel invariants violated")
    return Result(d, r, o, n)

# These values are fabricated and exist ONLY to demonstrate the arithmetic.
SYNTHETIC_CELLS = (
    Cell("synthetic_25_34", 25, 34, 1000, 0.10, 0.40),
    Cell("synthetic_35_44", 35, 44, 1200, 0.16, 0.50),
    Cell("synthetic_45_54", 45, 54, 900, 0.14, 0.45),
    Cell("synthetic_55_58", 55, 58, 400, 0.12, 0.35),
    Cell("synthetic_59_65", 59, 65, 700, 0.11, 0.40),
)

def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--example", action="store_true", help="run fabricated-data demonstration")
    args = parser.parse_args()
    if not args.example:
        parser.error("Only --example is supported; empirical estimation requires sourced inputs")
    result = calculate(SYNTHETIC_CELLS, (25, 58))
    print("SYNTHETIC EXAMPLE ONLY — NOT SAN DIEGO DATA")
    print("Reference age:", age_on(date(1984, 4, 5), date(2026, 10, 12)))
    print("Demographic eligible:", f"{result.demographic:,.0f}")
    print("Expected mutually receptive:", f"{result.receptive:,.2f}")
    print("Expected encounter-feasible:", f"{result.encounter_feasible:,.2f}")
    print("Encounter-feasible per 10,000 eligible:", f"{result.per_10000_eligible:,.2f}")

if __name__ == "__main__":
    main()
