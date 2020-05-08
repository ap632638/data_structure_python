class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
            print("Data inserted")

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            print("Data removed and returned")
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg
size = int(input("Enter size of queue: "))
queue = Queue(size)
while(True):
	print("1. Enqueue \n2. Dequeue \n3. Display \n4. Exit")
	ch = int(input("Choose from the options:- "))
	if(ch==1):
		data = input("Enter data to push: ")
		queue.enqueue(data)
	elif(ch==2):
		queue.dequeue()
	elif(ch==3):
		print(queue)
	elif(ch==4):
		exit(0)
	else:
		print("Invalid choice. Try Again....")