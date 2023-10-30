"""
Graphic classes and functions
"""

import npyscreen
from modules.tools.load_data import *
from modules.tools.file_reader import read_stations_conf

static_data = DataLoader().load()
stations_data = read_stations_conf()


def get_paths(route_obj) -> list:
    route = []
    for i in route_obj.route:
        route.append(stations_data[i])

    return route


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)
        self.addForm("SECOND", ChoseRoute)


class NumericInput(npyscreen.TitleText):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.value = ""

    def translate_key(self, inp):
        if inp in "0123456789" or inp == "KEY_BACKSPACE" or inp == "KEY_DELETE":
            return inp
        else:
            return None


class WelcomeForm(npyscreen.ActionForm):
    def create(self):
        center_x = int((self.max_x - len('Добро пожаловать в единую систему покупки билетов!')) / 2)
        self.add(npyscreen.FixedText, value='Добро пожаловать в единую систему покупки билетов', editable=False,
                 relx=center_x)
        self.add(npyscreen.FixedText, value='1 - Выберите номер маршрута', editable=False, relx=20, rely=20)
        self.add(npyscreen.FixedText, value='2 - Выберите тип билета', editable=False, relx=20)
        self.add(npyscreen.FixedText, value='ВНИМАНИЕ: таблицы можно скролить <page_up/page_down>', color="IMPORTANT",
                 relx=20, editable=False)
        self.add(npyscreen.FixedText, value='ВНИМАНИЕ: Во избежание проблем запускать в полноэкранном режиме',
                 color="IMPORTANT",
                 relx=20, editable=False)

        self.OK_BUTTON_TEXT = 'Далее'
        self.CANCEL_BUTTON_TEXT = 'Закрыть'

    def on_ok(self):
        self.parentApp.setNextForm("SECOND")

    def on_cancel(self):
        self.parentApp.setNextForm(None)


class ChoseRoute(npyscreen.Form):
    def create(self):
        self.title = self.add(npyscreen.FixedText,
                              value='Список маршрутов(для перехода к списку маршрутов и обратно - page left/right):',
                              editable=False)

        self.my_grid = self.add(npyscreen.GridColTitles,
                                name="Список маршрутов",
                                col_titles=["№", "Отправление", "Свободно мест", "Цена от", "Маршрут"], rely=5,
                                max_height=self.max_y - 10)
        self.get_id = self.add(NumericInput, name="Введите номер маршрута:", value="", editable=True)

        data = []
        for el in static_data:
            data.append(
                [el.train.number,
                 el.time,
                 el.train.count_free_seats(),
                 el.train.count_min_price(),
                 ' '.join(get_paths(el))]
            )
            self.my_grid.values = data

        def check_input(self):
            value: str = self.get_id.value.strip()
            return value.isdigit()

        def afterEditing(self):
            global global_route_id
            if not self.check_input():
                npyscreen.notify_confirm(message=f"Произошла ошибка! Номер маршрута должен быть числом, проверьте ввод",
                                         title="Ошибка!")
                self.parentApp.setNextForm('SECOND')
            else:
                global_route_id = int(self.get_id.value.strip())

            if len(list(filter(lambda x: x.id == global_route_id, static_data))) == 0:
                npyscreen.notify_confirm(message=f"Произошла ошибка! Такого маршрута не существует, проверьте ввод",
                                         title="Ошибка!")
                self.parentApp.setNextForm('SECOND')
            else:
                self.parentApp.setNextForm('THIRD')
