from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetAverageRatingsForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetAverageRatingsForm.__instance is None:
            GetAverageRatingsForm()
        return GetAverageRatingsForm.__instance

    def __init__(self):
        self._labels = {
            'Head': IntVar(),
            'Sort': StringVar(),
            'Begin': DoubleVar(),
            'End': DoubleVar(),
            'Graphic Results': BooleanVar()
        }
        if GetAverageRatingsForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetAverageRatingsForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def get_command(self):
        return lambda: print(data_analyzer.get_average_ratings(
            self.labels['Head'].get(),
            self.labels['Sort'].get(),
            self.labels['Begin'].get(),
            self.labels['End'].get(),
            self.labels['Graphic Results'].get()
        ))
