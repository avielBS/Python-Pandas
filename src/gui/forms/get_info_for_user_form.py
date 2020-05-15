from .form import Form
from tkinter import *
from data_analyzer import DataAnalyzer

data_analyzer = DataAnalyzer.get_instance()


class GetInfoForUserForm(Form):
    __instance = None

    @staticmethod
    def get_instance():
        if GetInfoForUserForm.__instance is None:
            GetInfoForUserForm()
        return GetInfoForUserForm.__instance

    def __init__(self):
        self._labels = {
            'User ID': IntVar()
        }

        self._data = None

        if GetInfoForUserForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetInfoForUserForm.__instance = self

    @property
    def labels(self):
        return self._labels

    @property
    def dropdowns(self):
        return None

    def execute(self):
        self._data = data_analyzer.get_info_for(self.labels['User ID'].get())
        print(self._data)

    @property
    def data(self):
        return self._data
