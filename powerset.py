class HashTable:
    def __init__(self, sz, stp):
        self.size = sz
        self.step = stp
        self.slots = [None] * self.size

    def hash_fun(self, value):        
        result = 0
        for i in range(len(value)):
            result += (ord(value[i]) * (1+i))
        result = result % self.size
        return result
    
    def seek_slot(self, value):
        slot_number = self.hash_fun(value)
        if self.slots[slot_number] is None:
            return slot_number
        else:
            for i in range(self.size):
                slot_number += self.step
                if slot_number >= self.size:
                    slot_number -= self.size
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
            for i in range(self.size):
                slot_number += self.step
                if slot_number >= self.size:
                    slot_number -= self.size
                if self.slots[slot_number] == value:
                    return slot_number

class PowerSet(HashTable):

    def __init__(self):
        super(HashTable, self).__init__(20000, 3)
        self.powerSet = set()

    def size(self):
        return len(self.powerSet)
        # количество элементов в множестве

    def put(self, value):
        # всегда срабатывает

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
        # пересечение текущего множества и set2
        return None 

    def union(self, set2):
        # объединение текущего множества и set2
        return None

    def difference(self, set2):
        # разница текущего множества и set2
        return None

    def issubset(self, set2):
        # возвращает True, если set2 есть
        # подмножество текущего множества,
        # иначе False
        return False

ps = PowerSet()
print(ps.size())
