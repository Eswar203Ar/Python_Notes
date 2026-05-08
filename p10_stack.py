class MyStack:
    def __init__(self,size):
        self.arr = [None] * size
        self.top = -1
        self.size = size
        return
    
    def push(self,ele):
        if(self.is_full()):
            print("Stack is full")
        else:
            self.top = self.top+1
            self.arr[self.top] = ele
            print(f"{ele} Pushed")
        return
    
    def is_full(self):
        if(self.top == self.size-1):
            return True
        else:
            return False   
    
    def peek(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(f"Peek : {self.arr[self.top]}") 
            return
        
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False 
    
    def traverse(self):
        if self.is_empty():
            print("stack is empty")
        else:
            print("stack Items are :")
            for i in range(self.top,-1,-1):
                print(self.arr[i])
        return
    
    def pop(self):
        if self.is_empty():
            print("Stack is Empty")
        else:
            print(f"pop : {self.arr[self.top]}")
            self.top = self.top-1
        return
         
    
stk = MyStack(5)
print("Stack is ready")
stk.push(10)
stk.push(20)
stk.push(30)
stk.push(40)
stk.push(50)
stk.push(60)

stk.peek()
stk.traverse()
stk.pop()
stk.pop()
