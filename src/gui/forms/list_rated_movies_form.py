from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class ListRatedMoviesForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if ListRatedMoviesForm.__instance is None:
            ListRatedMoviesForm()
        return ListRatedMoviesForm.__instance

    def __init__(self):
        self._labels = {
            'User ID': IntVar(),
            'Head': IntVar(),
            'Graphic Results': BooleanVar()
        }

        self._data = None

        if ListRatedMoviesForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ListRatedMoviesForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return None

    def execute(self):
        self._data = data_analyzer.get_users_rated_movies(self.labels['User ID'].get(),
                                                          self.labels['Head'].get(),
                                                          self.labels['Graphic Results'].get())
        print(self._data)

    @property
    def data(self):
        return self._data
