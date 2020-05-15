from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetUsersMovieCountForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetUsersMovieCountForm.__instance is None:
            GetUsersMovieCountForm()
        return GetUsersMovieCountForm.__instance

    def __init__(self):
        self._labels = {
            'User ID': IntVar()
        }

        self._data = None

        if GetUsersMovieCountForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetUsersMovieCountForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return None

    def execute(self):
        self._data = data_analyzer.get_user_movies_count(self.labels['User ID'].get())
        print(self._data)

    @property
    def data(self):
        return self._data
