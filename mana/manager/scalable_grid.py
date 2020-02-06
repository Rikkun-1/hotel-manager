from PyQt5 import QtCore, QtGui, QtWidgets
import sip


class Scalable_grid():
	
	def __init__(self, parentGrid):
		self.parentGrid = parentGrid
		self.items = []
		self.columnCount = 2
		self.itemCount = 0
		
	def add_item(self, item):
		self.items.append(item)
		
		row = int(self.itemCount / self.columnCount)
		column = self.itemCount % self.columnCount
		
		self.parentGrid.addWidget(item, row, column)
		self.itemCount += 1
		
	def remove_item(self, item):
		self.items.remove(item)
		
		trash = item.children()[0]
		if trash is not None:
			while trash.count():
				item = trash.takeAt(0)
				widget = item.widget()
				if widget is not None:
					widget.deleteLater()
				else:
					self.deleteLayout(item.trash)
			sip.delete(trash)
			
		self.itemCount -= 1
		self.recalculate()
	
	def recalculate(self):
		row = 0
		column = 0
		for i in self.items:
			if(column == self.columnCount-1): 
				self.parentGrid.addWidget(i, row, column)
				column = 0
				row += 1
			else: 
				self.parentGrid.addWidget(i, row, column)
				column += 1