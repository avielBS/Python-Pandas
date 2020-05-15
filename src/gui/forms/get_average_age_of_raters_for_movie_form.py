from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetAverageAgeOfRatersForMovieForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetAverageAgeOfRatersForMovieForm.__instance is None:
            GetAverageAgeOfRatersForMovieForm()
        return GetAverageAgeOfRatersForMovieForm.__instance

    def __init__(self):
        self._labels = {
            'Title': StringVar()
        }
        self._dropdowns = {
            'Title'
        }
        if GetAverageAgeOfRatersForMovieForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetAverageAgeOfRatersForMovieForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return self._dropdowns

    def execute(self):
        self._data = data_analyzer.get_raters_avg_age(self.labels['Title'].get())
        print(self._data)

    @property
    def get_data(self):
        return self._data