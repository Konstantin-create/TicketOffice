class Train:
    def __init__(self):
        self.carriages: list = []

    def count_min_price(self):
        return min([carriage.price for carriage in self.carriages])

    def count_free_seats(self, carriage_type=None):
        if carriage_type:
            return sum(
                [sum([int(not seat.is_busy) for seat in carriage.seats]) if isinstance(carriage, carriage_type) else 0
                 for carriage in self.carriages])
        return sum([sum([int(not seat.is_busy) for seat in carriage.seats]) for carriage in self.carriages])

    def __repr__(self):
        return f'Train: length - {len(self.carriages)}'
