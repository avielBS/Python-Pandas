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
        if GetUsersMovieCountForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetUsersMovieCountForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_user_movies_count(self.labels['User ID'].get()))
