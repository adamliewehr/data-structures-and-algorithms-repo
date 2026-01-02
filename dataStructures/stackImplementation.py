class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.prev = None 
        
class Stack():
    
    def __init__(self) -> None:
        self.head = None
        self.length=0

    def push(self, item):
        newNode = Node(item)
        self.length+=1
        if not self.head:
            self.head = newNode
            return
        
        newNode.prev = self.head
        self.head = newNode
        

    def pop(self):
        self.length=max(0, self.length-1)
        if self.length==0:
            head = self.head
            self.head = None
            return head.value
        
        head = self.head
        self.head = self.head.prev
        
        return head.value
    

        
    def peek(self):
        return self.head.value
    
    def printStack(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.prev
        print()
    


myStack = Stack()

myStack.push("A")
myStack.push("B")
myStack.push("C")
myStack.push("D")

myStack.pop()

print(myStack.peek())

myStack.printStack()