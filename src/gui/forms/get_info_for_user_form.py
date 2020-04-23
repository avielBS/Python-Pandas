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
        if GetInfoForUserForm.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            GetInfoForUserForm.__instance = self

    @property
    def labels(self):
        return self._labels

    def execute(self):
        print(data_analyzer.get_info_for(self.labels['User ID'].get()))
