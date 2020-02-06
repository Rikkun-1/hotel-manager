import datetime
import copy

from PyQt5 import QtCore, QtGui, QtWidgets
import sip

from .client import Client
from .room import Room
from .dialogs import show_client, show_room


class Resident():
	
	def __init__(self, client, room, settlement, eviction, comment = ''):
		self.client = client
		self.room = room
		self.__settlement = settlement
		self.__eviction = eviction
		
		self.client.settle(self.room.id)
		self.room.settle(client.passport)
		
		self.gridframe = QtWidgets.QFrame()
		self.gridLayout = QtWidgets.QGridLayout(self.gridframe)
		
		clientLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(clientLabel, 0, 0)
		clientLabel.setText("Клиент:")
		
		self.btdClient = QtWidgets.QPushButton(self.gridframe)
		self.gridLayout.addWidget(self.btdClient, 0, 1)
		self.btdClient.setText(client.full_name)
		self.btdClient.clicked.connect(self.show_client)
			
		roomLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(roomLabel, 1, 0)
		roomLabel.setText('Комната:')
			
		self.btdRoom = QtWidgets.QPushButton(self.gridframe)
		self.gridLayout.addWidget(self.btdRoom, 1, 1)
		self.btdRoom.setText(str(room.id))
		self.btdRoom.clicked.connect(self.show_room)
			
		settlementLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(settlementLabel, 2, 0)
		settlementLabel.setText("Дата заселения:")
			
		self.settlementVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(self.settlementVal, 2, 1)
		self.settlementVal.setText(str(settlement))
			
		evictionLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(evictionLabel, 3, 0)
		evictionLabel.setText("Дата выселения:")
			
		self.evictionVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(self.evictionVal, 3, 1)
		self.evictionVal.setText(str(eviction))
			
		commentLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(commentLabel, 4, 0)
		commentLabel.setText("Комментарий")
			
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridframe)
		self.gridLayout.addWidget(self.commentVal, 4, 1)
		self.commentVal.setPlainText(comment)
			
		self.btdDelete = QtWidgets.QPushButton(self.gridframe)
		self.gridLayout.addWidget(self.btdDelete, 5, 0)
		self.btdDelete.setText("Выселить")
	
	@property 
	def comment(self):
		return self.commentVal.toPlainText()
	
	@property 
	def settlement(self):
		return self.__settlement
		
	@property 
	def eviction(self):
		return self.__eviction
		
	def show_client(self):
		dialog = show_client(self.client)
		dialog.show()
		dialog.exec_()
		
	def show_room(self):
		dialog = show_room(self.room)
		dialog.show()
		dialog.exec_()
		
	def __del__(self):
		self.client.evict(self.room.id)
		self.room.evict(self.client.passport)