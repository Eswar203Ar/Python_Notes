class MyStack:
    def __init__(self,size):
        self.arr = [None] * size
        self.top = -1
        self.size = size
        return
    
    #add the vales into the stop in top order last in first out
    def push(self,ele):
        if(self.is_full()):
            print("stack is full")
        else:
            self.top = self.top+1
            self.arr[self.top] = ele
            print(f"{ele} pushed")
        return
    ## check the stack is full or not
    def is_full(self):
        if(self.top == self.size - 1):
            return True
        else:
            return False
        return
    
    # peek is showing the top element peek/top are same without removing 
    def peek(self):
        if(self.is_empty()):
            print("stack is empty")
        else:
            print(f"peek : {self.arr[self.top]}")
        return
    
    def is_empty(self):
        if(self.top == -1):
            return True
        else:
            return False
        return
    
    def display(self):
        if(self.is_empty()):
            print("stack is empty")
        else:
            print("stack Items are:")
        for i in range(self.top,-1,-1):
            print(self.arr[i])
        return
    
    def pop(self):
        if(self.is_empty()):
            print("stack is empty")
        else:
            print(f"pop : {self.arr[self.top]}")
        self.top = self.top - 1
        return  
             

## stack size is decalred
stack = MyStack(5)
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
stack.push(50)
stack.push(60)

stack.peek()

stack.display()

stack.pop()
stack.pop()