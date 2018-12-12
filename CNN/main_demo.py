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
from CNN.sub_gui.pool_gui import Ui_PoolingSubbox
from CNN.sub_gui.conv_gui import Ui_ConvSubbox
from CNN.sub_gui.activations_gui import Ui_ActSubbox
from CNN.sub_gui.linear_gui import Ui_LinearSubbox
from CNN.sub_gui.dropout_gui import Ui_DropoutSubbox
from CNN.sub_gui.train_gui import Ui_TrainSubbox
from CNN.sub_gui.testpath_gui import Ui_TestPathSubbox
import CNN.mnist_convolutional as mnist
import CNN.cifar_convolutional as cifar

class Ui_cnnWindow(QWidget):
    # CNN component button event functions
    def conv(self):
        self.conv_dialog.show()
        self.textBrowser_2.setText("Convolution을 추가합니다.")
    def pool(self):
        self.pool_dialog.show()
        self.textBrowser_2.setText("Pooling을 추가합니다.")
    def activation(self):
        self.activation_dialog.show()
        self.textBrowser_2.setText("Activation function을 추가합니다.")
    def linear(self):
        self.linear_dialog.show()
        self.textBrowser_2.setText("Linear를 추가합니다.")
    def dropout(self):
        self.dropout_dialog.show()
        self.textBrowser_2.setText("Drop-out을 추가합니다.")
    def undo(self):
        try:
            self.sequence=self.undo_list[-1]
            del self.undo_list[-1]
            self.textBrowser_2.setText("UNDO !")
        except:
            self.textBrowser_2.setText("Sequence가 비었습니다.")
        self.textBrowser.setText(self.sequence)
    def reset(self):
        del self.undo_list[:]
        self.sequence=""
        self.textBrowser.setText(self.sequence)
        self.textBrowser_2.setText("Sequence를 초기화 합니다..")
    def store(self):
        pycode = \
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


def nn(phase):
    net = Sequential([%s])
    return net
''' % self.sequence
        print(pycode)
        f = open("Model.py", 'w')
        f.write(pycode)
        f.close()
        QtWidgets.QMessageBox.about(None, "Store message", "모델이 성공적으로 저장되었습니다.")
        self.textBrowser_2.setText("'Model.py'가 저장되었습니다.")

    # Train & Test button event function
    def train(self):
        self.train_dialog.show()
        self.textBrowser_2.setText("Training 데이터를 선택합니다.")
    def test(self):
        self.test_data_path_dialog.show()
        self.textBrowser_2.setText("Test 데이터를 선택합니다.")

    def trainStop(self):
        self.th_cifar.terminate()
        self.th_mnist.terminate()
        self.textBrowser_2.setText("Training을 종료합니다.")
        self.textBrowser_3.append("\n\nTerminate training!!!")

    # Event functions after get the signals (CNN component)
    def gen_conv_sequence(self, signal):
        self.undo_list.append(self.sequence)
        for idx, value in enumerate(signal):
            if value == "":
                signal[idx]="'None'"
        self.sequence += "Convolution(output_depth=%s, batch_size=%s, input_dim=%s, input_depth=%s, kernel_size=%s, stride_size=%s, pad=%s, phase=phase),\n\n"\
                         %(signal[0],signal[1],signal[2],signal[3], signal[4], signal[5], signal[6])
        self.textBrowser.setText(self.sequence)
        self.conv_dialog.hide()

    def gen_pool_sequence(self, signal):
        self.undo_list.append(self.sequence)
        for idx, value in enumerate(signal):
            if value == "":
                signal[idx]="'None'"
        if signal[0] == 'Max':
            self.sequence += "MaxPool(pool_size=%s, pool_stride=%s, pad=%s),\n\n"\
                             %(signal[1],signal[2],signal[3])
        elif signal[0] == 'Average':
            self.sequence += "AvgPool(pool_size=%s, pool_stride=%s, pad=%s),\n\n" \
                             % (signal[1], signal[2], signal[3])
        else:
            QtWidgets.QMessageBox.about(None, "warning message", "Pooling 종류를 선택해주세요.")
        self.textBrowser.setText(self.sequence)
        self.pool_dialog.hide()

    def gen_activation_sequence(self, signal):
        self.undo_list.append(self.sequence)
        if signal[0] == 'Relu':
            self.sequence += "Relu(),\n\n"
        elif signal[0] == 'TanH':
            self.sequence += "Tanh(),\n\n"
        elif signal[0] == 'Elu':
            self.sequence += "Elu(),\n\n"
        elif signal[0] == 'Sigmoid':
            self.sequence += "Sigmoid(),\n\n"
        elif signal[0] == 'Softmax':
            self.sequence += "Softmax(),\n\n"
        else:
            QtWidgets.QMessageBox.about(None, "warning message", "Activation 종류를 선택해주세요.")
        self.textBrowser.setText(self.sequence)
        self.activation_dialog.hide()

    def gen_linear_sequence(self, signal):
        self.undo_list.append(self.sequence)
        for idx, value in enumerate(signal):
            if value == "":
                signal[idx] = "'None'"
        self.sequence += "Linear(output_dim=%s, batch_size=%s, input_dim=%s),\n\n" \
                         % (signal[0], signal[1], signal[2])
        self.textBrowser.setText(self.sequence)
        self.linear_dialog.hide()

    def gen_dropout_sequence(self, signal):
        self.undo_list.append(self.sequence)
        if signal == "":
            self.sequence += "Dropout(),\n\n"
        else:
            self.sequence += "Dropout(keep_prob=%s),\n\n" \
                         % (signal)
        self.textBrowser.setText(self.sequence)
        self.dropout_dialog.hide()

    # Print training log
    def print_console(self,msg):
        self.textBrowser_3.append(msg)

    # Print test result
    def print_console_test(self, msg):
        self.textBrowser_3.append(msg[0])
        self.textBrowser_3.append(msg[1])

    # Train module
    def mnist_train_module(self):
        QtWidgets.QMessageBox.about(None, "Train message", "MNIST 학습이 시작됩니다...")
        self.textBrowser_2.setText("MNIST 학습이 시작됩니다...")
        try:
            self.th_mnist.start()
            QtWidgets.QMessageBox.about(None, "Train message", "MNIST 학습 하는중...")
        except:
            QtWidgets.QMessageBox.about(None, "Error message", "에러발생:( 모델을 확인하세요.")
            self.textBrowser_2.setText("에러발생:( 모델을 확인하세요.")
        self.train_dialog.hide()


    def cifar_train_module(self):
        QtWidgets.QMessageBox.about(None, "Train message", "CIFAR10 학습이 시작됩니다...")
        self.textBrowser_2.setText("CIFAR10 학습이 시작됩니다...")
        try:
            self.th_cifar.start()
            QtWidgets.QMessageBox.about(None, "Train message", "CIFAR10 학습 하는중...")
        except:
            QtWidgets.QMessageBox.about(None, "Error message", "에러발생:( 모델을 확인하세요.")
            self.textBrowser_2.setText("에러발생:( 모델을 확인하세요.")
        self.train_dialog.hide()

    # Event functions after get the signals (Train and Test)
    def gen_train_sequence(self, signal):
        if signal=='mnist':
            if self.sequence =="":
                self.mnist_train_module()
            else:
                reply = QtWidgets.QMessageBox.question(None, "Train message", "모델을 저장하고 학습을 시작하시겠습니까?",
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.store()
                    self.mnist_train_module()
        elif signal=='cifar':
            if self.sequence =="":
                self.cifar_train_module()
            else:
                reply = QtWidgets.QMessageBox.question(None, "Train message", "모델을 저장하고 학습을 시작하시겠습니까?",
                                                       QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.Cancel)
                if reply == QtWidgets.QMessageBox.Yes:
                    self.store()
                    self.cifar_train_module()
        else:
            QtWidgets.QMessageBox.about(None, "Exception message", "잘못 된 선택입니다.")

    def test_data_select(self, signal):
        if signal[1] == 'mnist':
            self.mnist_prediction(signal[0])
        if signal[1] == 'cifar':
            self.cifar_prediction(signal[0])
        self.test_data_path_dialog.hide()

    def mnist_prediction(self,signal):
        # mnist test (threading)
        self.th_mnist_test = self.Thread(parent=self, tag='test', dataset='mnist', image_dir=signal['image'])

        self.th_mnist_test.test_msg.connect(self.print_console_test)
        self.th_mnist_test.start()

    def cifar_prediction(self,signal):
        # cifar test (threading)
        self.th_cifar_test = self.Thread(parent=self, tag='test', dataset='cifar', image_dir=signal['image'])

        self.th_cifar_test.test_msg.connect(self.print_console_test)
        self.th_cifar_test.start()

    def setupUi(self, MainWindow):
        self.sequence = ""
        self.undo_list = []

        MainWindow.setObjectName("CNN")
        MainWindow.resize(1230, 380)

        # Setting convolution parameter dialog
        self.conv_dialog = QtWidgets.QDialog()
        self.ui = Ui_ConvSubbox()
        self.ui.setupUi(self.conv_dialog)
        self.ui.conv_param.connect(self.gen_conv_sequence)

        # Setting pooling dialog
        self.pool_dialog = QtWidgets.QDialog()
        self.ui_2 = Ui_PoolingSubbox()
        self.ui_2.setupUi(self.pool_dialog)
        self.ui_2.pool_param.connect(self.gen_pool_sequence)

        # Setting activation select dialog
        self.activation_dialog = QtWidgets.QDialog()
        self.ui_3 = Ui_ActSubbox()
        self.ui_3.setupUi(self.activation_dialog)
        self.ui_3.act_param.connect(self.gen_activation_sequence)

        # Setting linear select dialog
        self.linear_dialog = QtWidgets.QDialog()
        self.ui_4 = Ui_LinearSubbox()
        self.ui_4.setupUi(self.linear_dialog)
        self.ui_4.linear_param.connect(self.gen_linear_sequence)

        # Setting train data select dialog
        self.train_dialog = QtWidgets.QDialog()
        self.ui_5 = Ui_TrainSubbox()
        self.ui_5.setupUi(self.train_dialog)
        self.ui_5.train_param.connect(self.gen_train_sequence)

        # Setting drop-out dialog
        self.dropout_dialog = QtWidgets.QDialog()
        self.ui_6 = Ui_DropoutSubbox()
        self.ui_6.setupUi(self.dropout_dialog)
        self.ui_6.dropout_param.connect(self.gen_dropout_sequence)

        # Setting test path dialog
        self.test_data_path_dialog = QtWidgets.QDialog()
        self.ui_7 = Ui_TestPathSubbox()
        self.ui_7.setupUi(self.test_data_path_dialog)
        self.ui_7.test_data_path_param.connect(self.test_data_select)

        # mnist train signal (threading)
        self.th_mnist = self.Thread(parent=self, dataset='mnist')
        self.th_mnist.train_msg.connect(self.print_console)

        # cifar train signal (threading)
        self.th_cifar = self.Thread(parent=self,dataset='cifar')
        self.th_cifar.train_msg.connect(self.print_console)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setObjectName("verticalLayout_12")

        ## CNN component group box
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.groupBox.setObjectName("groupBox")
        self.groupBox.setMinimumSize(QtCore.QSize(200, 180))
        self.groupBox.setMaximumSize(QtCore.QSize(200, 180))
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.convButton = QtWidgets.QPushButton(self.groupBox)
        self.convButton.setObjectName("convButton")
        self.verticalLayout_3.addWidget(self.convButton)
        self.poolButton = QtWidgets.QPushButton(self.groupBox)
        self.poolButton.setObjectName("poolButton")
        self.verticalLayout_3.addWidget(self.poolButton)
        self.actButton = QtWidgets.QPushButton(self.groupBox)
        self.actButton.setObjectName("actButton")
        self.verticalLayout_3.addWidget(self.actButton)
        self.linearButton = QtWidgets.QPushButton(self.groupBox)
        self.linearButton.setObjectName("linearButton")
        self.verticalLayout_3.addWidget(self.linearButton)
        self.dropoutButton = QtWidgets.QPushButton(self.groupBox)
        self.dropoutButton.setObjectName("dropoutButton")
        self.verticalLayout_3.addWidget(self.dropoutButton)
        self.verticalLayout_12.addWidget(self.groupBox)

        ## Train/Test group box
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_4.setObjectName("groupBox_4")
        self.groupBox_4.setMinimumSize(QtCore.QSize(200, 180))
        self.groupBox_4.setMaximumSize(QtCore.QSize(200, 180))
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.storeButton = QtWidgets.QPushButton(self.groupBox_4)
        self.storeButton.setObjectName("storeButton")

        self.verticalLayout_6.addWidget(self.storeButton)
        self.trainButton = QtWidgets.QPushButton(self.groupBox_4)
        self.trainButton.setObjectName("trainButton")

        self.verticalLayout_6.addWidget(self.trainButton)
        self.testButton = QtWidgets.QPushButton(self.groupBox_4)
        self.testButton.setObjectName("testButton")

        self.verticalLayout_6.addWidget(self.testButton)
        self.verticalLayout_12.addWidget(self.groupBox_4)
        self.horizontalLayout_3.addLayout(self.verticalLayout_12)

        ## Model group box
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName("groupBox_3")
        self.groupBox_3.setMinimumSize(QtCore.QSize(500, 360))
        self.groupBox_3.setMaximumSize(QtCore.QSize(500, 360))
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget_2 = QtWidgets.QTabWidget(self.groupBox_3)
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(self.tab_3)
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser.setStyleSheet("background-color: black; color: #00FF00 ")

        self.verticalLayout.addWidget(self.textBrowser)
        self.tabWidget_2.addTab(self.tab_3, "")
        self.verticalLayout_8.addWidget(self.tabWidget_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.undoButton = QtWidgets.QPushButton(self.groupBox_3)
        self.undoButton.setObjectName("undoButton")
        self.horizontalLayout_5.addWidget(self.undoButton)
        self.resetButton_2 = QtWidgets.QPushButton(self.groupBox_3)
        self.resetButton_2.setObjectName("resetButton_2")
        self.horizontalLayout_5.addWidget(self.resetButton_2)
        self.verticalLayout_8.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_3.addWidget(self.groupBox_3)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")

        ## Event log group box
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName("groupBox_2")
        self.groupBox_2.setMinimumSize(QtCore.QSize(500, 180))
        self.groupBox_2.setMaximumSize(QtCore.QSize(500, 180))
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.tabWidget = QtWidgets.QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.tab)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.tab)
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.horizontalLayout_4.addWidget(self.textBrowser_2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tableView_3 = QtWidgets.QTableView(self.tab_2)
        self.tableView_3.setObjectName("tableView_3")
        self.verticalLayout_7.addWidget(self.tableView_3)
        self.verticalLayout_9.addWidget(self.tabWidget)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_9.addLayout(self.horizontalLayout_6)
        self.verticalLayout_10.addWidget(self.groupBox_2)

        ## Console group box
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setObjectName("groupBox_5")
        self.groupBox_5.setMinimumSize(QtCore.QSize(500, 180))
        self.groupBox_5.setMaximumSize(QtCore.QSize(500, 180))
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.groupBox_5)
        self.textBrowser_3.setObjectName("textBrowser_3")
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
        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "CNN main"))
        self.groupBox.setTitle(_translate("MainWindow", "CNN components"))
        self.convButton.setText(_translate("MainWindow", "Convolution"))
        self.poolButton.setText(_translate("MainWindow", "Pooling"))
        self.actButton.setText(_translate("MainWindow", "Activations"))
        self.linearButton.setText(_translate("MainWindow", "Linear"))
        self.dropoutButton.setText(_translate("MainWindow", "Drop-out"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Train/Test"))
        self.storeButton.setText(_translate("MainWindow", "Save as 'Model.py' file"))
        self.trainButton.setText(_translate("MainWindow", "Training"))
        self.testButton.setText(_translate("MainWindow", "Test"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Model"))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_3), _translate("MainWindow", "Sequence"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Event Log"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Log"))
        self.resetButton_2.setText(_translate("MainWindow", "Reset"))
        self.undoButton.setText(_translate("MainWindow", "UNDO"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Console"))
        self.stopButton.setText(_translate("MainWindow", "Stop"))

        # Button event call
        self.convButton.clicked.connect(self.conv)
        self.poolButton.clicked.connect(self.pool)
        self.actButton.clicked.connect(self.activation)
        self.linearButton.clicked.connect(self.linear)
        self.dropoutButton.clicked.connect(self.dropout)
        self.undoButton.clicked.connect(self.undo)
        self.resetButton_2.clicked.connect(self.reset)
        self.storeButton.clicked.connect(self.store)
        self.trainButton.clicked.connect(self.train)
        self.stopButton.clicked.connect(self.trainStop)
        self.testButton.clicked.connect(self.test)

    class Thread(QtCore.QThread):
        train_msg = QtCore.pyqtSignal(str)
        test_msg = QtCore.pyqtSignal(list)

        def __init__(self,tag='train', dataset='mnist', image_dir=None, parent=None):
            super().__init__()
            self.main=parent
            self.tag=tag
            self.dataset = dataset
            self.image_dir=image_dir

        def run(self):
            if self.dataset == 'mnist':
                mnist.run(tag=self.tag, worker=self, image_dir=self.image_dir)
            elif  self.dataset == 'cifar':
                cifar.run(tag=self.tag, worker=self, image_dir=self.image_dir)
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
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_cnnWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())