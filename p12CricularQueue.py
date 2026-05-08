class CricularQueue:
    def __init__(self,size):
        self.arr = [None] *size
        self.front = -1
        self.rear = -1
        self.size = size
        return
    
    def insert(self,ele):
        if(self.is_full()):
            print("Cricular Queue is full")
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
                self.rear = self.rear + 1
                self.arr[self.rear] = ele
                print(f"{ele} inserted")
        return
    
    def is_full(self):
        if((self.front == 0 and self.rear == self.size-1) or (self.front == self.rear + 1)):
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
        
    def traverse(self):
        if(self.is_empty()):
            print("Empty Queue")
        else:
            if(self.front <= self.rear):
                for i in range(self.front ,self.rear+1):
                    print(self.arr[i])
            else:
                for i in range(self.front,self.size):
                    print(self.arr[i])
        return

        
                
            
    
cirQu = CricularQueue(8)
print("Cricular Queue is start")
cirQu.insert(10)
cirQu.insert(20)
cirQu.insert(30)
cirQu.insert(40)
cirQu.insert(50)
cirQu.insert(60)
cirQu.insert(70)
cirQu.insert(80)
cirQu.insert(90)
cirQu.delete()
cirQu.traverse()
