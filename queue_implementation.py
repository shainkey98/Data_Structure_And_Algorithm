# import sys
# sys.stdin = open("input.in","r+")
# sys.stdout = open("output.out","w+")


class Queue(object):
	def __init__(self,length):
		self.front = -1
		self.rear = 0
		self.array = []
		self.max = length

	def enqueue (self,item):
		if self.front+1 == self.max:
			print("Queue if full")
		else:
			self.front += 1
			self.array.append(item)

	def dequeue(self):
		if self.front == -1:
			print("Queue is empty")
		else:
			self.front -= 1
			self.array.pop(0)

	def show(self):
		if self.front == -1:
			print("Queue is empty")
		else:
			print(*self.array)

	def size(self):
		if self.front == -1:
			print("Queue is empty")
		else:
			print(len(self.array))

queue = Queue(5)
queue.enqueue(10)
queue.enqueue(100)
queue.enqueue(1)
queue.show()
queue.dequeue()
queue.show()
queue.size()