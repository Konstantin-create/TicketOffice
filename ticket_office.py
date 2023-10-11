from modules.randomize_data import *

data = RandomData()
for el in data.generate_routes():
    print(el.train.carriages[0])
