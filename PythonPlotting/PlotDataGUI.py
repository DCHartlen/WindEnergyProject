# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PlotDataGUI.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1021, 630)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.mainPlotWindow = PlotWidget(self.centralwidget)
        self.mainPlotWindow.setMinimumSize(QtCore.QSize(756, 571))
        self.mainPlotWindow.setObjectName("mainPlotWindow")
        self.gridLayout.addWidget(self.mainPlotWindow, 0, 0, 1, 1)
        self.verticalFrame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalFrame.sizePolicy().hasHeightForWidth())
        self.verticalFrame.setSizePolicy(sizePolicy)
        self.verticalFrame.setMinimumSize(QtCore.QSize(241, 0))
        self.verticalFrame.setObjectName("verticalFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 60, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMaximumSize(QtCore.QSize(450, 40))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.maxVoltsOut = QtWidgets.QLineEdit(self.verticalFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.maxVoltsOut.sizePolicy().hasHeightForWidth())
        self.maxVoltsOut.setSizePolicy(sizePolicy)
        self.maxVoltsOut.setMaximumSize(QtCore.QSize(450, 40))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.maxVoltsOut.setFont(font)
        self.maxVoltsOut.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.maxVoltsOut.setObjectName("maxVoltsOut")
        self.verticalLayout.addWidget(self.maxVoltsOut)
        spacerItem1 = QtWidgets.QSpacerItem(17, 357, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.startPlotting = QtWidgets.QPushButton(self.verticalFrame)
        self.startPlotting.setMaximumSize(QtCore.QSize(450, 23))
        self.startPlotting.setObjectName("startPlotting")
        self.horizontalLayout.addWidget(self.startPlotting)
        self.stopPlotting = QtWidgets.QPushButton(self.verticalFrame)
        self.stopPlotting.setMaximumSize(QtCore.QSize(450, 23))
        self.stopPlotting.setObjectName("stopPlotting")
        self.horizontalLayout.addWidget(self.stopPlotting)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.resetPlots = QtWidgets.QPushButton(self.verticalFrame)
        self.resetPlots.setMaximumSize(QtCore.QSize(450, 23))
        self.resetPlots.setObjectName("resetPlots")
        self.verticalLayout.addWidget(self.resetPlots)
        self.gridLayout.addWidget(self.verticalFrame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1021, 21))
        self.menuBar.setObjectName("menuBar")
        self.menuAbout = QtWidgets.QMenu(self.menuBar)
        self.menuAbout.setObjectName("menuAbout")
        self.menuOptions = QtWidgets.QMenu(self.menuBar)
        self.menuOptions.setObjectName("menuOptions")
        MainWindow.setMenuBar(self.menuBar)
        self.actionInformation = QtWidgets.QAction(MainWindow)
        self.actionInformation.setObjectName("actionInformation")
        self.actionExit_App = QtWidgets.QAction(MainWindow)
        self.actionExit_App.setObjectName("actionExit_App")
        self.actionHelp = QtWidgets.QAction(MainWindow)
        self.actionHelp.setObjectName("actionHelp")
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.actionTest = QtWidgets.QAction(MainWindow)
        self.actionTest.setObjectName("actionTest")
        self.actionTest_2 = QtWidgets.QAction(MainWindow)
        self.actionTest_2.setObjectName("actionTest_2")
        self.actionSelectCOMPort = QtWidgets.QAction(MainWindow)
        self.actionSelectCOMPort.setObjectName("actionSelectCOMPort")
        self.menuAbout.addAction(self.actionHelp)
        self.menuAbout.addAction(self.actionAbout)
        self.menuOptions.addAction(self.actionSelectCOMPort)
        self.menuBar.addAction(self.menuOptions.menuAction())
        self.menuBar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Plot Wind Turbine Output"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Maximum Voltage</span></p></body></html>"))
        self.startPlotting.setText(_translate("MainWindow", "Start"))
        self.stopPlotting.setText(_translate("MainWindow", "Stop"))
        self.resetPlots.setText(_translate("MainWindow", "Reset"))
        self.menuAbout.setTitle(_translate("MainWindow", "About"))
        self.menuOptions.setTitle(_translate("MainWindow", "Options"))
        self.actionInformation.setText(_translate("MainWindow", "Information"))
        self.actionExit_App.setText(_translate("MainWindow", "Exit App"))
        self.actionHelp.setText(_translate("MainWindow", "Help"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
        self.actionTest.setText(_translate("MainWindow", "test"))
        self.actionTest_2.setText(_translate("MainWindow", "test"))
        self.actionSelectCOMPort.setText(_translate("MainWindow", "Select COM Port"))

from pyqtgraph import PlotWidget
