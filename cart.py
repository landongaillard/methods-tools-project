from inventory import Inventory


class Cart:
    def __init__(self, promocode: bool) -> None:
        self.__promocode: bool = promocode
        self.__items: list[Inventory] = []

    def addItem(self, item: Inventory) -> None:
        pass

    def removeItem(self, item: Inventory) -> None:
        pass
    