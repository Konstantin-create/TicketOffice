import npyscreen


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)


class WelcomeForm(npyscreen.Form):
    def create(self):
        center_x = int((self.max_x - len("Текст по центру")) / 2)
        open('out.txt', 'w').write(str([self.max_x, center_x]))
        self.add(npyscreen.FixedText, value="Текст по центру", editable=False, relx=center_x)
        self.add(npyscreen.ButtonPress, name="Закрыть", when_pressed_function=self.close_app, relx=self.max_x - 30,
                 rely=self.max_y - 10)
        self.add(npyscreen.ButtonPress, name="Далее", when_pressed_function=self.dummy_func)

    def dummy_func(self):
        pass

    def close_app(self):
        self.parentApp.switchForm(None)
