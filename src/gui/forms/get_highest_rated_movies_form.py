from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetHighestRatedMoviesForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetHighestRatedMoviesForm.__instance is None:
            GetHighestRatedMoviesForm()
        return GetHighestRatedMoviesForm.__instance

    def __init__(self):
        self._labels = {
            'Head': IntVar(),
            'Graphic Results': BooleanVar()
        }
        if GetHighestRatedMoviesForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetHighestRatedMoviesForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_highest_rated_movies(
            self.labels['Head'].get(),
            self.labels['Graphic Results'].get()
        ))