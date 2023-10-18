import npyscreen
from modules.randomize_data import RandomData

rand_data = RandomData().generate_routes()


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)
        self.addForm("SECOND", MyForm)


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


class MyForm(npyscreen.Form):
    def afterEditing(self):
        self.parentApp.setNextForm(None)

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
