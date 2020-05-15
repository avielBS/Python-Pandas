from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetMovieRatedUsersCountForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetMovieRatedUsersCountForm.__instance is None:
            GetMovieRatedUsersCountForm()
        return GetMovieRatedUsersCountForm.__instance

    def __init__(self):
        self._labels = {
            'Title': StringVar()
        }

        self._dropdowns = {
            'Title'
        }
        if GetMovieRatedUsersCountForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetMovieRatedUsersCountForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return self._dropdowns

    def execute(self):
        print(data_analyzer.get_movie_rated_users_count(self.labels['Title'].get()))
