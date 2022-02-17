#итератор за *, задание без * тоже может
class FlatIterator:

	def __init__(self, obj_list):
		self.obj_list = obj_list

	def create_iterator(self, obj_list=None):
		if not obj_list:
			obj_list = self.obj_list
		res_list = []
		count = 0
		for lst in obj_list:
			if isinstance(lst, list):
				count = 1
				for el in lst:
					res_list.append(el)
			else:
				res_list.append(lst)
		if count:
			return self.create_iterator(res_list)
		return res_list

	def __iter__(self):
		self.iter_list = self.create_iterator()
		self.cursor = -1
		return self

	def __next__(self):
		self.cursor += 1
		if self.cursor == len(self.iter_list):
			raise StopIteration
		return self.iter_list[self.cursor]


nested_list = [
	['a', 'b', 'c', [1, 2]],
	['d', 'e', 'f', 'h', False, ['e', 'f', [1, 2], 'h'], ],
	[1, 2]
]

flat_list = [item for item in FlatIterator(nested_list)]
print(flat_list)
