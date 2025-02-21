from domain.items.base import Item


class LegendaryItem(Item):
    MAX_QUALITY = 80

    def update_quality(self) -> None:
        self.quality = self.MAX_QUALITY

    def decrease_sell_in(self) -> None:
        pass
