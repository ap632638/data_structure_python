class Stack:
	def __init__(self,max_size):
		self.__max_size = max_size
		self.__stack = [None]*max_size
		self.__top = -1;
	def get_max_size(self):
		return self.__max_size
	def get_top(self):
		return self.__top
	def set_top(self,top):
		self.__top = top
	def push(self,data):
		if(self.get_top()==self.get_max_size()-1):
			print("Stack is full")
		else:
			self.set_top(self.get_top()+1)
			self.__stack[self.get_top()] = data
			print("Data Inserted")
	def pop(self):
		if(self.get_top()==-1):
			print("Stack is empty")
		else:
			self.__stack.remove(self.__stack[self.get_top()])
			self.set_top(self.get_top()-1)
			print("Data removed")
	def display(self):
		if(self.get_top()==-1):
			print("Stack is empty")
		else:
			for i in range(self.get_top(),-1,-1):
				print(self.__stack[i])

size = int(input("Enter size of stack: "))
stack = Stack(size)
while(True):
	print("1. Push \n2. Pop \n3. Display \n4. Exit")
	ch = int(input("Choose from the options:- "))
	if(ch==1):
		data = input("Enter data to push: ")
		stack.push(data)
	elif(ch==2):
		stack.pop()
	elif(ch==3):
		stack.display()
	elif(ch==4):
		exit(0)
	else:
		print("Invalid choice. Try Again....")
