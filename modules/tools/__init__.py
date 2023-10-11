def count_free_seats(seats: list) -> int:
    return sum([1 for seat in seats if not seat.is_busy])
