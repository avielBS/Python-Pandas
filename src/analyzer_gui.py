import sys
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer()


class Application(Frame):
    labels = {
        'Get info for user',
        'Get average age of raters for movie',
        'List rated movies',
        'Get users\' rating average',
        'Get user\'s movie count',
        'Get rating of user for movie',
        'Get average ratings',
        'Get rating of movie',
        'Get highest rated movies',
        'Get lowest rated movies',
        'Compare two movies by titles'
    }

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.master.title("Data Analyzer")
        self.formFrame = Frame(master)
        self.formFrame.pack()
        self.create_buttons()

    def set_form(self, value):
        for widget in self.formFrame.winfo_children():
            widget.destroy()
        parameters = {
            'Get info for user': {
                'User ID': IntVar()
            },
            'Get average age of raters for movie': {
                'Title': StringVar()
            },
            'List rated movies': {
                'User ID': IntVar(),
                'Head': IntVar(),
                'Graphic Results': BooleanVar()
            },
            'Get users\' rating average': {
                'User ID': IntVar()
            },
            'Get user\'s movie count': {
                'User ID': IntVar()
            },
            'Get rating of user for movie': {
                'User ID': IntVar(),
                'Title': StringVar()
            },
            'Get average ratings': {
                'Head': IntVar(),
                'Sort': StringVar(),
                'Begin': DoubleVar(),
                'End': DoubleVar(),
                'Graphic Results': BooleanVar()
            },
            'Get rating of movie': {
                'Title': StringVar()
            },
            'Get highest rated movies': {
                'Head': IntVar(),
                'Graphic Results': BooleanVar()
            },
            'Get lowest rated movies': {
                'Head': IntVar(),
                'Graphic Results': BooleanVar()
            },
            'Compare two movies by titles': {
                'Title One': StringVar(),
                'Title Two': StringVar(),
                'Graphic Results': BooleanVar()
            }
        }
        commands = {
            'Get info for user': lambda: print(data_analyzer.get_info_for(
                parameters['Get info for user']['User ID'].get()
            )),
            'Get average age of raters for movie': lambda: print(data_analyzer.get_raters_avg_age(
                parameters['Get average age of raters for movie']['Title'].get()
            )),
            'List rated movies': lambda: print(data_analyzer.get_users_rated_movies(
                parameters['List rated movies']['User ID'].get(),
                parameters['List rated movies']['Head'].get(),
                parameters['List rated movies']['Graphic Results'].get()
            )),
            'Get users\' rating average': lambda: print(data_analyzer.get_user_rating_average(
                parameters['Get users\' rating average']['User ID'].get()
            )),
            'Get user\'s movie count': lambda: print(data_analyzer.get_user_movies_count(
                parameters['Get user\'s movie count']['User ID'].get()
            )),
            'Get rating of user for movie': lambda: print(data_analyzer.get_user_ratings_for(
                parameters['Get rating of user for movie']['User ID'].get(),
                parameters['Get rating of user for movie']['Title'].get()
            )),
            'Get average ratings': lambda: print(data_analyzer.get_average_ratings(
                parameters['Get average ratings']['Head'].get(),
                parameters['Get average ratings']['Sort'].get(),
                parameters['Get average ratings']['Begin'].get(),
                parameters['Get average ratings']['End'].get(),
                parameters['Get average ratings']['Graphic Results'].get()
            )),
            'Get rating of movie': lambda: print(data_analyzer.get_rating_of(
                parameters['Get rating of movie']['Title'].get()
            )),
            'Get highest rated movies': lambda: print(data_analyzer.get_highest_rated_movies(
                parameters['Get highest rated movies']['Head'].get(),
                parameters['Get highest rated movies']['Graphic Results'].get()
            )),
            'Get lowest rated movies': lambda: print(data_analyzer.get_lowest_rated_movies(
                parameters['Get lowest rated movies']['Head'].get(),
                parameters['Get lowest rated movies']['Graphic Results'].get()
            )),
            'Compare two movies by titles': lambda: print(data_analyzer.compare_two_movies_by_title(
                parameters['Compare two movies by titles']['Title One'].get(),
                parameters['Compare two movies by titles']['Title Two'].get(),
                parameters['Compare two movies by titles']['Graphic Results'].get()
            ))
        }
        command = commands.get(value)
        params = parameters.get(value)
        for index, param in enumerate(params):
            Label(self.formFrame, text=param).grid(row=0, column=index * 2)
            Entry(self.formFrame, textvariable=params[param]).grid(row=0, column=index * 2 + 1)
        Button(self.formFrame, text='Analyze', command=lambda: Application.execute_command(command)) \
            .grid(row=1, column=int(round(len(params.keys()) / 2)) + 1)

    @staticmethod
    def execute_command(command):
        textFrame.delete(1.0, END)
        command()

    def create_buttons(self):
        tkvar = StringVar(self)
        tkvar.set('Get info for user')  # set the default option
        self.set_form('Get info for user')
        popupMenu = OptionMenu(self, tkvar, *Application.labels, command=self.change_dropdown)
        Label(self, text="Choose analysis").grid(row=1, column=1)
        popupMenu.grid(row=2, column=1)

    def change_dropdown(self, value):
        textFrame.delete(1.0, END)
        self.set_form(value)


root = Tk()
app = Application(master=root)
textFrame = Text(root)
textFrame.pack()


class PrintToText(object):
    def flush(self):
        pass

    def write(self, s):
        textFrame.insert(END, s)


sys.stdout = PrintToText()


def start():
    app.mainloop()
