import unittest

from domain.item_factory import ItemFactory
from domain.items.aged_brie import AgedBrieItem
from domain.items.backstage_pass import BackstagePassItem
from domain.items.conjured import ConjuredItem
from domain.items.legendary import LegendaryItem
from domain.items.normal import NormalItem


class ItemBuilderTest(unittest.TestCase):
    def test_creates_normal_item(self) -> None:
        item = ItemFactory.build("foo", 1, 1)

        self.assertIsInstance(item, NormalItem)

    def test_creates_aged_brie_item(self) -> None:
        item = ItemFactory.build("Aged Brie", 1, 1)

        self.assertIsInstance(item, AgedBrieItem)

    def test_creates_backstage_pass_item(self) -> None:
        item = ItemFactory.build("Backstage passes to a TAFKAL80ETC concert", 1, 1)

        self.assertIsInstance(item, BackstagePassItem)

    def test_creates_legendary_item(self) -> None:
        item = ItemFactory.build("Sulfuras, Hand of Ragnaros", 1, 1)

        self.assertIsInstance(item, LegendaryItem)

    def test_creates_conjured_item(self) -> None:
        item = ItemFactory.build("Conjured", 1, 1)

        self.assertIsInstance(item, ConjuredItem)


if __name__ == "__main__":
    unittest.main()
