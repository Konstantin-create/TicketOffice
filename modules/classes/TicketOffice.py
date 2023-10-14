import npyscreen


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)
        self.addForm("SECOND", MyForm)


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
                                name="My Table",
                                col_titles=["Column 1", "Column 2", "Column 3"], rely=5)

        data = [
            [str(i), str(i * 2), str(i * 3)] for i in range(100)
        ]
        self.my_grid.values = data
