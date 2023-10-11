class Carriage:
    def __init__(self, name: str = None, price: int = -1, max_seats_quantity: int = -1, seats=None):
        if seats is None:
            seats = []

        self.name = name
        self.price = price
        self.max_seats_quantity = max_seats_quantity
        self.seats = seats

    def __repr__(self):
        return f'<Carriage: {self.name} | {self.price} | {self.max_seats_quantity}>'


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
    def __init__(self, id: int = -1, is_busy: bool = False):
        self.id = id
        self.is_busy = is_busy
