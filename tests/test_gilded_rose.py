# -*- coding: utf-8 -*-
import unittest

from application.gilded_rose import GildedRose
from domain.item import Item


class GildedRoseTest(unittest.TestCase):
    def test_normal_items_updates_quality(self) -> None:
        items = [Item("foo", 1, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)

    def test_normal_items_decrease_sell_in(self) -> None:
        items = [Item("foo", 1, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].sell_in)

    def test_normal_items_quality_decreases_twice_when_sell_in_zero(self) -> None:
        items = [Item("foo", -1, 2)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)

    def test_normal_items_quality_does_not_go_below_zero(self) -> None:
        items = [Item("foo", 1, 0)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("foo", items[0].name)
        self.assertEqual(0, items[0].quality)

    def test_aged_brie_increases_quality(self) -> None:
        items = [Item("Aged Brie", 1, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(2, items[0].quality)

    def test_aged_brie_quality_does_not_go_above_fifty(self) -> None:
        items = [Item("Aged Brie", 1, 50)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Aged Brie", items[0].name)
        self.assertEqual(50, items[0].quality)

    def test_sulfuras_does_not_update_quality(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(80, items[0].quality)

    def test_sulfuras_does_not_update_sell_in(self) -> None:
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
        self.assertEqual(1, items[0].sell_in)

    def test_backstage_pass_updates_quality(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(2, items[0].quality)

    def test_backstage_pass_updates_quality_twice_when_sell_in_less_than_10(
        self,
    ) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(3, items[0].quality)

    def test_backstage_pass_updates_quality_triple_when_sell_in_less_than_5(
        self,
    ) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(4, items[0].quality)

    def test_backstage_pass_updates_quality_to_zero_when_sell_in_zero(self) -> None:
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 1)]

        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()

        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)
        self.assertEqual(0, items[0].quality)


if __name__ == "__main__":
    unittest.main()
