
from libraries.gui import *
from libraries.api import *
import sys
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentTranslator
from qfluentwidgets import FluentIcon as FIF
from libraries.utils.JsonFile import JsonFile
from config import Language

__version__ = "0.1"

class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f'个人聊天 {__version__}')
        self.resize(800, 600)
        self.addSubInterface(Settings(self), FIF.SETTING, "设置")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = FluentTranslator()
    app.installTranslator(translator)
    w = Window()
    w.show()
    sys.exit(app.exec_())
