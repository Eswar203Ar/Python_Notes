# Node class
class Node:
    def _init_(self, data):
        self.data = data
        self.link = None

# Linked List class
class LinkedList:
    def _init_(self):
        self.head = None

    # Add node at the end
    def append(self, data):
        new_node = Node(data)
        
        # If the list is empty, new node becomes head
        if self.head == None:
            self.head = new_node
            return

        # Otherwise, go to the end and insert
        temp = self.head
        while temp.link:
            temp = temp.link
        temp.link = new_node

    # Linear search
    def linear_search(self, ele):
        temp = self.head

        while temp:
            if temp.data == ele:
                print("Element found")
                return
            temp = temp.link
        
        print("Element not found")

# Main program
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

ele = int(input("Enter element to search: "))
ll.linear_search(ele)