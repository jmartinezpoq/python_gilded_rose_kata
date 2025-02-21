import unittest

from domain.items.aged_brie import AgedBrieItem


class AgedBrieModelTest(unittest.TestCase):
    def test_aged_brie_updates_quality_by_increasing(self) -> None:
        item = AgedBrieItem("Aged Brie", 1, 1)

        item.update_quality()

        self.assertEqual(2, item.quality)


if __name__ == "__main__":
    unittest.main()
