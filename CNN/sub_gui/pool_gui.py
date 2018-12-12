# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pooling.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_PoolingSubbox(QWidget):
    pool_param = QtCore.pyqtSignal(list)
    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def pushButtonClicked(self):
        self.pool_param.emit(
            [self.comboBox.currentText(), self.lineEdit.text(), self.lineEdit_3.text(), self.lineEdit_2.text()])

    def setupUi(self, PoolingSubbox):
        PoolingSubbox.setObjectName("PoolingSubbox")
        PoolingSubbox.resize(261, 223)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(PoolingSubbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(PoolingSubbox)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setObjectName("label")
        self.horizontalLayout_4.addWidget(self.label)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.horizontalLayout_3.addWidget(self.lineEdit_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.pushButton = QtWidgets.QPushButton(PoolingSubbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(PoolingSubbox)
        QtCore.QMetaObject.connectSlotsByName(PoolingSubbox)

    def retranslateUi(self, PoolingSubbox):
        _translate = QtCore.QCoreApplication.translate
        PoolingSubbox.setWindowTitle(_translate("PoolingSubbox", "Setting: Pooling"))
        self.groupBox.setTitle(_translate("PoolingSubbox", "Setting"))
        self.label.setText(_translate("PoolingSubbox", "Select :"))
        self.comboBox.setItemText(0, _translate("PoolingSubbox", "Max"))
        self.comboBox.setItemText(1, _translate("PoolingSubbox", "Average"))
        self.label_2.setText(_translate("PoolingSubbox", "Pool size : "))
        self.label_3.setText(_translate("PoolingSubbox", "Pool stride: "))
        self.label_4.setText(_translate("PoolingSubbox", "Padding :"))
        self.pushButton.setText(_translate("PoolingSubbox", "OK"))

        # button event call
        self.pushButton.clicked.connect(self.pushButtonClicked)  # OK button


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PoolingSubbox = QtWidgets.QWidget()
    ui = Ui_PoolingSubbox()
    ui.setupUi(PoolingSubbox)
    PoolingSubbox.show()
    sys.exit(app.exec_())

