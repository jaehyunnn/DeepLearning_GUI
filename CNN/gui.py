# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jhpark/workspace/ADD_GUI/2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import CNN.mnist_convolutional as mnist

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(800, 355)
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 10, 800, 251))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton_conv = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_conv.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_conv)
        self.pushButton_maxpool = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_maxpool.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton_maxpool)
        self.pushButton_avgpool = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_avgpool.setObjectName("pushButton_9")
        self.verticalLayout.addWidget(self.pushButton_avgpool)
        self.pushButton_linear = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_linear.setObjectName("pushButton_4")
        self.verticalLayout.addWidget(self.pushButton_linear)
        self.pushButton_sigmoid = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_sigmoid.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_sigmoid)
        self.pushButton_tanh = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_tanh.setObjectName("pushButton_5")
        self.verticalLayout.addWidget(self.pushButton_tanh)
        self.pushButton_relu = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_relu.setObjectName("pushButton_6")
        self.verticalLayout.addWidget(self.pushButton_relu)
        self.pushButton_softmax = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_softmax.setObjectName("pushButton_7")
        self.verticalLayout.addWidget(self.pushButton_softmax)
        self.pushButton_dropout = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_dropout.setObjectName("pushButton_8")
        self.verticalLayout.addWidget(self.pushButton_dropout)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.textBrowser = QtWidgets.QTextBrowser(self.horizontalLayoutWidget)
        self.textBrowser.setObjectName("textBrowser")
        self.horizontalLayout.addWidget(self.textBrowser)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(0, 270, 800, 71))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(10, 10, 10, 10)
        self.formLayout.setObjectName("formLayout")
        self.pushButton_undo = QtWidgets.QPushButton(self.widget)
        self.pushButton_undo.setObjectName("pushButton_11")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.pushButton_undo)
        self.pushButton_reset = QtWidgets.QPushButton(self.widget)
        self.pushButton_reset.setObjectName("pushButton_10")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.pushButton_reset)
        self.pushButton_train = QtWidgets.QPushButton(self.widget)
        self.pushButton_train.setObjectName("pushButton_13")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.pushButton_train)
        self.pushButton_store = QtWidgets.QPushButton(self.widget)
        self.pushButton_store.setObjectName("pushButton_12")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.pushButton_store)
        self.sequence = ""
        self.undo_list = []
        self.horizontalLayoutWidget.raise_()
        self.pushButton_undo.raise_()
        self.pushButton_reset.raise_()
        self.pushButton_store.raise_()
        self.textBrowser.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)


    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.pushButton_conv.setText(_translate("Form", "Convolution"))
        self.pushButton_maxpool.setText(_translate("Form", "Max-pooling"))
        self.pushButton_avgpool.setText(_translate("Form", "Avg-pooling"))
        self.pushButton_linear.setText(_translate("Form", "Linear"))
        self.pushButton_sigmoid.setText(_translate("Form", "Sigmoid"))
        self.pushButton_tanh.setText(_translate("Form", "Tanh"))
        self.pushButton_relu.setText(_translate("Form", "Relu"))
        self.pushButton_softmax.setText(_translate("Form", "Softmax"))
        self.pushButton_dropout.setText(_translate("Form", "Dropout"))
        self.pushButton_undo.setText(_translate("Form", "UNDO"))
        self.pushButton_reset.setText(_translate("Form", "Reset"))
        self.pushButton_train.setText(_translate("Form", "Traning"))
        self.pushButton_store.setText(_translate("Form", ".py로 model 저장"))
        self.textBrowser.setText(self.sequence)
        self.textBrowser.setStyleSheet("background-color: black; color: #00FF00 ")

        self.pushButton_conv.clicked.connect(self.conv)
        self.pushButton_maxpool.clicked.connect(self.maxpool)
        self.pushButton_avgpool.clicked.connect(self.avgpool)
        self.pushButton_linear.clicked.connect(self.linear)
        self.pushButton_sigmoid.clicked.connect(self.sigmoid)
        self.pushButton_tanh.clicked.connect(self.tanh)
        self.pushButton_relu.clicked.connect(self.relu)
        self.pushButton_softmax.clicked.connect(self.softmax)
        self.pushButton_dropout.clicked.connect(self.dropout)
        self.pushButton_undo.clicked.connect(self.undo)
        self.pushButton_reset.clicked.connect(self.reset)
        self.pushButton_store.clicked.connect(self.store)
        self.pushButton_train.clicked.connect(self.train)

    def conv(self):
        self.undo_list.append(self.sequence)
        param_set = ui("conv_dialog.ui",ui.TYPEDIALOG)
        param_set.show()
        self.sequence += "Convolution(output_depth=128, batch_size=None, input_dim = None, input_depth=None, kernel_size=5, stride_size=2),\n"
        self.textBrowser.setText(self.sequence)
    def maxpool(self):
        self.undo_list.append(self.sequence)
        self.sequence += "MaxPool(pool_size=2, pool_stride=None, pad = 'SAME'),\n"
        self.textBrowser.setText(self.sequence)
    def avgpool(self):
        self.undo_list.append(self.sequence)
        self.sequence += "AvgPool(pool_size=2, pool_stride=None, pad = 'SAME'),\n"
        self.textBrowser.setText(self.sequence)
    def linear(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Linear(output_dim=128, batch_size=None, input_dim = None),\n"
        self.textBrowser.setText(self.sequence)
    def sigmoid(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Sigmoid(),\n"
        self.textBrowser.setText(self.sequence)
    def tanh(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Tanh(),\n"
        self.textBrowser.setText(self.sequence)
    def relu(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Relu(),\n"
        self.textBrowser.setText(self.sequence)
    def softmax(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Softmax(),\n"
        self.textBrowser.setText(self.sequence)
    def dropout(self):
        self.undo_list.append(self.sequence)
        self.sequence += "Dropout(),\n"
        self.textBrowser.setText(self.sequence)
    def undo(self):
        try:
            self.sequence=self.undo_list[-1]
            del self.undo_list[-1]
        except:
            print("Empty sequence!")
        self.textBrowser.setText(self.sequence)
    def reset(self):
        del self.undo_list[:]
        self.sequence=""
        self.textBrowser.setText(self.sequence)
    def store(self):
        pycode =\
'''
from modules.sequential import Sequential
from modules.linear import Linear
from modules.softmax import Softmax
from modules.relu import Relu
from modules.tanh import Tanh
from modules.sigmoid import Sigmoid
from modules.dropout import Dropout
from modules.elu import Elu
from modules.convolution import Convolution
from modules.avgpool import AvgPool
from modules.maxpool import MaxPool


def nn():
    net = Sequential([%s])
    return net
'''%self.sequence
        print(pycode)
        f = open("Model.py", 'w')
        f.write(pycode)
        f.close()
        QtWidgets.QMessageBox.about(None,"Store message","모델이 성공적으로 저장되었습니다.")
    def train(self):
        reply = QtWidgets.QMessageBox.question(None, "Train message", "모델을 저장하고 학습을 시작하시겠습니까?",QtWidgets.QMessageBox.Yes|QtWidgets.QMessageBox.Cancel)
        if reply == QtWidgets.QMessageBox.Yes:
            self.store()
            QtWidgets.QMessageBox.about(None, "Train message", "학습이 시작됩니다...")
            try:
                mnist.run()
                QtWidgets.QMessageBox.about(None, "Train message", "학습이 완료됬습니다...")
            except:
                QtWidgets.QMessageBox.about(None, "Error message", "에러입니다. 모델을 확인해주세요.")
        else:
            pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
