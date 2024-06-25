"""
|||||||||||||||||||||||||||

Циклические буферы -- FIFO

|||||||||||||||||||||||||||
"""

class fifo_v1():
	"""Простота релизации через класс использующий только методы словаря
		Использует много лишенй памяти для индексации старых значений,
		Из за этого требует необходимое количество памяти, но быстрее нижнего варианта"""
	def __init__(self, max=10):
		self.head = {}
		self.indx = 0
		self.maxLen = max
	def appendEl(self, item):
		self.indx = self.indx+1
		if len(self.head) >= self.maxLen:
			keys = self.head.keys()
			self.head.pop(min(keys))
			self.head[self.indx] = item
		else:
			self.head[self.indx] = item
	def print(self):
		print(self.head)

class box:
	def __init__(self, item):
		self._item = item
		self._index = None
		self._next = None
class fifo_v2():
	"""
	Вариант с еще более длительной работой,
	в основном из за того что основан на
	принципе связанных списков, плюс этого варианта это присущая Св\Спискам строгое соблюдение порядка
	Но минусом идет повышенное потребление памяти.
	"""
	def __init__(self, max=10):
		self.head = None
		self.max = max
		self.Id = 0
		self.chek = 0
		self.list = []

	def appendEl(self, item):
		self.Id += 1
		self.list.append(self.Id)
		item = box(item)
		piper = self.head
		if piper == None:
			item._index = self.Id
			self.head = item
			self.chek += 1
		else:
			if self.chek >= self.max:
				repl = min(self.list)
				self.list.remove(repl)
				while piper:
					if piper:
						if piper._index == repl:
							piper._item = item._item
							piper._index = self.Id
							break
						else:
							piper = piper._next
					else:
						break
			else:
				while piper:
					if piper._next != None:
						piper = piper._next
					else:
						item._index = self.Id
						piper._next = item
						self.chek += 1
						break
	def print(self):
		piper = self.head
		while piper:
			print(piper._item, piper._index)
			piper = piper._next




def main(list = None):
	"""
	fifo_v1 = Первый вариант
	fifo_v2 = Второй вариант
	"""
	# list = fifo_v1(max=10)
	# list = fifo_v2()
	for i in range(1000):
		list.appendEl(f'number--{i}--')
	list.print()
if __name__ == "__main__":
	main()

















