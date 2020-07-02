# PyQt Imports
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDesktopWidget, QAction
from PyQt5.QtCore import QPoint
from PyQt5.QtGui import QIcon
from PyQt5.QtPrintSupport import *

#Python Imports
import os,sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(960,600)

        font = QtGui.QFont()
        font.setPointSize(18)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("assets/app-logo-png.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        # set the main window to be Frameless
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setIconSize(QtCore.QSize(96, 129))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # **************** Line Text Code ****************************************
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(0, 55, 960, 531))
        font = QtGui.QFont()
        font.setFamily("Product Sans")
        fnt_size = 12
        font.setPointSize(fnt_size)
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet("background-image: url(assets/pad-bg-960x600.jpg);\n" 
        "padding-top: 30.6px;\n" 
        "padding-right : 0px;")
        self.textEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.textEdit.setFrameShadow(QtWidgets.QFrame.Plain)
        self.textEdit.setLineWidth(0)
        self.textEdit.setObjectName("textEdit")
        # **************** Line Text Code *****************************************

        self.bottom_blue_footer = QtWidgets.QLabel(self.centralwidget)
        self.bottom_blue_footer.setGeometry(QtCore.QRect(0, 586, 960, 14))
        self.bottom_blue_footer.setStyleSheet("background-image: url(assets/bottom-bar-dolt-pad.png);")
        self.bottom_blue_footer.setText("")
        self.bottom_blue_footer.setObjectName("bottom_blue_footer")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 301, 57))
        self.label_2.setStyleSheet("image: url(assets/top-bar-png.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")

        # **************** Print Button Code *******************************
        self.new_btn = QtWidgets.QLabel(self.centralwidget)
        self.new_btn.setGeometry(QtCore.QRect(130, 10, 152, 85))
        self.new_btn.setStyleSheet("image: url(assets/new-btn-png.png);")
        self.new_btn.setText("")
        self.new_btn.setObjectName("new_btn")
        # **************** Print Button Code *******************************


         # **************** Close Button Code ************************************ 
        self.close_btn = QtWidgets.QLabel(self.centralwidget)
        self.close_btn.setGeometry(QtCore.QRect(876, -22, 106, 101))
        self.close_btn.setStyleSheet("image: url(assets/close-btn-png.png);")
        self.close_btn.setText("")
        self.close_btn.setObjectName("close_btn")
        # **************** Close Button Code *************************************


        # **************** Empty White Canvas Code *******************************
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 0, 681, 61))
        self.label_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.label_5.setText("")
        self.label_5.setObjectName("label_5")
        # **************** Empty White Canvas Code *******************************


        # **************** Save Button Code **************************************
        self.save_btn = QtWidgets.QLabel(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(317, 10, 108, 41))
        self.save_btn.setStyleSheet("image: url(assets/save-btn-png.png);")
        self.save_btn.setText("")
        self.save_btn.setObjectName("save_btn")
        # **************** Save Button Code **************************************


        # **************** Paste Button Code *******************************
        self.paste_btn = QtWidgets.QLabel(self.centralwidget)
        self.paste_btn.setGeometry(QtCore.QRect(430, 10, 108, 41))
        self.paste_btn.setStyleSheet("image: url(assets/paste-btn-png.png);")
        # self.paste_btn = QAction(QIcon(os.path.join('assets','paste-btn-png.png')), "Paste")
        # self.paste_btn.setText("")
        
        self.paste_btn.setToolTip("Paste the copied text")
        self.paste_btn.setObjectName("paste_btn")

        
        # **************** Paste Button Code *******************************


        # **************** Print Button Code ******************************* 
        self.print_btn = QtWidgets.QLabel(self.centralwidget)
        self.print_btn.setGeometry(QtCore.QRect(545, 10, 108, 41))
        self.print_btn.setStyleSheet("image: url(assets/print-btn-png.png);")
        self.print_btn.setText("")
        self.print_btn.setObjectName("print_btn")
        # **************** Print Button Code *******************************


        # **************** About Button Code *******************************
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(660, 10, 40, 40))
        self.label.setStyleSheet("image: url(assets/about-btn-png.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        # **************** About Button Code *******************************


        self.label_5.raise_()
        self.textEdit.raise_()
        self.bottom_blue_footer.raise_()
        self.label_2.raise_()
        self.new_btn.raise_()
        self.close_btn.raise_()
        self.save_btn.raise_()
        self.paste_btn.raise_()
        self.print_btn.raise_()
        self.label.raise_()
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # This is a sample comment

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dolt Pad"))

    def file_print(self):
        print("file printed")  






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
