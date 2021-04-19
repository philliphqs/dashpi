from dearpygui.core import *
from dearpygui.simple import *


class StorageField:
    @staticmethod
    def show():
        add_child('StorageChild', border=False)
        add_plot('Test')