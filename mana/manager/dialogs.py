import datetime

from PyQt5 import QtCore, QtGui, QtWidgets
import sip


class NewClientDialog(QtWidgets.QDialog):

	def __init__(self, parent = None):
		super(NewClientDialog, self).__init__(parent)
		self.initUI()
		
	def initUI(self):
		self.resize(420, 200)
		self.setFixedSize(420, 200)
		self.setWindowTitle("Новый клиент")
		self.gridLayoutWidget = QtWidgets.QWidget(self)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 400, 180))
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.commentVal = QtWidgets.QTextEdit(self.gridLayoutWidget)
		self.full_name = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.full_name, 0, 0)
		self.passport = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.passport, 1, 0)
		self.nameVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.nameVal, 0, 1)
		self.passportVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.passportVal, 1, 1)
		self.comment = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.comment, 2, 0)
		self.gridLayout.addWidget(self.commentVal, 2, 1)
		self.btnDone = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.btnDone, 3, 1)
		
		onlyInt = QtGui.QIntValidator()
		self.passportVal.setValidator(onlyInt)
		
		self.full_name.setText("ФИО")
		self.passport.setText("Пасспорт")
		self.comment.setText("Комментарий")
		self.btnDone.setText("Готово")
		self.btnDone.clicked.connect(self.reject)
	
	def exec_(self):
		super(NewClientDialog, self).exec_()
		name = self.nameVal.text()
		try: 
			passport = int(self.passportVal.text())
			comment = self.commentVal.toPlainText()
			if name:
				return [name, passport, comment]
			else: 
				warning = WrongInput(['Имя пустое'])
				warning.show()
				warning.exec_()
				return 0
		except ValueError: pass
		except UnboundLocalError: pass
		
	
	def closeEvent(self, event):
		pass

class NewRoomDialog(QtWidgets.QDialog):

	def __init__(self, parent = None):
		super(NewRoomDialog, self).__init__(parent)
		self.initUI()
		
	def initUI(self):
		self.resize(350, 260)
		self.gridLayoutWidget = QtWidgets.QWidget(self)
		self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 10, 330, 250))
		self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
		self.idLabel = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.idLabel, 0, 0)
		self.idVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.idVal, 0, 1)
		self.capacityLabel = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.capacityLabel, 1, 0)
		self.capacityVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.capacityVal, 1, 1)
		self.comfortLabel = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.comfortLabel, 2, 0)
		self.comfortVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.comfortVal, 2, 1)
		self.paymentLabel = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.paymentLabel, 3, 0)
		self.paymentVal = QtWidgets.QLineEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.paymentVal, 3, 1)
		self.commentLabel = QtWidgets.QLabel(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.commentLabel, 4, 0)
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.commentVal, 4, 1)
		self.btnDone = QtWidgets.QPushButton(self.gridLayoutWidget)
		self.gridLayout.addWidget(self.btnDone, 5, 1)
		
		
		onlyInt = QtGui.QIntValidator()
		self.idVal.setValidator(onlyInt)
		self.capacityVal.setValidator(onlyInt)
		self.comfortVal.setValidator(onlyInt)
		self.paymentVal.setValidator(onlyInt)
		
		self.idLabel.setText("Номер")
		self.capacityLabel.setText("Вместимость")
		self.comfortLabel.setText("Комфорт")
		self.paymentLabel.setText("Оплата за сутки")
		self.commentLabel.setText("Комментарий")
		
		self.btnDone.setText("Готово")
		self.btnDone.clicked.connect(self.reject)
	
	def exec_(self):
		super(NewRoomDialog, self).exec_()
		comment = self.commentVal.toPlainText()
		try: 
			id = int(self.idVal.text())
			capacity = int(self.capacityVal.text())
			comfort = int(self.comfortVal.text())
			payment = int(self.paymentVal.text())
			return [id, capacity, comfort, payment, comment]
		except ValueError: pass
		
	def closeEvent(self, event):
		pass


class WrongInput(QtWidgets.QDialog):

	def __init__(self, whats_wrong, parent = None):
		super(WrongInput, self).__init__(parent)
		self.initUI(whats_wrong)
		
	def initUI(self, whats_wrong):
		self.resize(10*len(whats_wrong), 100)
		self.setWindowTitle("Ошибка")
		
		self.verticalLayout = QtWidgets.QVBoxLayout(self)
		
		for i in whats_wrong:
			label = QtWidgets.QLabel(self)
			label.setText(str(i))
			self.verticalLayout.addWidget(label)
			

class show_client(QtWidgets.QDialog):

	def __init__(self, client, parent = None):
		super(show_client, self).__init__(parent)
		self.initUI(client)
		
	def initUI(self, client):
		self.client = client
		self.setWindowTitle("Клиент")
		self.resize(370, 280)
		self.setFixedSize(370, 280)
		
		self.gridframe = QtWidgets.QFrame(self)
		self.gridLayout = QtWidgets.QGridLayout(self.gridframe)

		nameLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(nameLabel, 0, 0)
		nameLabel.setText("ФИО:")
		
		fullName = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(fullName, 0, 1)
		fullName.setText(client.full_name)
		
		passportLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(passportLabel, 1, 0)
		passportLabel.setText("Пасспорт:")
		
		passportVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(passportVal, 1, 1)
		passportVal.setText(str(client.passport))
		
		settledLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(settledLabel, 2, 0)
		settledLabel.setText("Заселен в:")
		
		self.settledVal = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(self.settledVal, 2, 1)
		self.settledVal.setText(str(client.settled_into))
		
		commentLabel = QtWidgets.QLabel(self.gridframe)
		self.gridLayout.addWidget(commentLabel, 3, 0)
		commentLabel.setText("Комментарий")
		
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridframe)
		self.gridLayout.addWidget(self.commentVal, 3, 1)
		self.commentVal.setPlainText(client.comment)
	
	def __del__(self):
		self.client.comment = self.commentVal.toPlainText()
	


class show_room(QtWidgets.QDialog):

	def __init__(self, room, parent = None):
		super(show_room, self).__init__(parent)
		self.initUI(room)
		
	def initUI(self, room):
		self.setWindowTitle("Комната")
		self.resize(380, 330)
		self.setFixedSize(380, 330)
		
		self.room = room
		self.gridframe = QtWidgets.QFrame(self)
		gridLayout = QtWidgets.QGridLayout(self.gridframe)
		
		idLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(idLabel, 0, 0)
		idLabel.setText("Номер:")
		
		idVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(idVal, 0, 1)
		idVal.setText(str(room.id))
		
		capacityLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(capacityLabel, 1, 0)
		capacityLabel.setText("Вместимость:")
		
		capacityVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(capacityVal, 1, 1)
		capacityVal.setText(str(room.capacity))
		
		comfortLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(comfortLabel, 2, 0)
		comfortLabel.setText("Комфорт:")
		
		comfortVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(comfortVal, 2, 1)
		comfortVal.setText(str(room.comfort))
		
		paymentLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(paymentLabel, 3, 0)
		paymentLabel.setText("Оплата за сутки:")
		
		paymentVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(paymentVal, 3, 1)
		paymentVal.setText(str(room.payment))
		
		clientsLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(clientsLabel, 4, 0)
		clientsLabel.setText("Клиенты:")
		
		self.clientsVal = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(self.clientsVal, 4, 1)
		self.clientsVal.setText(str(self.room.clients))
		
		commentLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(commentLabel, 5, 0)
		commentLabel.setText("Комментарий")
		
		self.commentVal = QtWidgets.QPlainTextEdit(self.gridframe)
		gridLayout.addWidget(self.commentVal, 5, 1)
		self.commentVal.setPlainText(room.comment)
		
		
	def __del__(self):
		self.room.comment = self.commentVal.toPlainText()
		
class DateDialog(QtWidgets.QDialog):
	
	def __init__(self, parent = None):
		super(DateDialog, self).__init__(parent)
		self.initUI()
		
	def initUI(self):
		self.setWindowTitle("Введите даты")
		self.resize(200, 200)
		self.setFixedSize(350, 120)
		
		self.gridframe = QtWidgets.QFrame(self)
		gridLayout = QtWidgets.QGridLayout(self.gridframe)
		
		settlementLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(settlementLabel, 0, 0)
		settlementLabel.setText("Заселяется:")
		
		evictionLabel = QtWidgets.QLabel(self.gridframe)
		gridLayout.addWidget(evictionLabel, 1, 0)
		evictionLabel.setText("Выселяется:")
		
		self.settlementVal = QtWidgets.QDateEdit()
		gridLayout.addWidget(self.settlementVal, 0, 1)
		
		self.evictionVal = QtWidgets.QDateEdit()
		gridLayout.addWidget(self.evictionVal, 1, 1)
		
		btnDone = QtWidgets.QPushButton()
		gridLayout.addWidget(btnDone, 5, 1)
		btnDone.setText("Готово")
		btnDone.clicked.connect(self.reject)
		self.show()
		
		
	def exec_(self):
		super(DateDialog, self).exec_()
		settlement = self.settlementVal.date().toPyDate()
		
		eviction = self.evictionVal.date().toPyDate()
		return [settlement, eviction]
		
	def closeEvent(self, event):
		pass