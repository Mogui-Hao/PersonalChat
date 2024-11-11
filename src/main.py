
from libraries.gui import *
import sys
from PyQt6.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentTranslator, setTheme, Theme
from qfluentwidgets import FluentIcon as FIF
from config import *
from json import load, dump
from json.decoder import JSONDecodeError
from libraries.api.utils.JsonFile import JsonFile

__version__ = "0.1"
Config = Config
try:
    if os.path.exists(ConfigPath):
        Config = JsonFile(ConfigPath)
    else:
        raise JSONDecodeError
except JSONDecodeError:
    with open(ConfigPath, "w") as f:
        dump(Config, f)
finally:
    Config = JsonFile(ConfigPath)

class Window(FluentWindow):
    def __init__(self):
        super().__init__()
        setTheme(getattr(Theme, Config.Json["style"]["theme"].upper()))
        self.setWindowTitle(f'个人聊天 {__version__}')
        self.resize(800, 600)

        # self.addSubInterface(S(self), FIF.SETTING, "设置")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    translator = FluentTranslator()
    app.installTranslator(translator)
    w = Window()
    w.show()
    sys.exit(app.exec())

