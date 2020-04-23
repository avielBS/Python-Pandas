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
        if ListRatedMoviesForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            ListRatedMoviesForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def execute(self):
        print(data_analyzer.get_users_rated_movies(self.labels['User ID'].get(), self.labels['Head'].get(), self.labels['Graphic Results'].get()))
