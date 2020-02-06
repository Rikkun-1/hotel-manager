import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
import sip

from . import find
from .scalable_grid import Scalable_grid
from .database import Database
from .client import Client
from .room import Room
from .resident import Resident
from .dialogs import NewClientDialog, NewRoomDialog, WrongInput, DateDialog


class Ui_MainWindow(object):

	def btnDeleteClient(self):
		sender = self.sender()
		index = self.clients.items.index(sender.parent())
		residentIndexes = find.find_residents_by_passport(self.database.residents, self.database.clients[index].passport)
		count = 0
		for i in residentIndexes:
			i -= count
			self.residents.remove_item(self.database.residents[i].gridframe)
			del self.database.residents[i]
			count += 1
		del self.database.clients[index]
		self.clients.remove_item(sender.parent())
		
	def btnDeleteRoom(self):
		sender = self.sender()
		index = self.rooms.items.index(sender.parent())
		residentIndexes = find.find_residents_by_id(self.database.residents, self.database.rooms[index].id)
		count = 0
		for i in residentIndexes:
			i -= count
			self.residents.remove_item(self.database.residents[i].gridframe)
			del self.database.residents[i]
			count += 1
		del self.database.rooms[index]
		self.rooms.remove_item(sender.parent())
		
	def btnDeleteResident(self):
		sender = self.sender()
		index = self.residents.items.index(sender.parent())
		del self.database.residents[index]
		self.residents.remove_item(sender.parent())
	
	def add_new_client(self):
		dialog = NewClientDialog()
		data = dialog.exec_()
		if(data):
			if find.find_by_passport(self.database.clients, data[1]) != -1:
				warning = WrongInput(['Клиент с таким пасспортом уже существует'])
				warning.exec_()
			else:
				client = Client(data[0], data[1], data[2])
				client.btdDelete.clicked.connect(self.btnDeleteClient)
				client.btnSettle.clicked.connect(self.client_settle)
				self.clients.add_item(client.gridframe)
				self.database.clients.append(client)
			
	def add_new_room(self):
		dialog = NewRoomDialog()
		data = dialog.exec_()
		if(data):
			if find.find_by_id(self.database.rooms, data[0]) != -1:
				warning = WrongInput(['Комната с таким номером уже существует'])
				warning.exec_()
			else:
				room = Room(data[0], data[1], data[2], data[3], data[4])
				room.btdDelete.clicked.connect(self.btnDeleteRoom)
				room.btnSettle.clicked.connect(self.room_settle)
				self.rooms.add_item(room.gridframe)
				self.database.rooms.append(room)
					
	def client_settle(self):	
		sender = self.sender()
		clientIndex = self.clients.items.index(sender.parent())
		id, ok = QtWidgets.QInputDialog.getInt(self, "Заселение",
				"Номер комнаты:")
		if ok:
			client = self.database.clients[clientIndex]
			roomIndex = find.find_by_id(self.database.rooms, id)
			if roomIndex == -1:
				warning = WrongInput(['Нет комнаты с таким номером'])
				warning.exec_()
			else:
				dialog = DateDialog()
				data = dialog.exec_()
				
				client = self.database.clients[clientIndex]
				room = self.database.rooms[roomIndex]
			
				if len(room.clients) == room.capacity:
					warning = WrongInput(['В комнате больше нет мест'])
					warning.exec_()
				elif room.id in client.settled_into: 
					if client.passport in room.clients:
						warning = WrongInput(['Постоялец уже заселен в эту комнату'])
						warning.exec_()
				else:
					resident = Resident(client, room, data[0], data[1], '')
					resident.btdDelete.clicked.connect(self.btnDeleteResident)
					self.residents.add_item(resident.gridframe)
					self.database.residents.append(resident)
			
	def room_settle(self):	
		sender = self.sender()
		roomIndex = self.rooms.items.index(sender.parent())
		passport, ok = QtWidgets.QInputDialog.getInt(self, "Заселение",
				"Пасспорт клиента:")
		if ok:
			room = self.database.rooms[roomIndex]
			clientIndex = find.find_by_passport(self.database.clients, passport)
			if clientIndex == -1:
				warning = WrongInput(['Нет клиента с таким паспортом'])
				warning.exec_()
			else:
				dialog = DateDialog()
				data = dialog.exec_()
				
				client = self.database.clients[clientIndex]
				room = self.database.rooms[roomIndex]
			
				if len(room.clients) == room.capacity:
					warning = WrongInput(['В комнате больше нет мест'])
					warning.exec_()
				elif room.id in client.settled_into: 
					if client.full_name in room.clients:
						warning = WrongInput(['Постоялец уже заселен в эту комнату'])
						warning.exec_()
				else:
					resident = Resident(client, room, data[0], data[1], '')
					resident.btdDelete.clicked.connect(self.btnDeleteResident)
					self.residents.add_item(resident.gridframe)
					self.database.residents.append(resident)
	
	def setupUi(self, MainWindow):
		MainWindow.setObjectName("MainWindow")
		MainWindow.resize(900, 600)
		MainWindow.setMinimumSize(QtCore.QSize(400, 350))
		
		self.centralwidget = QtWidgets.QWidget(MainWindow)
		MainWindow.setCentralWidget(self.centralwidget)	
		self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
		
		self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
		self.tab_1 = QtWidgets.QWidget()
		self.tabWidget.addTab(self.tab_1, "Клиенты")
		self.tab_2 = QtWidgets.QWidget()
		self.tabWidget.addTab(self.tab_2, "Комнаты")
		self.tab_3 = QtWidgets.QWidget()
		self.tabWidget.addTab(self.tab_3, "Постояльцы")
		self.verticalLayout.addWidget(self.tabWidget)
		
		self.verticalLayout_1 = QtWidgets.QVBoxLayout(self.tab_1)
		self.scrollArea_1 = QtWidgets.QScrollArea(self.tab_1)
		self.scrollArea_1.setWidgetResizable(True)
		self.verticalLayout_1.addWidget(self.scrollArea_1)
		self.scrollAreaWidgetContents_1 = QtWidgets.QWidget()
		self.scrollArea_1.setWidget(self.scrollAreaWidgetContents_1)
		self.gridLayout_1 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_1)
		self.btnNewClient = QtWidgets.QPushButton('Добавить нового клиента', self.tab_1)
		self.verticalLayout_1.addWidget(self.btnNewClient)
		self.btnNewClient.clicked.connect(self.add_new_client)
		
		self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tab_2)
		self.scrollArea_2 = QtWidgets.QScrollArea(self.tab_2)
		self.scrollArea_2.setWidgetResizable(True)
		self.verticalLayout_2.addWidget(self.scrollArea_2)
		self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
		self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_2)
		self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_2)
		self.btnNewRoom = QtWidgets.QPushButton('Добавить новую комнату', self.tab_2)
		self.verticalLayout_2.addWidget(self.btnNewRoom)
		self.btnNewRoom.clicked.connect(self.add_new_room)
		
		self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tab_3)
		self.scrollArea_3 = QtWidgets.QScrollArea(self.tab_3)
		self.scrollArea_3.setWidgetResizable(True)
		self.verticalLayout_3.addWidget(self.scrollArea_3)
		self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
		self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
		self.gridLayout_3 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
			
		self.clients = Scalable_grid(self.gridLayout_1)
		self.rooms = Scalable_grid(self.gridLayout_2)
		self.residents = Scalable_grid(self.gridLayout_3)
		
		self.database = Database()
		
		for client in self.database.clients:
			client.btdDelete.clicked.connect(self.btnDeleteClient)
			client.btnSettle.clicked.connect(self.client_settle)
			self.clients.add_item(client.gridframe)
		
		for room in self.database.rooms:
			room.btdDelete.clicked.connect(self.btnDeleteRoom)
			room.btnSettle.clicked.connect(self.room_settle)
			self.rooms.add_item(room.gridframe)
		
		for resident in self.database.residents:
			resident.btdDelete.clicked.connect(self.btnDeleteResident)
			self.residents.add_item(resident.gridframe)
			
		MainWindow.setWindowTitle("Менеджер отеля")
		QtCore.QMetaObject.connectSlotsByName(MainWindow)	
