import npyscreen


class TicketOffice(npyscreen.StandardApp):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)


class WelcomeForm(npyscreen.Form):
    # Конструктор
    def create(self):
        cols, _ = self.useable_space()
        title_widget = self.add(npyscreen.TitleText, name="Добро пожаловать в систему покупки билетов!", rely=1, editable=False)
        # title_widget.relx = int((cols - len(title_widget.value)) / 2)

    # переопределенный метод, срабатывающий при нажатии на кнопку «ok»
    def on_ok(self):
        self.parentApp.

