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
        options = {
            'Get info for user': {
                'cmd': lambda: print(data_analyzer.get_info_for(
                    options['Get info for user']['params']['User ID'].get()
                )),
                'params': {
                    'User ID': IntVar()
                }
            },
            'Get average age of raters for movie': {
                'cmd': lambda: print(data_analyzer.get_raters_avg_age(
                    options['Get average age of raters for movie']['params']['Title'].get()
                )),
                'params': {
                    'Title': StringVar()
                }
            },
            'List rated movies': {
                'cmd': lambda: print(data_analyzer.get_users_rated_movies(
                    options['List rated movies']['params']['User ID'].get(),
                    options['List rated movies']['params']['Head'].get(),
                    options['List rated movies']['params']['Graphic Results'].get()
                )),
                'params': {
                    'User ID': IntVar(),
                    'Head': IntVar(),
                    'Graphic Results': BooleanVar()
                }
            },
            'Get users\' rating average': {
                'cmd': lambda: print(data_analyzer.get_user_rating_average(
                    options['Get users\' rating average']['params']['User ID'].get()
                )),
                'params': {
                    'User ID': IntVar()
                }
            },
            'Get user\'s movie count': {
                'cmd': lambda: print(data_analyzer.get_user_movies_count(
                    options['Get user\'s movie count']['params']['User ID'].get()
                )),
                'params': {
                    'User ID': IntVar()
                }
            },
            'Get rating of user for movie': {
                'cmd': lambda: print(data_analyzer.get_user_ratings_for(
                    options['Get rating of user for movie']['params']['User ID'].get(),
                    options['Get rating of user for movie']['params']['Title'].get()
                )),
                'params': {
                    'User ID': IntVar(),
                    'Title': StringVar()
                }
            },
            'Get average ratings': {
                'cmd': lambda: print(data_analyzer.get_average_ratings(
                    options['Get average ratings']['params']['Head'].get(),
                    options['Get average ratings']['params']['Sort'].get(),
                    options['Get average ratings']['params']['Begin'].get(),
                    options['Get average ratings']['params']['End'].get(),
                    options['Get average ratings']['params']['Graphic Results'].get()
                )),
                'params': {
                    'Head': IntVar(),
                    'Sort': StringVar(),
                    'Begin': DoubleVar(),
                    'End': DoubleVar(),
                    'Graphic Results': BooleanVar()
                }
            },
            'Get rating of movie': {
                'cmd': lambda: print(data_analyzer.get_rating_of(
                    options['Get rating of movie']['params']['Title'].get()
                )),
                'params': {
                    'Title': StringVar()
                }
            },
            'Get highest rated movies': {
                'cmd': lambda: print(data_analyzer.get_highest_rated_movies(
                    options['Get highest rated movies']['params']['Head'].get(),
                    options['Get highest rated movies']['params']['Graphic Results'].get()
                )),
                'params': {
                    'Head': IntVar(),
                    'Graphic Results': BooleanVar()
                }
            },
            'Get lowest rated movies': {
                'cmd': lambda: print(data_analyzer.get_lowest_rated_movies(
                    options['Get lowest rated movies']['params']['Head'].get(),
                    options['Get lowest rated movies']['params']['Graphic Results'].get()
                )),
                'params': {
                    'Head': IntVar(),
                    'Graphic Results': BooleanVar()
                }
            },
            'Compare two movies by titles': {
                'cmd': lambda: print(data_analyzer.compare_two_movies_by_title(
                    options['Compare two movies by titles']['params']['Title One'].get(),
                    options['Compare two movies by titles']['params']['Title Two'].get(),
                    options['Compare two movies by titles']['params']['Graphic Results'].get()
                )),
                'params': {
                    'Title One': StringVar(),
                    'Title Two': StringVar(),
                    'Graphic Results': BooleanVar()
                }
            }
        }
        option = options.get(value)
        for index, param in enumerate(option['params']):
            Label(self.formFrame, text=param).grid(row=0, column=index * 2)
            Entry(self.formFrame, textvariable=option['params'][param]).grid(row=0, column=index * 2 + 1)
        Button(self.formFrame, text='Analyze', command=lambda: Application.execute_command(option['cmd'])) \
            .grid(row=1, column=int(round(len(option['params'].keys()) / 2)) + 1)

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


start()
