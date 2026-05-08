class MyQueue:
    def __init__(self,size):
        self.arr = [None] * size
        self.front = 0
        self.rear = -1
        self.size = size
        return
    
    def is_empty(self):
        if(self.rear == -1 ):
            return True
        else:
            return False
    
    def insert(self,ele):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.arr[self.rear] = ele
            print(f"{ele} Inserted")
        return
    
    def is_full(self):
        if(self.rear == self.size-1):
            return True
        else:
            return False
        return
    
    def peek(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            print(f"peek : {self.arr[self.front]}")
        return
    
    def display(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            print("Queue items are:")
        for i in range(self.rear+1):
            print(self.arr[i])
        return  
    
    def delete(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            print(f"Deleted : {self.arr[self.front]}")
        for i in range(1,self.rear+1):
            self.arr[i-1] = self.arr[i]
        self.rear = self.rear -1
        return  
    
Queue = MyQueue(5)
print("Queue is Ready")

Queue.insert(10)
Queue.insert(20)
Queue.insert(30)
Queue.insert(40)
Queue.insert(50)
Queue.insert(60)

Queue.peek()
Queue.display()
Queue.delete()
Queue.delete()
    