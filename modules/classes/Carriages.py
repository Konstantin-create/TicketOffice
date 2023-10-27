"""
Carriages and seat classes
"""

from modules.tools.seats_manager import count_free_seats


class Carriage:
    def __init__(self, name: str = None, price: int = -1, max_seats_quantity: int = -1, seats=None):
        if seats is None:
            seats = []

        self.name = name
        self.price = price
        self.max_seats_quantity = max_seats_quantity
        self.seats = seats

    def __repr__(self):
        return f'<Carriage: {self.name} | {self.price} | {count_free_seats(self.seats)}/{self.max_seats_quantity}>'


class SeatCarriage(Carriage):
    def __init__(self, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'сидячий вагон'
        self.price = 500
        self.max_seats_quantity = 60
        self.seats = seats


class EconomCarriage(Carriage):
    def __init__(self, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон эконом'
        self.price = 1000
        self.max_seats_quantity = 60
        self.seats = seats


class CoupeCarriage(Carriage):
    def __init__(self, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон купе'
        self.price = 2000
        self.max_seats_quantity = 20
        self.seats = seats


class FirstClassCarriage(Carriage):
    def __init__(self, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон св'
        self.price = 5000
        self.max_seats_quantity = 10
        self.seats = seats


class Seat:
    def __init__(self, id: int = -1, is_busy: bool = False):
        self.id = id
        self.is_busy = is_busy

    def __repr__(self):
        return f'<Seat: {self.id} | busy? - {self.is_busy}>'
