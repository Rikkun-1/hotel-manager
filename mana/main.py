import sys 
import datetime

from PyQt5 import QtWidgets

import manager.interface  as interface


class interface(QtWidgets.QMainWindow, interface.Ui_MainWindow):

	def __init__(self):
		super().__init__()
		self.setupUi(self)  
	
	def resizeEvent(self, *args):
		columnCount = int(self.width() / 400)
		self.clients.columnCount = columnCount
		self.rooms.columnCount = columnCount
		self.residents.columnCount = columnCount
		self.clients.recalculate()
		self.rooms.recalculate()
		self.residents.recalculate()


def main():
	app = QtWidgets.QApplication(sys.argv)  
	window = interface()  
	window.show()  
	app.exec_()  
	window.database.save_data()


if __name__ == '__main__': 
	main()  