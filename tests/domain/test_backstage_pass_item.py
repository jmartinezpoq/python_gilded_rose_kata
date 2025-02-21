import unittest

from domain.items.backstage_pass import BackstagePassItem


class BackstagePassModelTest(unittest.TestCase):
    def test_backstage_pass_updates_quality(self) -> None:
        item = BackstagePassItem("Backstage passes to a TAFKAL80ETC concert", 15, 1)

        item.update_quality()

        self.assertEqual(2, item.quality)

    def test_backstage_pass_updates_quality_twice_when_sell_in_less_than_10(
        self,
    ) -> None:
        item = BackstagePassItem("Backstage passes to a TAFKAL80ETC concert", 9, 1)

        item.update_quality()

        self.assertEqual(3, item.quality)

    def test_backstage_pass_updates_quality_twice_when_sell_in_less_than_5(
        self,
    ) -> None:
        item = BackstagePassItem("Backstage passes to a TAFKAL80ETC concert", 4, 1)

        item.update_quality()

        self.assertEqual(4, item.quality)

    def test_backstage_pass_updates_quality_to_zero_when_sell_in_zero(self) -> None:
        item = BackstagePassItem("Backstage passes to a TAFKAL80ETC concert", -1, 1)

        item.update_quality()

        self.assertEqual(0, item.quality)


if __name__ == "__main__":
    unittest.main()
