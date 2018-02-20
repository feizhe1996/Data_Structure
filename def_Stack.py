class Stack:
	def __init__(self):
		self.item = []
	def isEmpty(self):
		return self.items == []
	def push(self,item):
		self.item.append(item)
	def pop(self):
		self.item.pop()
	def size(self):
		return len(self.item)
	def peek(self):
		return self.item[len(self.item)-1]

s = Stack()
s.push([1,2])
s.push(3)
print(s.peek())
print(s.size())