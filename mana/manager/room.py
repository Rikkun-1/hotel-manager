from PyQt5 import QtCore, QtGui, QtWidgets
import sip


class Room:

	def __init__(self, id, capacity, comfort, payment, comment = ''):
		self.__id = id
		self.__capacity = capacity
		self.__comfort = comfort
		self.__payment = payment
		self.__clients = []
		
		self.gridframe = QtWidgets.QFrame()
		gridLayout = QtWidgets.QGridLayout(self.gridframe)

		idLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(idLabel, 0, 0)
		idLabel.setText("Номер:")
		
		idVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(idVal, 0, 1)
		idVal.setText(str(id))
		
		capacityLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(capacityLabel, 1, 0)
		capacityLabel.setText("Вместимость:")
		
		capacityVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(capacityVal, 1, 1)
		capacityVal.setText(str(capacity))
		
		comfortLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(comfortLabel, 2, 0)
		comfortLabel.setText("Комфорт:")
		
		comfortVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(comfortVal, 2, 1)
		comfortVal.setText(str(comfort))
		
		paymentLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(paymentLabel, 3, 0)
		paymentLabel.setText("Оплата за сутки:")
		
		paymentVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(paymentVal, 3, 1)
		paymentVal.setText(str(payment))
		
		clientsLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(clientsLabel, 4, 0)
		clientsLabel.setText("Клиенты:")
		
		self.clientsVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(self.clientsVal, 4, 1)
		self.clientsVal.setText(str(self.clients))
		
		commentLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(commentLabel, 5, 0)
		commentLabel.setText("Комментарий")
		
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridframe)
		gridLayout.addWidget(self.commentVal, 5, 1)
		self.commentVal.setPlainText(comment)
		
		self.btdDelete = QtWidgets.QPushButton(self.gridframe)
		gridLayout.addWidget(self.btdDelete, 6, 0)
		self.btdDelete.setText("Удалить")
		
		self.btnSettle = QtWidgets.QPushButton(self.gridframe)
		gridLayout.addWidget(self.btnSettle, 6, 1)
		self.btnSettle.setText("Заселить")
			  
	@property
	def id(self):
		return self.__id
		
	@id.setter
	def id(self, id):
		self.__id = id
		idVal.setText(id)
			
	@property
	def capacity(self):
		return self.__capacity
 
	@capacity.setter
	def capacity(self, capacity):
		self.__capacity = capacity
		capacityVal.setText(capacity)
			
	@property
	def comfort(self):
		return self.__comfort
 
	@comfort.setter
	def comfort(self, comfort):
		self.__comfort = comfort
		comfortVal.setText(comfort)
	
	@property
	def payment(self):
		return self.__payment
 
	@payment.setter
	def payment(self, payment):
		self.__payment = payment
		paymentVal.setText(payment)
	
	@property 
	def comment(self):
		return self.commentVal.toPlainText()
	
	@comment.setter	
	def comment(self, comment):
		self.commentVal.setPlainText(comment)
	
	@property
	def clients(self):
		return self.__clients
		
	def settle(self, client_passport):
		self.__clients.append(client_passport)
		self.clientsVal.setText(str(self.__clients))
	
	def evict(self, client_passport):
		self.__clients.remove(client_passport)
		self.clientsVal.setText(str(self.__clients))
	
	def __str__(self):
		a = str(self.__id)
		b = str(self.__capacity)
		c = str(self.__comfort)
		d = str(self.__payment)
		e = str(self.__clients)
		f = self.comment
		stats = [a, b, c, d, e, f]
		return ' '.join(stats)