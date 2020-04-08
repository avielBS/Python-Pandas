from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class CompareTwoMoviesByTitlesForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if CompareTwoMoviesByTitlesForm.__instance is None:
            CompareTwoMoviesByTitlesForm()
        return CompareTwoMoviesByTitlesForm.__instance

    def __init__(self):
        self._labels = {
            'Title One': StringVar(),
            'Title Two': StringVar(),
            'Graphic Results': BooleanVar()
        }
        if CompareTwoMoviesByTitlesForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CompareTwoMoviesByTitlesForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_highest_rated_movies(
            self.labels['Title One'].get(),
            self.labels['Title Two'].get(),
            self.labels['Graphic Results'].get()
        ))
