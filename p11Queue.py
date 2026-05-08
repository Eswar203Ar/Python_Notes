class MyQueue:
    def __init__(self,size):
        self.arr = [None] * size
        self.size = size
        self.front = 0
        self.rear = -1
        return
    
    def is_empty(self):
        if(self.rear == -1):
            return True
        else:
            return False
        return
    
    def insert(self,ele):
        if(self.is_full()):
            print("Queue is full")
        else:
            self.rear = self.rear + 1
            self.arr[self.rear] = ele
            print(f"{ele} inserted")
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
    
    def traverse(self):
        if(self.is_empty()):
            print("Queue is empty")
        else:
            print("Queue Items are")
        for i in range(self.rear+1):
            print(f"{self.arr[i]}")
        return
    
    def delete(self):
        if(self.is_empty()):
            print("Queue is Empty")
        else:
            print(f"Deleted : {self.arr[self.front]}")
        for i in range(1,self.rear + 1):
            self.arr[i-1] = self.arr[i]
        self.rear = self.rear-1
        return
    
que = MyQueue(5)
print("Queue is ready")
"""
while True:
    print("Queue operations")
    print("1.insert")
    print("2.peek")
    print("3.traverse")
    print("4.delete")
    print("5.Quit")
    
    choice = int(input("Enter choice:"))
    if(choice == 1):
        ele = int(input("Enter element to insert :"))
        que.insert(ele)
    elif(choice == 2):
        que.peek()
    elif(choice == 3):
        que.traverse
    elif(choice == 4):
        que.delete()
    elif(choice == 5):
        print("Quit")
        break
   """     

que.insert(10)
que.insert(20)
que.insert(30)
que.insert(40)
que.insert(50)
que.insert(60)
que.peek()
que.traverse()
que.delete()
que.delete()

