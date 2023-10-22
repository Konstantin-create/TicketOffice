import random

import npyscreen
from modules.randomize_data import RandomData
from modules.classes.Carriages import *

rand_data = RandomData().generate_routes()
global_route_id: int = 0
chosen_ticket = {
    'route': None,
    'carriage': None,
    'seat_num': None
}


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)
        self.addForm("SECOND", ChoseRoute)
        self.addForm("THIRD", ChoseCarriage)
        self.addForm("FOURTH", ConfirmForm)


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

        self.OK_BUTTON_TEXT = 'Далее'
        self.CANCEL_BUTTON_TEXT = 'Закрыть'

    def on_ok(self):
        print('Next page')
        self.parentApp.setNextForm("SECOND")

    def on_cancel(self):
        self.parentApp.setNextForm(None)


class ChoseRoute(npyscreen.Form):

    def create(self):
        self.title = self.add(npyscreen.FixedText, value='Список маршрутов:', editable=False)

        self.my_grid = self.add(npyscreen.GridColTitles,
                                name="Список маршрутов",
                                col_titles=["№", "Отправление", "Свободно мест", "Цена от"], rely=5,
                                max_height=self.max_y - 10,
                                )
        self.get_id = self.add(NumericInput, name="Введите номер маршрута:", value="", editable=True)

        data = []
        for el in rand_data:
            data.append(
                [el.id,
                 el.time,
                 el.train.count_free_seats(),
                 el.train.count_min_price()]
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

        if len(list(filter(lambda x: x.id == global_route_id, rand_data))) == 0:
            npyscreen.notify_confirm(message=f"Произошла ошибка! Такого маршрута не существует, проверьте ввод",
                                     title="Ошибка!")
            self.parentApp.setNextForm('SECOND')
        else:
            self.parentApp.setNextForm('THIRD')


class ChoseCarriage(npyscreen.Form):
    def create(self):
        self.title = self.add(npyscreen.FixedText, value='Выберите тип вагона:', editable=False)
        self.route_id = self.add(npyscreen.FixedText, value=f'Номер отправления: {global_route_id}', editable=False,
                                 rely=5)
        self.route_time = self.add(npyscreen.FixedText, value=f'Время отправления: {None}', editable=False)
        self.route_carriage_title = self.add(npyscreen.FixedText, value='Билеты:', editable=False)
        self.carriage_type1 = self.add(npyscreen.FixedText, editable=False)
        self.carriage_type2 = self.add(npyscreen.FixedText, editable=False)
        self.carriage_type3 = self.add(npyscreen.FixedText, editable=False)
        self.carriage_type4 = self.add(npyscreen.FixedText, editable=False)
        self.id_type = self.add(NumericInput, name="Введите тип вагона:", value="", editable=True, rely=50)

    def beforeEditing(self):
        route = list(filter(lambda x: x.id == global_route_id, rand_data))[0]
        self.route_id.value = f'Номер отправления: {global_route_id}'

        self.route_time.value = f'Время отправления: {route.time}'
        self.carriage_type1.value = f'1 - СИДЯЧИЕ: {route.train.count_free_seats(carriage_type=SeatCarriage)}/{SeatCarriage().max_seats_quantity}'
        self.carriage_type2.value = f'2 - ПЛАЦКАРТ: {route.train.count_free_seats(carriage_type=EconomCarriage)}/{EconomCarriage().max_seats_quantity}'
        self.carriage_type3.value = f'3 - КУПЕ: {route.train.count_free_seats(carriage_type=CoupeCarriage)}/{CoupeCarriage().max_seats_quantity}'
        self.carriage_type4.value = f'4 - СВ: {route.train.count_free_seats(carriage_type=FirstClassCarriage)}/{FirstClassCarriage().max_seats_quantity}'

    def check_input(self):
        value: str = self.id_type.value.strip()
        return value.isdigit()

    def afterEditing(self):
        global global_route_id, chosen_ticket

        route = list(filter(lambda x: x.id == global_route_id, rand_data))[0]
        train = route.train

        if not self.check_input() or int(self.id_type.value.strip()) not in [1, 2, 3, 4]:
            npyscreen.notify_confirm(
                message=f"Произошла ошибка! Тип вагона должен быть числом от 1 до 4, проверьте ввод",
                title="Ошибка!")
            self.parentApp.setNextForm('THIRD')
        else:
            carriage_type = [SeatCarriage, EconomCarriage, CoupeCarriage, FirstClassCarriage][
                int(self.id_type.value.strip()) - 1]

            carriage_bought = train.buy_ticket(carriage_type)
            if train.count_free_seats(carriage_type) == 0 or not carriage_bought:
                npyscreen.notify_confirm(
                    message="Произошла ошибка! Места в этом типе вагонов закончились, выберете другой!",
                    title="Ошибка!")
                self.parentApp.setNextForm('THIRD')
                return

            chosen_ticket = {'route': route, 'carriage': carriage_bought[0], 'seat_num': carriage_bought[1]}
            self.parentApp.setNextForm("FOURTH")


class ConfirmForm(npyscreen.Form):
    def create(self):
        self.title = self.add(npyscreen.FixedText, value='Подтвердите покупку билета:', editable=False)

        self.table = self.add(npyscreen.GridColTitles,
                              col_titles=["№", "МАРШРУТ", "ОТПРАВЛЕНИЕ", "ВАГОН", "МЕСТО", "ЦЕНА"],
                              columns=6,
                              select_whole_line=True,
                              max_height=10,
                              rely=5)

    def beforeEditing(self):
        self.table.values = [
            [
                random.randint(1, chosen_ticket['route'].train.count_free_seats(type(chosen_ticket['carriage']))),
                chosen_ticket['route'].id,
                chosen_ticket['route'].time,
                chosen_ticket['route'].train.carriages.index(chosen_ticket['carriage']) + 1,
                chosen_ticket['seat_num'] + 1,
                chosen_ticket['carriage'].price
            ]
        ]

    def afterEditing(self):
        self.parentApp.setNextForm('MAIN')
