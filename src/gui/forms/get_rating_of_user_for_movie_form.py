from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetRatingOfUserForMovieForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetRatingOfUserForMovieForm.__instance is None:
            GetRatingOfUserForMovieForm()
        return GetRatingOfUserForMovieForm.__instance

    def __init__(self):
        self._labels = {
            'User ID': IntVar(),
            'Title': StringVar()
        }
        if GetRatingOfUserForMovieForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetRatingOfUserForMovieForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_user_ratings_for(
            self.labels['User ID'].get(),
            self.labels['Title'].get()
        ))