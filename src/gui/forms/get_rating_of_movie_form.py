from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetRatingOfMovieForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetRatingOfMovieForm.__instance is None:
            GetRatingOfMovieForm()
        return GetRatingOfMovieForm.__instance

    def __init__(self):
        self._labels = {
            'Title': StringVar()
        }
        if GetRatingOfMovieForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetRatingOfMovieForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def execute(self):
        print(data_analyzer.get_rating_of(self.labels['Title'].get()))
