"""
Route class file
"""

from modules.classes.Train import Train


class Route:
    def __init__(self, number: int = -1, train: Train | None = None, route: list | None = None, time: str = ''):
        self.number = number
        self.train = train
        self.route = route
        self.time = time

    def __repr__(self):
        return f'<Route: {self.number} | {self.train} | {self.time}>'
