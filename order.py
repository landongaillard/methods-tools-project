class Order:
    def __init__(self, orderID: str, dateOrdered: int, shippingDate: str, total: float, shippingAddress: str) -> None:
        self.__orderID: str = orderID
        self.__dateOrdered: int = dateOrdered
        self.__shippingDate: str = shippingDate
        self.__total: float = total
        self.__shippingAddress: str = shippingAddress

    def cancelOrder(self) -> None:
        pass

    # we may not need this due to us not having to keep track of
    # order history anymore
    def viewOrder(self) -> None:
        pass

