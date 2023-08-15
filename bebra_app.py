from PyQt5 import QtCore, QtGui, QtWidgets
import sys



class Ui_MainWindow(object):

    #def button_reaction(self):





    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(795, 500)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.563, y1:0.563, x2:1, y2:0, stop:0.454545 rgba(0, 0, 0, 165), stop:0.886364 rgba(255, 255, 255, 255));")
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.centralwidget.setObjectName("centralwidget")

        self.Bebra_title = QtWidgets.QLabel(self.centralwidget)
        self.Bebra_title.setGeometry(QtCore.QRect(140, 20, 581, 101))
        font = QtGui.QFont()
        font.setFamily("Ravie")
        font.setPointSize(18)
        font.setBold(False)
        self.Bebra_title.setFont(font)
        self.Bebra_title.setStyleSheet("background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.Bebra_title.setObjectName("Bebra_title")

        self.Yes_button = QtWidgets.QPushButton(self.centralwidget)
        self.Yes_button.setGeometry(QtCore.QRect(110, 270, 181, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Yes_button.setFont(font)
        self.Yes_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.Yes_button.setObjectName("Yes_button")
        #self.Yes_button.setChekable(True)

        self.No_button = QtWidgets.QPushButton(self.centralwidget)
        self.No_button.setGeometry(QtCore.QRect(510, 270, 181, 24))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.No_button.setFont(font)
        self.No_button.setStyleSheet("color: rgb(255, 255, 255);")
        self.No_button.setObjectName("No_button")
        #self.No_button.setChekable(True)

        self.Bebra_label = QtWidgets.QLabel(self.centralwidget)
        self.Bebra_label.setGeometry(QtCore.QRect(320, 170, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Bebra_label.setFont(font)
        self.Bebra_label.setStyleSheet("color: rgb(255, 255, 255);")
        self.Bebra_label.setObjectName("Bebra_label")

        self.Bebra_answer = QtWidgets.QLabel(self.centralwidget)
        self.Bebra_answer.setGeometry(QtCore.QRect(348, 250, 111, 71))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.Bebra_answer.setFont(font)
        self.Bebra_answer.setStyleSheet("color: rgb(255, 255, 255);")
        self.Bebra_answer.setText("")
        self.Bebra_answer.setObjectName("Bebra_answer")

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Бебронюх"))
        self.Bebra_title.setText(_translate("MainWindow", "ХАЧУ БЕБРЫЫЫЫЫЫЫ OAAOOAOOAOAOOAOAOA"))
        self.Yes_button.setText(_translate("MainWindow", "Да"))
        self.No_button.setText(_translate("MainWindow", "Нет"))
        self.Bebra_label.setText(_translate("MainWindow", "Нюхаем беброчку?"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
