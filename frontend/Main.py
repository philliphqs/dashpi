from dearpygui.core import *
from dearpygui.simple import *

from frontend.ConsoleField import *
from frontend.StorageField import *


class Main:
    @staticmethod
    def show():
        with window('MainWindow'):
            add_text('DashPi')
            ConsoleField.show()
