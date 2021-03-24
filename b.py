import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic
from health_param import health_pa

import sys
# sys.stdout = open('output.txt','a')
        
#UI파일 연결
#단, UI파일은 Python 코드 파일과 같은 디렉토리에 위치해야한다.
form_class = uic.loadUiType("b.ui")[0]

#화면을 띄우는데 사용되는 Class 선언
class WindowClass(QMainWindow, form_class) :
    def __init__(self) :
        super().__init__()
        self.setupUi(self)

        self.tw.setRowCount(100)	
        self.tw.setColumnCount(3)
        self.tw.setHorizontalHeaderItem(0,QTableWidgetItem("이름"))
        self.tw.setHorizontalHeaderItem(1,QTableWidgetItem("생년월일"))
        self.tw.setHorizontalHeaderItem(2,QTableWidgetItem("비번"))

        self.addItem()
        
        self.tw.cellClicked.connect(self.twClicked)
        self.fopen_btn.clicked.connect(self.addItem)

        #버튼에 기능을 연결하는 코드
        self.ma_btn.clicked.connect(self.maFunction)

    def twClicked(self):
        try:
            rownum = self.tw.currentRow()
            self.le_name.setText( self.tw.item(rownum, 0).text() )
            self.le_birth.setText( self.tw.item(rownum, 1).text() )
            self.le_pw.setText ( self.tw.item(rownum, 2).text() )
        except :
            self.le_name.setText( '' )
            self.le_birth.setText( '' )
            self.le_pw.setText ( '' )

    def addItem(self) :
        with open('output.txt','a+',encoding='UTF8') as f:
            f.seek(0)
            lines = f.readlines()
            for i,line in enumerate(lines):
                self.tw.setItem(i,0,QTableWidgetItem(line.split(' ')[0]))
                self.tw.setItem(i,1,QTableWidgetItem(line.split(' ')[1]))
                self.tw.setItem(i,2,QTableWidgetItem(line.split(' ')[2]))

    #btn_1이 눌리면 작동할 함수
    def maFunction(self) :
        try:
            health_pa(self.le_name.text(),self.le_birth.text(),self.le_pw.text())
        except Exception as e:
            print(e)
            print("예외가 발생")        

if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = WindowClass() 
    myWindow.show()
    app.exec_()