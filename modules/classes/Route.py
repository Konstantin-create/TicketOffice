"""
Route class file
"""

from modules.classes.Train import Train


class Route:
    def __init__(self, id: int = -1, train: Train | None = None, time: str = ''):
        self.id = id
        self.train = train
        self.time = time  # todo: rewrite on datetime obj

    def __repr__(self):
        return f'<Route: {self.id} | {self.train} | {self.time}>'
