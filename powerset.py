class HashTable:
	def __init__(self, sz, stp):
		self.sizes = sz
		self.step = stp
		self.slots = [None] * self.sizes

	def hash_fun(self, value):        
		result = 0
		for i in range(len(value)):
			result += (ord(value[i]) * (1+i))
		result = result % self.sizes
		return result
	
	def seek_slot(self, value):
		slot_number = self.hash_fun(value)
		if self.slots[slot_number] is None:
			return slot_number
		else:
			for i in range(self.sizes):
				slot_number += self.step
				if slot_number >= self.sizes:
					slot_number -= self.sizes
				if self.slots[slot_number] is None:
					return slot_number
		return None

	def put(self, value):
		slot_number = self.seek_slot(value)
		if slot_number is not None:
			self.slots[slot_number] = value
			return slot_number
		else:
			return None

	def find(self, value):
		slot_number = self.hash_fun(value)
		if self.slots[slot_number] == value:
			return slot_number
		else:
			for i in range(self.sizes):
				slot_number += self.step
				if slot_number >= self.sizes:
					slot_number -= self.sizes
				if self.slots[slot_number] == value:
					return slot_number

class PowerSet(HashTable):

	def __init__(self):
		HashTable.__init__(self, 20000, 3)
		self.powerSet = set()

	def size(self):
		return len(self.powerSet)
		# количество элементов в множестве

	def put(self, value):
		if self.get(value) == True:
			return
		else:
			self.powerSet.add(value)
			slot_number = self.seek_slot(value)
			if slot_number is not None:
				self.slots[slot_number] = value

	def get(self, value):
		if value in self.powerSet:
			return True
		return False

	def remove(self, value):
		if self.get(value) == True:
			self.powerSet.remove(value)
			self.slots[self.find(value)] = None
			return True
		return False

	def intersection(self, set2):
		newSet = self.powerSet.intersection(set2.powerSet)
		newPowerSet = PowerSet()
		for i in newSet:
			newPowerSet.put(i)
		return newPowerSet

	def union(self, set2):
		newSet = self.powerSet.union(set2.powerSet)
		newPowerSet = PowerSet()
		for i in newSet:
			newPowerSet.put(i)
		return newPowerSet

	def difference(self, set2):
		newSet = self.powerSet.difference(set2.powerSet)
		newPowerSet = PowerSet()
		for i in newSet:
			newPowerSet.put(i)
		return newPowerSet

	def issubset(self, set2):
		return set2.powerSet.issubset(self.powerSet)
