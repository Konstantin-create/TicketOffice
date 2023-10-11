class Carriage:
    def __init__(self):
        self.name: str | None = None
        self.price: int | None = None
        self.max_quantity: int | None = None

    def __repr__(self):
        return f'<Carriage: {self.name} | {self.price} | {self.max_quantity}>'


class SeatCarriage(Carriage):
    def __init__(self):
        super().__init__()
        name = 'сидячий вагон'
        price = 500
        max_quantity = 60


class EconomCarriage(Carriage):
    def __init__(self):
        super().__init__()
        name = 'вагон эконом'
        price = 1000
        max_quantity = 60


class CoupeCarriage(Carriage):
    def __init__(self):
        super().__init__()
        name = 'вагон купе'
        price = 2000
        max_quantity = 20


class FirstClassCarriage(Carriage):
    def __init__(self):
        super().__init__()
        name = 'вагон св'
        price = 5000
        max_quantity = 10


class Seat:
    IS_BUSY: bool = False
