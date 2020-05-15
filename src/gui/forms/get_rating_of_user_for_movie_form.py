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
        self._dropdowns = {
            'Title'
        }
        if GetRatingOfUserForMovieForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetRatingOfUserForMovieForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return self._dropdowns

    def execute(self):
        self._data = data_analyzer.get_user_ratings_for(self.labels['User ID'].get(), self.labels['Title'].get())
        print(self._data)

    @property
    def get_data(self):
        return self._data