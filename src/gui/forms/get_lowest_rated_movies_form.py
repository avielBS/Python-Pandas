from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetLowestRatedMoviesForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetLowestRatedMoviesForm.__instance is None:
            GetLowestRatedMoviesForm()
        return GetLowestRatedMoviesForm.__instance

    def __init__(self):
        self._labels = {
            'Head': IntVar(),
            'Graphic Results': BooleanVar()
        }

        self._data = None

        if GetLowestRatedMoviesForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetLowestRatedMoviesForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return None

    def execute(self):
        self._data = data_analyzer.get_lowest_rated_movies(self.labels['Head'].get(),
                                                           self.labels['Graphic Results'].get())
        print(self._data)

    @property
    def data(self):
        return self._data
