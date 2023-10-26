import configparser


def read_ini():
    config = configparser.ConfigParser()
    config.read('config/Route.ini')
    route_section = {}
    train_section = {}
    schedule_section = {}

    for i in config['Route']:
        route_section[i] = config['Route'][i]

    for i in config['Train']:
        train_section[i] = config['Train'][i]

    for i in config['Shedule']:
        schedule_section[i] = config['Shedule'][i]

    print(route_section)
    print(train_section)
    print(schedule_section)

