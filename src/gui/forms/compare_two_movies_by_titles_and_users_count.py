from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class CompareTwoMoviesByTitlesAndUsersCountForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if CompareTwoMoviesByTitlesAndUsersCountForm.__instance is None:
            CompareTwoMoviesByTitlesAndUsersCountForm()
        return CompareTwoMoviesByTitlesAndUsersCountForm.__instance

    def __init__(self):
        self._labels = {
            'Title One': StringVar(),
            'Title Two': StringVar(),
            'Graphic Results': BooleanVar()
        }

        self._dropdowns = {
            'Title One',
            'Title Two'
        }

        self._data = None

        if CompareTwoMoviesByTitlesAndUsersCountForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            CompareTwoMoviesByTitlesAndUsersCountForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return self._dropdowns

    def execute(self):
        self._data = data_analyzer.compare_two_movies_by_title_and_users_count(self.labels['Title One'].get(),
                                                                               self.labels['Title Two'].get(),
                                                                               self.labels['Graphic Results'].get())
        print(self._data)

    @property
    def data(self):
        return self._data
