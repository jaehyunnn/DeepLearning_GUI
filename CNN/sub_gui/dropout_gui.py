# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activations.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_DropoutSubbox(QWidget):
    dropout_param = QtCore.pyqtSignal(str)

    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def dropout_param_send(self):
        self.dropout_param.emit(self.lineEdit.text())

    def setupUi(self, DropoutSubbox):
        DropoutSubbox.setObjectName("DropoutSubbox")
        DropoutSubbox.resize(224, 82)
        self.verticalLayout = QtWidgets.QVBoxLayout(DropoutSubbox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(DropoutSubbox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(DropoutSubbox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(DropoutSubbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DropoutSubbox)
        QtCore.QMetaObject.connectSlotsByName(DropoutSubbox)

    def retranslateUi(self, DropoutSubbox):
        _translate = QtCore.QCoreApplication.translate
        DropoutSubbox.setWindowTitle(_translate("DropoutSubbox", "Setting: Dropout"))
        self.label.setText(_translate("DropoutSubbox", "Keep probability :"))
        self.pushButton.setText(_translate("DropoutSubbox", "OK"))

        self.pushButton.clicked.connect(self.dropout_param_send)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DropoutSubbox = QtWidgets.QWidget()
    ui = Ui_DropoutSubbox()
    ui.setupUi(DropoutSubbox)
    DropoutSubbox.show()
    sys.exit(app.exec_())

