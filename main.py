# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './BPomron.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

import pyqtgraph as pg
import numpy as np

VENDOR_ID = 0x0590 #
PRODUCT_ID = 0x0090 #

import hid
import time

cmd_init=[ 0x02, 0x08, 0x00, 0x00, 0x00, 0x00, 0x10, 0x00, 0x18 ] # + [0]*55
cmd_data= [ 0x02, 0x08, 0x01, 0x00, 0x02, 0xac, 0x28, 0x00, 0x8f ] # + [0]*55
cmd_done = [0x02, 0x08, 0x0f, 0x00, 0x00, 0x00, 0x00, 0x00, 0x07 ] #+ [0]*55
cmd_fail = [0x02, 0x08, 0x0f, 0x0f, 0x0f, 0x0f, 0x00, 0x00, 0x08] #+ [0]*55

segundos=0.2
jump=14
sysList = []
diasList = []
pulseList = []
h = hid.device()

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 705)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 991, 641))
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setGeometry(QtCore.QRect(10, 10, 961, 591))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        #self.graphicsView = QtWidgets.QGraphicsView(self.widget)
        self.graphicsView = pg.PlotWidget(self.widget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout.addWidget(self.graphicsView)
        self.btnRecords = QtWidgets.QPushButton(self.widget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.btnRecords.setFont(font)
        self.btnRecords.setObjectName("btnRecords")
        self.verticalLayout.addWidget(self.btnRecords)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.groupBox = QtWidgets.QGroupBox(self.tab_2)
        self.groupBox.setGeometry(QtCore.QRect(30, 20, 921, 571))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.widget1 = QtWidgets.QWidget(self.groupBox)
        self.widget1.setGeometry(QtCore.QRect(20, 30, 371, 311))
        self.widget1.setObjectName("widget1")
        self.gridLayout = QtWidgets.QGridLayout(self.widget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lcdNumber = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber.setDigitCount(3)
        self.lcdNumber.setObjectName("lcdNumber")
        self.gridLayout.addWidget(self.lcdNumber, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_2.setDigitCount(3)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.gridLayout.addWidget(self.lcdNumber_2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.widget1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.lcdNumber_3 = QtWidgets.QLCDNumber(self.widget1)
        self.lcdNumber_3.setDigitCount(3)
        self.lcdNumber_3.setObjectName("lcdNumber_3")
        self.gridLayout.addWidget(self.lcdNumber_3, 2, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.widget1)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab_2, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.retranslateUi(MainWindow)
        self.btnRecords.clicked.connect(self.btn_clk)


        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def btn_clk(self):
        #L = [1, 2, 3, 4, 5,6,7,8]

        [ slist, dlist, plist,a,b,c]= self.omron()

        L = np.arange(1, np.size(slist))
        slist.pop()
        print("L")
        print(L)
        print(slist)
        # pg.plot(L)#this line plots in a new window
        self.graphicsView.plot(L, slist)

    def buildCRC(self,data):
        crc = 0
        size = data[1] - 1
        while not size == 0:
            crc = crc ^ data[size]
            size = size - 1
        return crc

    def readOmron(self):
        # read back the answer
        print("Read the data")
        d = h.read(64)
        print(d)
        return d

    def getBPvalues(self,buffer):
        for i in range(0, 3):
            sistolica = buffer[8 + i * jump] + 25
            diastolica = buffer[7 + i * jump]
            pulso = buffer[10 + i * jump]
            print(sistolica)
            print(diastolica)
            print(pulso)
            print('')
            sysList.append(sistolica)
            diasList.append(diastolica)
            pulseList.append(pulso)
            if sistolica == 280 and diastolica == 255 and pulso == 255:
                break
        return [sistolica, diastolica, pulso, sysList, diasList, pulseList]

    def showDialog(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("USB Not Connected")
        msgBox.setWindowTitle("USB Conncetion error")
        msgBox.setStandardButtons(QMessageBox.Ok)  # | QMessageBox.Cancel)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
    def showDialog2(self):
        msgBox = QMessageBox()
        msgBox.setIcon(QMessageBox.Critical)
        msgBox.setText("START OMRON")
        msgBox.setWindowTitle("USB Conncetion error")
        msgBox.setStandardButtons(QMessageBox.Ok)  # | QMessageBox.Cancel)
        # msgBox.buttonClicked.connect(msgButtonClick)

        returnValue = msgBox.exec()
        if returnValue == QMessageBox.Ok:
            print('OK clicked')
    def omron(self):
        for d in hid.enumerate():
            keys = list(d.keys())
            keys.sort()
            # for key in keys:
            # print("%s : %s" % (key, d[key]))

        # try opening a device, then perform write and read

        try:
            print("Opening the device")
            addr = 0x02AC


            h.open(VENDOR_ID, PRODUCT_ID)  # TREZOR VendorID/ProductID

            print("Manufacturer: %s" % h.get_manufacturer_string())
            print("Product: %s" % h.get_product_string())
            # print("Serial No: %s" % h.get_serial_number_string())

            # enable non-blocking mode
            h.set_nonblocking(1)

            print("crc")
            print(self.buildCRC(cmd_data))
            # write some data to the device
            print("Write the data")

            h.write(cmd_init)
            # wait
            time.sleep(segundos)
            rc1 = self.readOmron()
            time.sleep(segundos)
            for i in range(0, 70):
                cmd_data[4] = addr >> 8;
                cmd_data[5] = addr & 0xFF;
                cmd_data[8] = self.buildCRC(cmd_data);
                h.write(cmd_data)
                # wait
                time.sleep(segundos)
                rc2 = self.readOmron()
                # wait
                time.sleep(segundos)
                addr = addr + 42
                if not rc2 == []:
                    [sys, dias, pulse, slist, dlist, plist] = self.getBPvalues(rc2)
                    if sys == 280 and dias == 255 and pulse == 255:
                        break
                else:
                    self.showDialog2()
                    print("Closing the device")
                    h.close()
                    return 0
                    break
            print(slist)
            print(dlist)
            print(plist)
            print("last values")
            last = len(slist) - 2
            print(slist[last])
            print(dlist[last])
            print(plist[last])
            if rc2 == []:
                print("fail")
                h.write(cmd_fail)
                time.sleep(segundos)
                rc3 = self.readOmron()

            else:
                print("done")
                h.write(cmd_done)
                time.sleep(segundos)
                rc3 = self.readOmron()

            print("Closing the device")
            h.close()
            return[ slist, dlist, plist,slist[last],dlist[last],plist[last]]

        except IOError as ex:
            print(ex)
            self.showDialog()
            print("You probably don't have the hard coded device. Update the hid.device line")
            print("in this script with one from the enumeration list output above and try again.")

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "BP DIAGNOSTIC"))
        self.btnRecords.setText(_translate("MainWindow", "Get Last Records"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Last Records"))
        self.groupBox.setTitle(_translate("MainWindow", "Last Record"))
        self.label.setText(_translate("MainWindow", "Systolic"))
        self.label_2.setText(_translate("MainWindow", "Distolic"))
        self.label_3.setText(_translate("MainWindow", "Pulse"))
        self.pushButton.setText(_translate("MainWindow", "Get Last Record"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Last Record"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

