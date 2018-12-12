# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_file_load.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from CNN.sub_gui.test_gui import Ui_TestSubbox

class Ui_TestPathSubbox(QWidget):
    test_data_path_param = QtCore.pyqtSignal(list)
    param_list=[]
    dir={}
    def prediction(self,signal):
        self.param_list.append(signal)
        self.test_data_path_param.emit(self.param_list)
        self.test_data_select_dialog.hide()

    def test_data_select(self):
        self.param_list.append(self.dir)
        self.test_data_select_dialog.show()

    def image(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'CNN/data')
        print(fname)
        self.dir['image']=fname[0]
        self.textBrowser_2.setText(fname[0])
        self.label.setPixmap(QtGui.QPixmap("%s"%fname[0]))

    def setupUi(self, TestPathSubbox):
        TestPathSubbox.setObjectName("TestPathSubbox")
        TestPathSubbox.resize(410, 400)

        self.test_data_select_dialog = QtWidgets.QDialog()
        self.ui = Ui_TestSubbox()
        self.ui.setupUi(self.test_data_select_dialog)
        self.ui.test_param.connect(self.prediction)

        self.centralwidget = QtWidgets.QWidget(TestPathSubbox)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(160, 340, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(310, 80, 81, 41))
        self.verticalLayoutWidget_3.setObjectName("verticalLayoutWidget_3")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(20, 20, 75, 23))
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(20, 20, 280, 100))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(189, 130, 201, 200))
        self.label.setText("")
        self.label.setObjectName("label")

        self.statusbar = QtWidgets.QStatusBar(TestPathSubbox)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(TestPathSubbox)
        QtCore.QMetaObject.connectSlotsByName(TestPathSubbox)

    def retranslateUi(self, TestPathSubbox):
        _translate = QtCore.QCoreApplication.translate
        TestPathSubbox.setWindowTitle(_translate("TestPathSubbox", "Load test data"))
        self.pushButton.setText(_translate("TestPathSubbox", "Prediction"))
        self.pushButton_4.setText(_translate("TestPathSubbox", "Image"))

        self.pushButton_4.clicked.connect(self.image)
        self.pushButton.clicked.connect(self.test_data_select)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TestPathSubbox = QtWidgets.QWidget()
    ui = Ui_TestPathSubbox()
    ui.setupUi(TestPathSubbox)
    TestPathSubbox.show()
    sys.exit(app.exec_())

