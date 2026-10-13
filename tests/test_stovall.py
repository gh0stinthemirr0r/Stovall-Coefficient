import sys
import unittest
from datetime import date
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'src'))
from stovall import Cell, calculate, age_on, SYNTHETIC_CELLS

class TestStovall(unittest.TestCase):
    def test_reference_age(self):
        self.assertEqual(age_on(date(1984, 4, 5), date(2026, 10, 12)), 42)
        self.assertEqual(age_on(date(1984, 4, 5), date(2027, 4, 5)), 43)
    def test_funnel(self):
        r = calculate(SYNTHETIC_CELLS, (25, 58))
        self.assertEqual(r.demographic, 3500)
        self.assertAlmostEqual(r.receptive, 466)
        self.assertAlmostEqual(r.encounter_feasible, 209.5)
        self.assertTrue(0 <= r.encounter_feasible <= r.receptive <= r.demographic)
    def test_older_adults_included(self):
        r = calculate([Cell('older', 55, 58, 400, .12, .35)], (25, 58))
        self.assertGreater(r.encounter_feasible, 0)
    def test_partial_cell_rejected(self):
        with self.assertRaises(ValueError):
            calculate([Cell('a', 20, 30, 100, .2, .3)], (25, 58))
    def test_duplicate_rejected(self):
        c = Cell('a', 25, 30, 100, .2, .3)
        with self.assertRaises(ValueError):
            calculate([c,c])
    def test_bad_probability_rejected(self):
        with self.assertRaises(ValueError):
            calculate([Cell('a', 25, 30, 100, 1.2, .3)])
    def test_unfiltered_includes_older(self):
        self.assertEqual(calculate(SYNTHETIC_CELLS).demographic, 4200)

if __name__ == '__main__':
    unittest.main()
