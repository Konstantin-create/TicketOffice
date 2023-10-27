import configparser


def read_ini() -> dict:
    config = configparser.ConfigParser()
    config.read('config/Route.ini')
    routes = {

    }

    for i in config['Route']:
        routes[i] = {'route': [int(s) for s in config['Route'][i].split('-')], 'train': None, 'schedule': None}

    for i in config['Train']:
        routes[config['Train'][i]]['train'] = i
        routes[config['Train'][i]]['schedule'] = config['Shedule'][i]

    return routes


def read_stations_conf() -> dict:
    stations = {}

    with open('config/Stations.conf') as file:
        lines = file.readlines()

    for line in lines:
        data = line.split()
        stations[int(data[0])] = data[1]

    return stations


def read_train(train_id) -> dict:
    train = configparser.ConfigParser()
    train.read(f'config/Train{train_id}.ini')

    data = {}

    for carriage_type in train['CountCarriages']:
        data[carriage_type] = {
            'count_carriages': train['CountCarriages'][carriage_type],
            'max_seats': train['CountSeatCarriages'][carriage_type],
            'price': train['PriceCarriages'][carriage_type]
        }
        
    return data
