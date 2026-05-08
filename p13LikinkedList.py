class Node:
    def __init__(self,data):
        self.data = data
        self.link = None
        return
class LinkedList:
    def __init__(self):
        self.head = None
        return
    def append(self,data):
        self.temp = Node(data)
        if(self.head == None):
            self.head = self.temp
        else:
            self.last = self.head
            while(self.last.link != None):
                self.last = self.last.link
            self.last.link = self.temp
        print(f" {data} Appeneded")
        return
    
    def traverse(self):
        if(self.head == None):
            print("List is empty")
        else:
            temp = self.head
            while(temp != None):
                print(temp.data)
                temp = temp.link
        return
    
    def get_count(self):
        count = 0
        self.temp = self.head
        while(self.temp != None):
            count = count + 1
            self.temp = self.temp.link
        return count
    
    def add_first(self,data):
        self.temp = Node(data)
        self.temp.link = self.head
        self.head = self.temp
        print("added at first")
        return
    
    def add_after(self,loc,data):
        n = self.get_count()
        if(loc < 0 or loc >= n):
            print("Invalid Loc given")
        else:
            i = 1
            target = self.head
            while i < loc:
                target = target.link
                i = i + 1
            temp = Node(data)
            temp.link = target.link
            target.link = temp
            print("after added")
            
    def delete_first(self):
        if(self.head == None):
            print("List is empty")
        else:
            target = self.head
            self.head = self.head.link
            target.link = None
            del target
            print("first node deleted")
        return
    
    def delete_after(self,loc):
        n = self.get_count()
        if(loc < 1 or loc > n-1):
            print("Inavalid Location")
        else:
            i = 1
            temp = self.head
            while(i < loc):
                temp = temp.link
                i = i+1
            target = temp.link
            temp.link = target.link
            target.link = None
            del target
            print("node delete after ")
        return
    
    def swap_data(self,loc1,loc2):
        n = self.get_count()
        if(loc1<1 or loc1>n or loc2<1 or loc2>n):
            print("Inavlaid locs given")
        else:
            i=1
            temp1 = self.head
            while(i<loc1):
                temp1 = temp1.link
                i = i+1
            i=1
            temp2 = self.head
            while(i<loc2):
                temp2 = temp2.link
                i = i +1
                temp =  temp2.data
                temp1 = data = temp2.data
                temp2.data = temp
                print("data swapped")
            return   
    
        
               
                  

obj = LinkedList()
obj.append(10)
obj.append(20)
obj.append(30)

obj.traverse()

obj.append(40)
obj.append(50)

obj.traverse()

print(f"count : {obj.get_count()}")

obj.traverse()

obj.add_first(5)

obj.traverse()

obj.add_after(3,25)
obj.traverse()

obj.delete_first()
obj.delete_first()
obj.delete_first()
obj.traverse()

obj.delete_first()
obj.traverse()

obj.delete_after(3)
obj.traverse()

obj.swap_data(2,5)
obj.traverse()