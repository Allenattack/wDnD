# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'startup.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_startup(object):
    def setupUi(self, startup):
        startup.setObjectName("startup")
        startup.resize(430, 250)
        self.centralwidget = QtWidgets.QWidget(startup)
        self.centralwidget.setObjectName("centralwidget")
        startup.setCentralWidget(self.centralwidget)

        self.retranslateUi(startup)
        QtCore.QMetaObject.connectSlotsByName(startup)

    def retranslateUi(self, startup):
        _translate = QtCore.QCoreApplication.translate
        startup.setWindowTitle(_translate("startup", "MainWindow"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    startup = QtWidgets.QMainWindow()
    ui = Ui_startup()
    ui.setupUi(startup)
    startup.show()
    sys.exit(app.exec_())

