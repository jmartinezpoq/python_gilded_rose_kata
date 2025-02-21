import unittest

from domain.items.conjured import ConjuredItem


class MyTestCase(unittest.TestCase):
    def test_conjured_item_updates_quality_twice(self) -> None:
        item = ConjuredItem("Conjured item", 1, 2)

        item.update_quality()

        self.assertEqual(0, item.quality)


if __name__ == "__main__":
    unittest.main()
