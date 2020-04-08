import sys
from tkinter import *
from data_analyzer import DataAnalyzer
from gui.form_factory import FormFactory


class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Data Analyzer")
        self.formFrame = Frame(master)
        self.formFrame.pack()
        self.create_form()

    def set_form(self, value):
        for widget in self.formFrame.winfo_children():
            widget.destroy()
        form = FormFactory.get_form(value)
        FormFactory.place_labels_and_entries(form.labels, self.formFrame)
        Button(self.formFrame, text='Analyze', command=form.get_command()).grid(row=1, column=1)

    @staticmethod
    def execute_command(command):
        textFrame.delete(1.0, END)
        command()

    def create_form(self):
        tkvar = StringVar(self)
        tkvar.set('Get info for user')
        self.set_form('Get info for user')
        popupMenu = OptionMenu(self, tkvar, *FormFactory.get_choices(), command=self.change_dropdown)
        Label(self, text="Choose analysis").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

    def change_dropdown(self, value):
        textFrame.delete(1.0, END)
        self.set_form(value)


class PrintToText(object):
    def flush(self):
        pass

    def write(self, s):
        textFrame.insert(END, s)


root = Tk()
app = Application(master=root)
textFrame = Text(root)
textFrame.pack()
sys.stdout = PrintToText()


def start():
    app.mainloop()