class Node:
    def __init__(self,data):
        self.__data = data
        self.__next = None
    def set_next(self,node):
        self.__next = node
    def get_next(self):
        return self.__next
    def get_data(self):
        return self.__data
    def set_data(self,data):
        self.__data = data
class LinkedList:
    def __init__(self):
        self.__head = None
    def set_head(self,node):
        self.__head = node
    def get_head(self):
        return self.__head
    def append(self,data):
        node = Node(data)
        if(self.get_head()==None):     #######List is empty
            self.set_head(node)
        else:
            temp = self.get_head()  #####storing head for traversal
            while(temp.get_next()!=None):
                temp = temp.get_next()
            temp.set_next(node)   ########storing node in the next of last element
    def insert(self,pos,data):
        if(pos == 1 and self.get_head()==None):
            self.append(data)
        elif(pos ==1):
            node = Node(data)
            temp = self.get_head()
            node.set_next(temp)
            self.set_head(node)
        else:
            temp = self.get_head()
            if(temp == None):
                print("Invalid position no element in list.")
                return
            u = 1
            while(u<pos-1): ###traversing upto pos-1 node in the list
                if(temp.get_next() != None):
                    temp = temp.get_next()
                elif(temp.get_next()==None and u==pos-1):
                    break
                else:
                    print("Invalid position only {} elements in the list".format(u))
                    break
                u+=1
            if(u==pos-1):
                node = Node(data)
                nxt = temp.get_next()
                temp.set_next(node)
                node.set_next(nxt)
    def remove(self):
        temp = self.get_head()
        if(temp == None):
            print("List is empty")
        else:
            if(temp.get_next() == None):
                self.set_head(None)
                return temp.get_data()
            while(temp.get_next().get_next()!=None):
                temp = temp.get_next()
            t = temp.get_next()
            temp.set_next(None)
            return t.get_data()
    def delete(self,pos):
        if(self.get_head()==None):
            print("Nothing to delete, List is empty.")
        elif(pos ==1):
            temp = self.get_head()
            self.set_head(temp.get_next())
        else:
            temp = self.get_head()
            if(temp == None):
                print("Invalid position no element in list.")
                return
            u = 0
            while(u < pos-2): ###traversing upto pos-1 node in the list
                if(temp.get_next() != None):
                    temp = temp.get_next()
                elif(temp.get_next()==None and u==pos-1):
                    break
                else:
                    print("Invalid position only {} elements in the list".format(u))
                    break
                u+=1
            if(u==pos-2):
                if(temp.get_next().get_next()!=None):
                    temp.set_next(temp.get_next().get_next())
                else:
                    temp.set_next(None)
                
    def traverse(self):
        temp = self.get_head()
        while(temp != None):
            print(temp.get_data(),end=" ")
            temp = temp.get_next()
linklist = LinkedList()
while(True):
    print("1. Insert \n2. Append(insert at last pos) \n3. Delete \n4. Remove(from last pos.) \n5. Traverse \n6. Exit")
    ch = int(input("Enter choice: "))
    if(ch == 1):
        data = input("Enter data: ")
        pos = int(input("Enter position: "))
        linklist.insert(pos,data)
        pos = print("Data inserted at pos: ",pos)
    elif(ch == 2):
        data = input("Enter data: ")
        linklist.append(data)
    elif(ch == 3):
        pos = int(input("Enter position: "))
        linklist.delete(pos)
        print("Element is removed at position: ",pos)
        print("Data deleted at position: ",pos)
    elif(ch == 4):
        rem = linklist.remove()
        print(f"{rem} is removed from the last position.")
    elif(ch == 5):
        print("Element in list are: ")
        linklist.traverse()
    elif(ch == 6):
        exit(0)
    else:
        print("Invalid Choice. Try again....")
                    

                        
                    


                
            
