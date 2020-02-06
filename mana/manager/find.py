
def find_by_id(list, id):
	position = -1
	for i in range(0, len(list)):
		if list[i].id == id: 
			position = i
	return position
def find_by_passport(list, passport):
	position = -1
	for i in range(0, len(list)):
		if list[i].passport == passport: 
			position = i
	return position
	
def find_residents_by_id(list, id):
	positions = []
	for i in range(0, len(list)):
		if list[i].room.id == id: 
			positions.append(i)
	return positions
	
def find_residents_by_passport(list, passport):
	positions = []
	for i in range(0, len(list)):
		if list[i].client.passport == passport: 
			positions.append(i)
	return positions
	