class Train:
    def __init__(self):
        self.carriages: list = []

    def count_min_price(self) -> int:
        return min([carriage.price for carriage in self.carriages])

    def count_free_seats(self, carriage_type=None) -> int:
        if carriage_type:
            return sum(
                [sum([int(not seat.is_busy) for seat in carriage.seats]) if isinstance(carriage, carriage_type) else 0
                 for carriage in self.carriages])
        return sum([sum([int(not seat.is_busy) for seat in carriage.seats]) for carriage in self.carriages])

    def buy_ticket(self, carriage_type=None):
        carriages_of_this_type = [carriage for carriage in self.carriages if isinstance(carriage, carriage_type)]

        for carriage in carriages_of_this_type:
            for i in range(len(carriage.seats)):
                if not carriage.seats[i].is_busy:
                    carriage.seats[i].is_busy = True
                    return [carriage, i]
        return None

    def __repr__(self):
        return f'Train: length - {len(self.carriages)}'
