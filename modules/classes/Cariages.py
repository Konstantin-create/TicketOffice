class Carriage:
    def __init__(self):
        self.name: str | None = None
        self.price: int | None = None
        self.quantity: int | None = None


class SeatCarriage(Carriage):
    pass


class EconomCarriage(Carriage):
    pass


class CoupeCarriage(Carriage):
    pass


class FirstClassCarriage(Carriage):
    pass


class Seat:
    IS_BUSY: bool = False
