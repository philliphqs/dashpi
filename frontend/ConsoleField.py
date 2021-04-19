from dearpygui.core import *
from dearpygui.simple import *


class ConsoleField:
    @staticmethod
    def show():
        add_child('LogChild')
        add_logger('Logger',
                   auto_scroll=True,
                   autosize_x=True,
                   height=200,
                   clear_button=False,
                   auto_scroll_button=False)

        log_info('You need to login to your RaspberryPi! '
                 'Use /login IP/HOSTNAME PASSWORD PORT(Leave it alone for default)',
                 logger='Logger')
        end()
