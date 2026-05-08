class MyCircularQueue:
    def __init__(self,size):
        self.arr = [None] * size
        self.front = -1
        self.rear = -1
        self.size = size
        return
    
    def insert(self,ele):
        if(self.is_full()):
            print("circular queue is full")
        else:
            if(self.rear == -1):
                self.front = 0
                self.rear = 0
                self.arr[self.rear] = ele
                print(f"{ele} inserted")
            elif(self.rear == self.size-1):
                self.rear = 0
                self.arr[self.rear] = ele
                print(f"{ele} inserted")
            else:
                self.rear = self.rear+1
                self.arr[self.rear] = ele
                print(f"{ele} inserted")
        return
    
    def is_full(self):
        if((self.front == 0 and self.rear == self.size-1) or  (self.front == self.rear+1)):
            return True
        else:
            return False
        return
    
    def delete(self):
        if(self.is_empty()):
            print("Cricular Queue is empty")
        else:
            print(f"Deleted : {self.arr[self.front]}")
            if(self.front == self.rear):
                self.front = -1
                self.rear = -1
            elif(self.front == self.size-1):
                self.front = 0
            else:
                self.front = self.front + 1
        return   
    
    def is_empty(self):
        if(self.front == -1):
            return True
        else:
            return False
        return     
    
    def display(self):
        if(self.is_empty()):
            print("circular queue is empty")
        else:
            if(self.front <= self.rear):
                for i in range(self.front,self.rear+1):
                    print(self.arr[i])
            else:
                for i in range(self.front,self.size):
                    print(self.arr[i])
        return
                
      
cQueue = MyCircularQueue(8)
print("cricular queue is ready")
cQueue.insert(10)
cQueue.insert(20)
cQueue.insert(30)
cQueue.insert(40)
cQueue.insert(50)
cQueue.insert(60)
cQueue.insert(70)
cQueue.insert(80)
cQueue.insert(90)

cQueue.delete()
cQueue.delete()

cQueue.display()