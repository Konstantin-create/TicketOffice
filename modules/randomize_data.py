import random
from config import Config
from modules.classes import *


class RandomData:
    def __init__(self):
        pass

    def generate_routes(self) -> list:
        routes = []
        carriages_types = random.choice([SeatCarriage, EconomCarriage, CoupeCarriage, FirstClassCarriage])

        for i in range(random.randint(Config.TRAIN_PER_ROUTE_MIN_QUANTITY, Config.TRAIN_PER_ROUTE_MAX_QUANTITY)):
            routes.append(
                Route(
                    id=random.randint(1000, 9999),
                    train=Train(),
                    time=f'{random.randint(0, 23):02}:{random.randint(0, 59)}'
                )
            )

        return routes
