# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pooling.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_LinearSubbox(QWidget):
    linear_param = QtCore.pyqtSignal(list)
    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def linear_param_send(self):
        self.linear_param.emit([self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text()])

    def setupUi(self, LinearSubbox):
        LinearSubbox.setObjectName("LinearSubbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(LinearSubbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(LinearSubbox)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("output_depth")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("output_depth")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("batch_size")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("batch_size")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("width_height")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("width_height")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButton = QtWidgets.QPushButton(LinearSubbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(LinearSubbox)
        QtCore.QMetaObject.connectSlotsByName(LinearSubbox)

    def retranslateUi(self, LinearSubbox):
        _translate = QtCore.QCoreApplication.translate
        LinearSubbox.setWindowTitle(_translate("LinearSubbox", "Setting: linear"))
        self.groupBox.setTitle(_translate("LinearSubbox", "Setting"))
        self.label.setText(_translate("LinearSubbox", "Output dim:"))
        self.label_2.setText(_translate("LinearSubbox", "Batch size :"))
        self.label_3.setText(_translate("LinearSubbox", "Input dim :"))

        self.pushButton.setText(_translate("LinearSubbox", "OK"))

        # button event call
        self.pushButton.clicked.connect(self.linear_param_send)  # OK button

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LinearSubbox = QtWidgets.QWidget()
    ui = Ui_LinearSubbox()
    ui.setupUi(LinearSubbox)
    LinearSubbox.show()
    sys.exit(app.exec_())
