class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None # if doubly linked list
        
class Queue():
    
    def __init__(self) -> None:
        self.head, self.tail = None, None
        self.length=0
    
    def enqueue(self, item):
        self.length+=1
        newNode = Node(item)
        if not self.tail: # if the queue is empty
            self.tail, self.head = newNode, newNode # we set the value of the tail and the head to the new node
            return
            
        self.tail.next = newNode # took the tail and added a new node to the queue
        self.tail = newNode # take the tail, and point it to the new node

    def deque(self):
        if not self.head:
            return None

        self.length-=1 # book keeping
        
        if self.length == 0: # if we are now at length 0
            self.tail = None # free the tail
        
        head = self.head # save our current head
        self.head = self.head.next # update our head to the next value
        head.next = None # the value we are about to deque: remove the reference to the next node
        return head # return the value of the head that was just popped or dequed
        
    def peek(self):
        return self.head.value
    
    def printQueue(self):
        temp = self.head
        while temp:
            print(temp.value, end=" -> ")
            temp = temp.next
        print()
    
myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
myQueue.enqueue("1")
myQueue.enqueue("2")
myQueue.enqueue("3")

myQueue.printQueue()