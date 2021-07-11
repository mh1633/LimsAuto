import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUi

current_UI = os.path.dirname(os.path.abspath(__file__))
path_UI = str(os.path.join(current_UI,'UI\\'))

def help_description_UI_clicked(self) :
    dlg = help_description_UI()
    dlg.exec()

class help_description_UI(QDialog):
    def __init__(self) :
        super().__init__()
        loadUi(path_UI + 'help_description.ui',self)

