class Train:
    def __init__(self):
        self.carriages: list = []

    def __repr__(self):
        return f'Train: {len(self.carriages)}'
