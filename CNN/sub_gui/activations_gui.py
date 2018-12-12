# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'activations.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_ActSubbox(QWidget):
    act_param = QtCore.pyqtSignal(list)
    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def act_param_send(self):
        self.act_param.emit([self.comboBox.currentText()])

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(224, 82)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Setting: Activations"))
        self.label.setText(_translate("Form", "Select :"))
        self.comboBox.setItemText(0, _translate("Form", "Relu"))
        self.comboBox.setItemText(1, _translate("Form", "TanH"))
        self.comboBox.setItemText(2, _translate("Form", "Elu"))
        self.comboBox.setItemText(3, _translate("Form", "Sigmoid"))
        self.comboBox.setItemText(4, _translate("Form", "Softmax"))
        self.pushButton.setText(_translate("Form", "OK"))

        # button event call
        self.pushButton.clicked.connect(self.act_param_send)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_ActSubbox()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

