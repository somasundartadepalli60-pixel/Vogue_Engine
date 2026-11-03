"""Regression tests for the dependency-free wardrobe planner."""
import unittest
from vogue_engine.wardrobe.offline_planner import Garment, recommend, score_outfit


class PlannerTests(unittest.TestCase):
    def setUp(self):
        self.items = [Garment("White tee", "top", "white", ("summer",), ("casual",)),
                      Garment("Blue jeans", "bottom", "navy", ("summer",), ("casual",)),
                      Garment("Black sneakers", "shoes", "black", (), ("casual",))]

    def test_recommendation(self):
        results = recommend(self.items, "summer", "casual")
        self.assertEqual(len(results), 1)
        self.assertTrue(0 <= results[0][0] <= 100)

    def test_missing_category(self):
        self.assertEqual(recommend(self.items[:2]), [])

    def test_bad_category(self):
        with self.assertRaises(ValueError):
            Garment("Hat", "accessory", "red"0

    def test_duplicate_category(self):
        with self.assertRaises(ValueError):
            score_outfit((self.items[0], self.items[0], self.items[2]))

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            recommend(self.items, limit=0)

    def test_stable_ranking(self):
        self.assertEqual(recommend(self.items), recommend(self.items))

if __name__ == "__main__":
    unittest.main()
