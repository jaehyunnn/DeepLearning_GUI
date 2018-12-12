# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pooling.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_TrainSubbox(QWidget):
    train_param = QtCore.pyqtSignal(str)

    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def mnist(self):
        self.train_param.emit('mnist')
    def cifar(self):
        self.train_param.emit('cifar')

    def setupUi(self, TrainSubbox):
        TrainSubbox.setObjectName("TrainSubbox")
        TrainSubbox.resize(630, 378)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(TrainSubbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(TrainSubbox)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        self.pushButton.setEnabled(True)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("CNN/image/mnist.png"))
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("CNN/image/cifar10.png"))
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.retranslateUi(TrainSubbox)
        QtCore.QMetaObject.connectSlotsByName(TrainSubbox)

    def retranslateUi(self, TrainSubbox):
        _translate = QtCore.QCoreApplication.translate
        TrainSubbox.setWindowTitle(_translate("TrainSubbox", "Train data select"))
        self.groupBox.setTitle(_translate("TrainSubbox", "Dataset"))
        self.pushButton_2.setText(_translate("TrainSubbox", "CIFAR-10"))
        self.pushButton.setText(_translate("TrainSubbox", "MNIST"))

        self.pushButton.clicked.connect(self.mnist)
        self.pushButton_2.clicked.connect(self.cifar)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    TrainSubbox = QtWidgets.QWidget()
    ui = Ui_TrainSubbox()
    ui.setupUi(TrainSubbox)
    TrainSubbox.show()
    sys.exit(app.exec_())

