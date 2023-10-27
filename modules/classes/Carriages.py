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

    def get_carriage_type_by_str(self, carriage_name):
        if carriage_name == 'seatcarriage': return SeatCarriage
        if carriage_name == 'economcarriage': return EconomCarriage
        if carriage_name == 'coupecarriage': return CoupeCarriage
        if carriage_name == 'firstclasscarriage': return FirstClassCarriage

    def __repr__(self):
        return f'<Carriage: {self.name} | {self.price} | {count_free_seats(self.seats)}/{self.max_seats_quantity}>'


class SeatCarriage(Carriage):
    def __init__(self, price: int = 500, max_seats: int = 60, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'сидячий вагон'
        self.price = price
        self.max_seats_quantity = max_seats
        self.seats = seats


class EconomCarriage(Carriage):
    def __init__(self, price: int = 1000, max_seats: int = 30, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон эконом'
        self.price = price
        self.max_seats_quantity = max_seats
        self.seats = seats


class CoupeCarriage(Carriage):
    def __init__(self, price: int = 2000, max_seats: int = 20, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон купе'
        self.price = price
        self.max_seats_quantity = max_seats
        self.seats = seats


class FirstClassCarriage(Carriage):
    def __init__(self, price: int = 5000, max_seats: int = 10, seats: list = None):
        super().__init__()
        if seats is None:
            seats = []

        self.name = 'вагон св'
        self.price = price
        self.max_seats_quantity = max_seats
        self.seats = seats


class Seat:
    def __init__(self, id: int = -1, is_busy: bool = False):
        self.id = id
        self.is_busy = is_busy

    def __repr__(self):
        return f'<Seat: {self.id} | busy? - {self.is_busy}>'
