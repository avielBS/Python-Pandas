from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetUsersRatingAverageForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetUsersRatingAverageForm.__instance is None:
            GetUsersRatingAverageForm()
        return GetUsersRatingAverageForm.__instance

    def __init__(self):
        self._labels = {
            'User ID': IntVar()
        }
        if GetUsersRatingAverageForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetUsersRatingAverageForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_user_rating_average(self.labels['User ID'].get()))