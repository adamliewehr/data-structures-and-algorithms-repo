class Node():
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None 
        
class DoublyLinkedList():
    def __init__(self) -> None:
        self.length = 0
        self.head = None
        self.tail = None
        
    def prepend(self, item):
        node = Node(item)
        
        # bookkeeping!
        self.length+=1
        
        if not self.head:
            self.head, self.tail = node, node
            return
        
        # new node points forward to the current head
        # current head points back to new node
        # head points to new node
        node.next = self.head
        self.head.prev = node
        self.head = node
        
    
    def insertAt(self, item, idx):
        
        
        
        if idx > self.length:
            raise Exception("uh oh")
        
        
        
        if idx == self.length:
            self.append(item)
            return
        elif idx==0:
            self.prepend(item)
            return 
        
        self.length+=1
            
        curr = self.head
        for _ in range(idx): # go to the node we are inserting at
            if curr:
                curr = curr.next
                
        node = Node(item)
        node.next = curr
        node.prev = curr.prev
        curr.prev = node
        if curr.prev:
            node.prev.next = node
            
        
    
    def append(self, item):
        self.length+=1
        node = Node(item)
        
        if not self.tail:
            self.head, self.tail = node, node
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def remove(self, item):
        curr = self.head
        for i in range(self.length):
            if curr:
                if curr.value == item:
                    break
                curr = curr.next
                
        if not curr:
            return None # if there is no current, there is no item to remove
        
        self.length-=1
        if self.length == 0:
            out = self.head.value
            curr.prev, curr.next = None, None
            return out
        
        if curr.prev:
            curr.prev = curr.next
            
        if curr.next:
            curr.next = curr.prev
            
        
        if curr == self.head:
            self.head = curr.next
            
        if curr==self.tail:
            self.tail = curr.prev
            
        curr.prev, curr.next = None, None # break the links that curr is pointing to
        
        return curr.value
        
        
    
    def get(self, idx):
        pass
    
    def removeAt(self, idx):
        pass