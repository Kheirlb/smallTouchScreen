#!/usr/bin/python3
import sys
import time
from PyQt5 import QtCore, QtWidgets, QtGui, Qt, uic
# import paho.mqtt.client as mqtt
# import paho.mqtt.publish as publish
from PyQt5.QtGui import QTextCursor

print('Imported Packages and Starting Launch VI')

qtCreatorFile = "smallTouch.ui"  # Enter file here.

Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)

num = 0

class Window(QtWidgets.QMainWindow, Ui_MainWindow):
	def __init__(self):
		QtWidgets.QMainWindow.__init__(self)
		Ui_MainWindow.__init__(self)
		self.setupUi(self)
		# self.showMaximized()
		self.initUI()

	def initUI(self):
		print('initUI')

		self.but.clicked.connect(self.countUp)

	def countUp(self):
		global num
		num = num + 1
		self.line.setText(str(num))

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
