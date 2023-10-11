from modules.classes.Train import Train


class Route:
    def __init__(self):
        self.id: int = -1
        self.train: Train | None = None
        self.time: str | None = None  # todo: rewrite on datetime obj

    def __repr__(self):
        return f'<Route: {self.id} | {self.train} | {self.time}>'
