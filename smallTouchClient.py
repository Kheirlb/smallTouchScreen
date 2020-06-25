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
		self.lamp_setting = 0
		self.is_lamp_on = False

	def initUI(self):
		print('initUI')

		self.lamp_sl.sliderMoved.connect(self.change_lamp_brightness)
		self.lamp_but.clicked.connect(self.toggle_lamp)

	def change_lamp_brightness(self):
		self.lamp_le.setText(str(self.lamp_sl.value()) + '%')
		if self.lamp_sl.value() < 1:
			self.is_lamp_on = False
		else:
			self.is_lamp_on = True

	def toggle_lamp(self):
		self.is_lamp_on = not self.is_lamp_on
		if self.is_lamp_on:
			self.lamp_setting = 100
		else:
			self.lamp_setting = 0
		self.lamp_le.setText(str(self.lamp_setting) + '%')
		self.lamp_sl.setValue(self.lamp_setting)

def main():
    app = QtWidgets.QApplication(sys.argv)
    main = Window()
    main.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
