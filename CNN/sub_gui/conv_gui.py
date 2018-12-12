# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pooling.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_ConvSubbox(QWidget):
    conv_param = QtCore.pyqtSignal(list)
    # OK 버튼을 눌렀을 때 main 창으로 시그널 전달해주는 함수
    def conv_param_send(self):
        self.conv_param.emit([self.lineEdit.text(),self.lineEdit_2.text(),self.lineEdit_3.text(), self.lineEdit_4.text(),
                              self.lineEdit_5.text(), self.lineEdit_6.text(), self.lineEdit_7.text()])
    def setupUi(self, ConvSubbox):
        ConvSubbox.setObjectName("ConvSubbox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(ConvSubbox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(ConvSubbox)
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
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setObjectName("input_depth")
        self.horizontalLayout_4.addWidget(self.label_4)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_4.setObjectName("input_depth")
        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setObjectName("kernel_size")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_5.setObjectName("kernel_size")
        self.horizontalLayout_5.addWidget(self.lineEdit_5)

        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setObjectName("stride_size")
        self.horizontalLayout_6.addWidget(self.label_6)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_6.setObjectName("stride_size")
        self.horizontalLayout_6.addWidget(self.lineEdit_6)

        self.verticalLayout.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setObjectName("pad")
        self.horizontalLayout_7.addWidget(self.label_7)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_7.setObjectName("pad")
        self.horizontalLayout_7.addWidget(self.lineEdit_7)

        self.verticalLayout.addLayout(self.horizontalLayout_7)
        self.verticalLayout_2.addWidget(self.groupBox)

        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")

        self.pushButton = QtWidgets.QPushButton(ConvSubbox)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_5.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.retranslateUi(ConvSubbox)
        QtCore.QMetaObject.connectSlotsByName(ConvSubbox)

    def retranslateUi(self, ConvSubbox):
        _translate = QtCore.QCoreApplication.translate
        ConvSubbox.setWindowTitle(_translate("ConvSubbox", "Setting: Conv"))
        self.groupBox.setTitle(_translate("ConvSubbox", "Setting"))
        self.label.setText(_translate("ConvSubbox", "Output depth:"))
        self.label_2.setText(_translate("ConvSubbox", "Batch size :"))
        self.label_3.setText(_translate("ConvSubbox", "Width & Height :"))
        self.label_4.setText(_translate("ConvSubbox", "Input depth :"))
        self.label_5.setText(_translate("ConvSubbox", "Kernel size :"))
        self.label_6.setText(_translate("ConvSubbox", "Stride :"))
        self.label_7.setText(_translate("ConvSubbox", "Padding :"))

        self.pushButton.setText(_translate("ConvSubbox", "OK"))

        # button event call
        self.pushButton.clicked.connect(self.conv_param_send)  # OK button
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ConvSubbox = QtWidgets.QWidget()
    ui = Ui_ConvSubbox()
    ui.setupUi(ConvSubbox)
    ConvSubbox.show()
    sys.exit(app.exec_())
