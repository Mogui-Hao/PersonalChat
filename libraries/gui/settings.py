
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import BodyLabel, ComboBox
from qfluentwidgets import FluentIcon as FIF
import os

class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Settings")
        # 创建组件
        text = "语言"
        self.languageText = BodyLabel(text + ":", self)
        self.languageText.setMaximumWidth(len(text) * 15 + 5)
        self.languageComboBox = ComboBox(self)
        self.languageComboBox.addItem("中文", FIF.LANGUAGE)
        self.languageComboBox.addItem("English", FIF.LANGUAGE)

        # 设置布局
        layout = QHBoxLayout(self)
        layout.addWidget(self.languageText)  # 添加语言文本标签到布局
        layout.addWidget(self.languageComboBox)  # 添加语言选择框到布局

        self.setLayout(layout)  # 将布局应用到窗口
