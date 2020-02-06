from PyQt5 import QtCore, QtGui, QtWidgets
import sip


class Client(object):

	def __init__(self, full_name, passport, comment):
		self.__full_name = full_name
		self.__passport = passport
		self.__settled_into = []
		
		self.gridframe = QtWidgets.QFrame()
		self.gridLayout = QtWidgets.QGridLayout(self.gridframe)
		
		nameLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(nameLabel, 0, 0)
		nameLabel.setText("ФИО:")
		
		fullName = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(fullName, 0, 1)
		fullName.setText(full_name)
		
		passportLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(passportLabel, 1, 0)
		passportLabel.setText("Пасспорт:")
		
		passportVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(passportVal, 1, 1)
		passportVal.setText(str(passport))
		
		settledLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(settledLabel, 2, 0)
		settledLabel.setText("Заселен в:")
		
		self.settledVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(self.settledVal, 2, 1)
		self.settledVal.setText(str(self.__settled_into))
		
		commentLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(commentLabel, 3, 0)
		commentLabel.setText("Комментарий")
		
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridframe)
		self.gridLayout.addWidget(self.commentVal, 3, 1)
		self.commentVal.setPlainText(comment)
		
		self.btdDelete = QtWidgets.QPushButton(self.gridframe)
		self.gridLayout.addWidget(self.btdDelete, 4, 0)
		self.btdDelete.setText("Удалить")
		
		self.btnSettle = QtWidgets.QPushButton(self.gridframe)
		self.gridLayout.addWidget(self.btnSettle, 4, 1)
		self.btnSettle.setText("Заселить")
	
		
	def __str__(self):
		a = self.__full_name
		b = str(self.__passport)
		c = self.comment
		d = str(self.__settled_into)
		stats = [a, b, c, d]
		return ' '.join(stats)
		
	@property
	def full_name(self):
		return self.__full_name
	
	@property
	def passport(self):
		return self.__passport
	
	@property
	def settled_into(self):
		return self.__settled_into
	
	def settle(self, room_id):
		self.__settled_into.append(room_id)
		self.settledVal.setText(str(self.__settled_into))
	
	def evict(self, room_id):
		self.__settled_into.remove(room_id)
		self.settledVal.setText(str(self.__settled_into))
	
	@property 
	def comment(self):
		return self.commentVal.toPlainText()
		
	@comment.setter	
	def comment(self, comment):
		self.commentVal.setPlainText(comment)