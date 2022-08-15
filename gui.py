# Form implementation generated from reading ui file 'test.ui'
#
# Created by: PyQt6 UI code generator 6.3.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QLabel, QListWidgetItem, QPushButton, QApplication
import main

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(406, 567)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(0, 55, 401, 471))
        self.listWidget.setObjectName("listWidget")
        # font = QtGui.QFont()
        # font.setPointSize(12)
        # font.setBold(True)
        # for q in main.finalFoodItems:
        #     y = 0
        #     for x in q:
        #         item = QListWidgetItem(x)
        #         if y == 0:
        #             item.setFont(font)
        #         self.listWidget.addItem(item)
        #         y += 1
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(0, 30, 401, 21))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.BreakfastButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.BreakfastButton.setObjectName("BreakfastButton")
        self.horizontalLayout_2.addWidget(self.BreakfastButton)
        self.LunchButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.LunchButton.setObjectName("LunchButton")
        self.horizontalLayout_2.addWidget(self.LunchButton)
        self.DinnerButton = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.DinnerButton.setObjectName("DinnerButton")
        self.horizontalLayout_2.addWidget(self.DinnerButton)
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 401, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.HampButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.HampButton.setObjectName("HampButton")
        self.horizontalLayout.addWidget(self.HampButton)
        self.BerkButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.BerkButton.setObjectName("BerkButton")
        self.horizontalLayout.addWidget(self.BerkButton)
        self.FrankButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.FrankButton.setObjectName("FrankButton")
        self.horizontalLayout.addWidget(self.FrankButton)
        self.WorcesterButton = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.WorcesterButton.setObjectName("WorcesterButton")
        self.horizontalLayout.addWidget(self.WorcesterButton)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 406, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.HampButton.clicked.connect(self.hampshireButtonClicked)
        self.BerkButton.clicked.connect(self.berkshireButtonClicked)
        self.FrankButton.clicked.connect(self.franklinButtonClicked)
        self.WorcesterButton.clicked.connect(self.worcesterButtonClicked)
        self.BreakfastButton.clicked.connect(self.breakfastButtonClicked)
        self.LunchButton.clicked.connect(self.lunchButtonClicked)
        self.DinnerButton.clicked.connect(self.dinnerButtonClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.BreakfastButton.setText(_translate("MainWindow", "Breakfast"))
        self.LunchButton.setText(_translate("MainWindow", "Lunch"))
        self.DinnerButton.setText(_translate("MainWindow", "Dinner"))
        self.HampButton.setText(_translate("MainWindow", "Hampshire"))
        self.BerkButton.setText(_translate("MainWindow", "Berkshire"))
        self.FrankButton.setText(_translate("MainWindow", "Franklin"))
        self.WorcesterButton.setText(_translate("MainWindow", "Worcester"))

    DCSelection = "none"
    menuSelection = "none"

    def hampshireButtonClicked(self):
        print("hamp button clicked")
        self.DCSelection = "hamp"


    def berkshireButtonClicked(self):
        print("Clicked")
        self.DCSelection = "berk"

    def franklinButtonClicked(self):
        print("clicked")
        self.DCSelection = "frank"

    def worcesterButtonClicked(self):
        print("clicked")
        self.DCSelection = "woo"

    def breakfastButtonClicked(self):
        if self.DCSelection == "hamp":
            self.menuSelection = main.hampshireBreakfast
        if self.DCSelection == "berk":
            self.menuSelection = main.berkshireBreakfast
        if self.DCSelection == "frank":
            self.menuSelection = main.franklinBreakfast
        if self.DCSelection == "woo":
            self.menuSelection = main.worcesterBreakfast
        self.printData()

    def lunchButtonClicked(self):
        if self.DCSelection == "hamp":
            self.menuSelection = main.hampshireLunch
        if self.DCSelection == "berk":
            self.menuSelection = main.berkshireLunch
        if self.DCSelection == "frank":
            self.menuSelection = main.franklinLunch
        if self.DCSelection == "woo":
            self.menuSelection = main.worcesterLunch
        self.printData()

    def dinnerButtonClicked(self):
        if self.DCSelection == "hamp":
            self.menuSelection = main.hampshireDinner
        if self.DCSelection == "berk":
            self.menuSelection = main.berkshireDinner
        if self.DCSelection == "frank":
            self.menuSelection = main.franklinDinner
        if self.DCSelection == "woo":
            self.menuSelection = main.worcesterDinner
        self.printData()

    font = QtGui.QFont()
    font.setPointSize(12)
    font.setBold(True)

    def printData(self):
        print("breakfast button clicked")
        self.listWidget.clear()
        for q in self.menuSelection:
            y = 0
            for x in q:
                item = QListWidgetItem(x)
                if y == 0:
                    item.setFont(self.font)
                self.listWidget.addItem(item)
                y += 1


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())