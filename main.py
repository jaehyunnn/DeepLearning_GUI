# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\JaeHyun\Documents\git\ADD_GUI_complete\main.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!
import sys
import os

from PyQt5 import QtCore, QtGui, QtWidgets
from CNN.main_demo import Ui_cnnWindow
from RNN.main_demo import Ui_rnnWindow
from RBM.main_demo import Ui_rbmWindow

class Ui_MainWindow(object):
    def open_cnn(self):
        self.cnn.show()
    def open_rnn(self):
        self.rnn.show()
    def open_rbm(self):
        self.rbm.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(380, 360)
        MainWindow.setMinimumSize(QtCore.QSize(380, 360))

        # Module dialog
        self.cnn = QtWidgets.QDialog()
        self.cnn_ui = Ui_cnnWindow()
        self.cnn_ui.setupUi(self.cnn)

        self.rnn = QtWidgets.QDialog()
        self.rnn_ui = Ui_rnnWindow()
        self.rnn_ui.setupUi(self.rnn)

        self.rbm = QtWidgets.QDialog()
        self.rbm_ui = Ui_rbmWindow()
        self.rbm_ui.setupUi(self.rbm)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 220, 361, 131))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.verticalLayoutWidget)
        self.groupBox.setObjectName("groupBox")
        self.cnnButton = QtWidgets.QPushButton(self.groupBox)
        self.cnnButton.setGeometry(QtCore.QRect(0, 30, 359, 23))
        self.cnnButton.setObjectName("cnnButton")
        self.rnnButton = QtWidgets.QPushButton(self.groupBox)
        self.rnnButton.setGeometry(QtCore.QRect(0, 60, 359, 23))
        self.rnnButton.setObjectName("rnnButton")
        self.rbmButton = QtWidgets.QPushButton(self.groupBox)
        self.rbmButton.setGeometry(QtCore.QRect(0, 90, 359, 23))
        self.rbmButton.setObjectName("rbmButton")
        self.verticalLayout.addWidget(self.groupBox)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 29, 361, 181))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("logo/Korea.png"))
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.label = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("logo/ADD.png"))
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 10, 361, 20))
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 380, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "MODULES"))
        self.cnnButton.setText(_translate("MainWindow", "CNN"))
        self.rnnButton.setText(_translate("MainWindow", "RNN"))
        self.rbmButton.setText(_translate("MainWindow", "RBM"))
        self.label_3.setText(_translate("MainWindow", "딥러닝 설계 모듈 DEMO"))

        self.cnnButton.clicked.connect(self.open_cnn)
        self.rnnButton.clicked.connect(self.open_rnn)
        self.rbmButton.clicked.connect(self.open_rbm)


# For printing exception
sys._excepthook = sys.excepthook

def my_exception_hook(exctype, value, traceback):
    # Print the error and traceback
    print(exctype, value, traceback)
    # Call the normal Exception hook after
    sys._excepthook(exctype, value, traceback)
    sys.exit(1)

# Set the exception hook to our wrapping function
sys.excepthook = my_exception_hook

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    except:
        print("Exiting")
