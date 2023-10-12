import npyscreen


class TicketOffice(npyscreen.NPSAppManaged):
    def onStart(self):
        self.addForm("MAIN", WelcomeForm)


class WelcomeForm(npyscreen.ActionForm):
    def create(self):
        center_x = int((self.max_x - len("Текст по центру")) / 2)
        open('out.txt', 'w').write(str([self.max_x, center_x]))
        self.add(npyscreen.FixedText, value="Текст по центру", editable=False, relx=center_x)
        self.OK_BUTTON_TEXT = 'Далее'
        self.CANCEL_BUTTON_TEXT = 'Закрыть'

    def on_ok(self):
        print('Next page')
        self.parentApp.setNextForm(None)

    def on_cancel(self):
        self.parentApp.setNextForm(None)
