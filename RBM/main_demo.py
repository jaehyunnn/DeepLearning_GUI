# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ex00.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!
import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import RBM.mnist_rbm_train as mnist_train
import RBM.mnist_rbm_test as mnist_test
from RBM.sub_gui.test_result import Ui_Form

class Ui_rbmWindow(QWidget):
    # CNN component button event functions
    def train(self):
        QtWidgets.QMessageBox.about(None, "Train message", "RBM 학습을 시작합니다.")
        self.textBrowser_3.setText("RBM 학습을 시작합니다.\n")
        try:
            self.th_train.start()
            QtWidgets.QMessageBox.about(None, "Train message", "RBM 학습 하는중...")
        except:
            QtWidgets.QMessageBox.about(None, "Error message", "에러발생:( 모델을 확인하세요.")
            self.textBrowser_2.setText("에러발생:( 모델을 확인하세요.")

    def test(self):
        QtWidgets.QMessageBox.about(None, "Test message", "RBM 테스트를 진행합니다.")
        self.textBrowser_3.setText("RBM 테스트를 진행합니다.\n")
        self.th_test.start()

    def trainStop(self):
        self.th_train.terminate()
        self.th_test.terminate()
        self.textBrowser_3.setText("학습을 종료합니다.")
        # self.textBrowser_3.append("\n\nTerminate training!!!")

    def showResult(self,msg):
        self.test_result.show()
        self.textBrowser_3.setText("RBM 테스트 결과 입니다.")

    # Print training log
    def print_console(self,msg):
        self.textBrowser_3.append(msg)

    def setupUi(self, MainWindow):
        self.sequence = ""
        self.undo_list = []

        MainWindow.setObjectName("RBM")
        MainWindow.resize(580, 300)

        # Setting test result dialog
        self.test_result = QtWidgets.QDialog()
        self.ui_7 = Ui_Form()
        self.ui_7.setupUi(self.test_result)

        # train signal (threading)
        self.th_train = self.Thread(parent=self, tag='train')
        self.th_train.train_msg.connect(self.print_console)

        # test signal (threading)
        self.th_test = self.Thread(parent=self, tag='test')
        self.th_test.test_msg.connect(self.showResult)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.trainButton = QtWidgets.QPushButton(self.groupBox_4)
        self.trainButton.setObjectName("trainButton")


        self.verticalLayout_6.addWidget(self.trainButton)
        self.testButton = QtWidgets.QPushButton(self.groupBox_4)
        self.testButton.setObjectName("testButton")


        self.verticalLayout_6.addWidget(self.testButton)
        self.verticalLayout_12.addWidget(self.groupBox_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_4.addWidget(self.textBrowser_2)
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableView_3 = QtWidgets.QTableView(self.tab_2)
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_7.addWidget(self.tableView_3)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setMinimumSize(QtCore.QSize(400, 100))
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_3.setMinimumSize(QtCore.QSize(400, 100))
        self.verticalLayout_11.addWidget(self.textBrowser_3)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.stopButton = QtWidgets.QPushButton(self.groupBox_5)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_8.addWidget(self.stopButton)
        self.verticalLayout_11.addLayout(self.horizontalLayout_8)
        self.verticalLayout_10.addWidget(self.groupBox_5)
        self.horizontalLayout_3.addLayout(self.verticalLayout_10)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "RBM main"))
        self.groupBox_4.setTitle(_translate("MainWindow", "RBM demo"))
        self.trainButton.setText(_translate("MainWindow", "Training"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Console"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

        # Button event call
        self.trainButton.clicked.connect(self.train)
        self.stopButton.clicked.connect(self.trainStop)
        self.testButton.clicked.connect(self.test)

    class Thread(QtCore.QThread):
        train_msg = QtCore.pyqtSignal(str)
        test_msg = QtCore.pyqtSignal(str)

        def __init__(self,tag='train',parent=None):
            super().__init__()
            self.main=parent
            self.tag=tag

        def run(self):
            if self.tag == 'train':
                mnist_train.run(worker=self)
            elif  self.tag == 'test':
                mnist_test.run(worker=self)
"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
"""
def open():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QWidget()
    ui = Ui_rbmWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())