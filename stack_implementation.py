# import sys
# sys.stdin = open("input.in","r+")
# sys.stdout = open("output.out","w+")


class stack(object):
	def __init__(self,length):
		self.max = length
		self.array = []
		self.top = -1

	def push(self,item):
		if self.top<self.max-1:
			self.array.append(item)
			self.top +=1
		else:
			print("Stack is full")

	def pop(self):
		if self.top == -1:
			print("Stack is Empty")
		else:
			self.array.pop()
			self.top -= 1
	def peek(self):
		if self.top == -1:
			print("Stack is empty")
		else:
			print(self.array[-1])

	def size(self):
		if self.top == -1:
			print("Stack is empty")
		else:
			print(len(self.array))

	def show(self):
		if self.top == -1:
			print("Stack is empty")
		else:
			print(*self.array)


Stack = stack(5)
Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(2)
Stack.push(3)
Stack.show()
Stack.push(3)