import sys
import os
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.uic import loadUi
import Sub_UI

#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
current_UI = os.path.dirname(os.path.abspath(__file__))
form_class = uic.loadUiType(str(os.path.join(current_UI,'UI\\'))+'Main_UI.ui')[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)
# 메인함수에 사용될 전역 변수들
        self.run_usable = 1

# 화면 전환에도 항상 위에 위치
        # self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.RPA_RUN.clicked.connect(self.Run)
        self.RPA_STOP.clicked.connect(self.Run)
        self.menu_help_help.triggered.connect(Sub_UI.help_description_UI_clicked)

#-----------------------  Main Run -----------------------

    def Run(self) :
        if self.run_usable == 1 :
            self.run_usable = 0
            self.RPA_RUN.setEnabled(False)
            self.RPA_STOP.setEnabled(True)
        



#-----------------------  Main Run Stop  -----------------------

        else :
            self.run_usable = 1
            self.RPA_STOP.setEnabled(False)
            self.RPA_RUN.setEnabled(True)

    
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    Main_UI = WindowClass()
    Main_UI.show()
    app.exec_()