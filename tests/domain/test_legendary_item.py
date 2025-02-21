import unittest

from domain.items.legendary import LegendaryItem


class LegendaryItemTest(unittest.TestCase):
    def test_legendary_item_does_not_update_quality(self) -> None:
        item = LegendaryItem("Sulfuras, Hand of Ragnaros", 1, 80)

        item.update_quality()

        self.assertEqual(80, item.quality)

    def test_legendary_item_does_not_update_sell_in(self) -> None:
        item = LegendaryItem("Sulfuras, Hand of Ragnaros", 1, 80)

        item.decrease_sell_in()

        self.assertEqual(1, item.sell_in)


if __name__ == "__main__":
    unittest.main()
