import datetime

from . import find
from .client import Client
from .room import Room
from .resident import Resident


class Database():
	
	def __init__(self):
		self.path = 'data'
		self.clients = []
		self.rooms = []
		self.residents = []
		self.load_data()
		
	def save_data(self):
		self.save_clients()
		self.save_rooms()
		self.save_residents()
	
	def load_data(self):
		self.load_clients()
		self.load_rooms()
		self.load_residents()
		
	def save_clients(self):
		with open('manager\\' + self.path + '\\clients.txt', 'w') as file:
			for a in self.clients:
				file.write(a.full_name + '\n')
				file.write(str(a.passport) + '\n')
				file.write(a.comment + '\n')	
		pass
		
	def save_rooms(self):
		with open('manager\\' + self.path + '\\rooms.txt', 'w') as file:
			for a in self.rooms:
				file.write(str(a.id) + '\n')
				file.write(str(a.capacity) + '\n')
				file.write(str(a.comfort) + '\n')
				file.write(str(a.payment) + '\n')
				file.write(a.comment + '\n')
		pass
		
	def save_residents(self):
		with open('manager\\' + self.path + '\\residents.txt', 'w') as file:
			for a in self.residents:
				file.write(str(a.client.passport) + ' ')
				file.write(str(a.room.id) + '\n')
				file.write(str(a.settlement) + '\n')
				file.write(str(a.eviction) + '\n')
				file.write(str(a.comment) + '\n')
		pass

	def load_clients(self):
		act = 0
		with open('manager\\' + self.path + '\\clients.txt', 'r') as file:
			for line in file:
				line = line.replace('\n', '');
				act += 1
				if act == 1: full_name = line
				if act == 2: passport = int(line)
				if act == 3: 
					comment = line
					new_client = Client(full_name, passport, comment)
					self.clients.append(new_client)
					act = 0
		return self.clients
		
	def load_rooms(self):
		act = 0
		with open('manager\\' + self.path + '\\rooms.txt', 'r') as file:
			for line in file:
				line = line.replace('\n', '')
				act += 1
				if act == 1: id = int(line)
				if act == 2: capacity = int(line)
				if act == 3: comfort = int(line)
				if act == 4: payment = int(line)
				if act == 5: 
					comment = line
					new_room = Room(id, capacity, comfort, payment, comment)
					self.rooms.append(new_room)
					act = 0
		return self.rooms

	def load_residents(self):
		act = 0
		with open('manager\\' + self.path + '\\residents.txt', 'r') as file:
			for line in file:
				line = line.replace('\n', '')
				act += 1
				if act == 1:
					ids = list(map(int, line.split()))
					clientPos = find.find_by_passport(self.clients, ids[0])
					roomPos = find.find_by_id(self.rooms, ids[1])
				if act == 2:
					year, month, day = map(int, line.split('-'))
					settlement = datetime.date(year, month, day)
				if act == 3:
					year, month, day = map(int, line.split('-'))
					eviction = datetime.date(year, month, day)
				if act == 4:
					comment = line
					new_resident = Resident(self.clients[clientPos], self.rooms[roomPos], settlement, eviction, comment)
					self.residents.append(new_resident)
					act = 0
		return self.residents