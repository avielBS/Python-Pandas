from tkinter import *
from gui.form_factory import FormFactory


class PrintToText(object):
    def __init__(self, application):
        self.application = application

    def flush(self):
        pass

    def write(self, s):
        self.application.textFrame.insert(END, s)


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        sys.stdout = PrintToText(self)
        self.master = master
        self.pack()
        self.master.title("Movie Ratings Data Analyzer")
        self.formFrame = Frame(master)
        self.formFrame.pack()
        self._textFrame = Text(master)
        self._textFrame.pack()
        self.create_form()

    @property
    def textFrame(self):
        return self._textFrame

    def create_form(self):
        tkvar = StringVar(self)
        tkvar.set('Get info for user')
        self.set_form('Get info for user')
        popupMenu = OptionMenu(self, tkvar, *FormFactory.get_choices(), command=lambda value: (self.textFrame.delete(1.0, END), self.set_form(value)))
        Label(self, text="Choose analysis").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

    def set_form(self, value):
        for widget in self.formFrame.winfo_children():
            widget.destroy()
        form = FormFactory.get_form(value)
        FormFactory.place_labels_and_entries(form, self.formFrame)
        Button(self.formFrame, text='Analyze', command=lambda: (self.textFrame.delete(1.0, END), form.execute())).grid(row=1, column=1)


def start():
    Application(Tk()).mainloop()
