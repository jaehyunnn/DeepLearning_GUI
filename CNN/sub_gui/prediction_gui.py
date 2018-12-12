# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Prediction_result.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *

class Ui_PredSubbox(QWidget):
    pred_param = QtCore.pyqtSignal(str)

    def setupUi(self, PredSubbox):
        PredSubbox.setObjectName("PredSubbox")
        PredSubbox.resize(448, 308)
        self.centralwidget = QtWidgets.QWidget(PredSubbox)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(20, 40, 202, 221))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2, 0, QtCore.Qt.AlignHCenter)
        self.label = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(270, 110, 151, 91))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.verticalLayoutWidget_2)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser = QtWidgets.QTextBrowser(self.verticalLayoutWidget_2)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout_2.addWidget(self.textBrowser)
        self.verticalLayoutWidget.raise_()
        self.label.raise_()
        self.verticalLayoutWidget_2.raise_()
        self.label_3.raise_()
        self.menubar = QtWidgets.QMenuBar(PredSubbox)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 448, 21))
        self.menubar.setObjectName("menubar")
        self.statusbar = QtWidgets.QStatusBar(PredSubbox)
        self.statusbar.setObjectName("statusbar")

        self.retranslateUi(PredSubbox)
        QtCore.QMetaObject.connectSlotsByName(PredSubbox)

    def retranslateUi(self, PredSubbox):
        _translate = QtCore.QCoreApplication.translate
        PredSubbox.setWindowTitle(_translate("PredSubbox", "Prediction"))
        self.label_2.setText(_translate("PredSubbox", "Input Image"))
        self.label_3.setText(_translate("PredSubbox", "Predicted class"))
        self.textBrowser.setHtml(_translate("PredSubbox", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Gulim\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PredSubbox = QtWidgets.QWidget()
    ui = Ui_PredSubbox()
    ui.setupUi(PredSubbox)
    PredSubbox.show()
    sys.exit(app.exec_())

