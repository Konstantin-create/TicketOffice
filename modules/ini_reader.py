import configparser


def read_ini() -> dict:
    config = configparser.ConfigParser()
    config.read('config/Route.ini')
    routes = {

    }

    for i in config['Route']:
        routes[i] = {'route': config['Route'][i], 'train': None, 'schedule': None}

    for i in config['Train']:
        routes[config['Train'][i]]['train'] = i
        routes[config['Train'][i]]['schedule'] = config['Shedule'][i]

    return routes
