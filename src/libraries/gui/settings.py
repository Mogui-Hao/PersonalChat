
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from qfluentwidgets import BodyLabel, ComboBox
from qfluentwidgets import FluentIcon as FIF
from config import *
import os
from json import loads

class Settings(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("Settings")
        # 创建组件
        self.languageText = BodyLabel(
            CurrentLanguage["Tab"]["Settings"]["language"] + ": ", self
        )
        self.languageText.setMaximumWidth(len(CurrentLanguage) * 15 + 5)
        self.languageComboBox = ComboBox(self)
        self.languageComboBox.setMaximumWidth(100)
        for item in LanguageValues:
            self.languageComboBox.addItem(item["info"]["name"], FIF.LANGUAGE)
        self.languageComboBox.currentIndexChanged.connect(lambda index: self.languageText.setText(self.languageComboBox.itemText(index)))
        # 设置布局
        layoutHight = QHBoxLayout(self)
        # layout.addWidget(self.languageText)  # 添加语言文本标签到布局
        layoutHight.addWidget(self.languageComboBox)  # 添加语言选择框到布局
        self.setLayout(layoutHight)  # 将布局应用到窗口
