class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None
        self.prev_node = None


class DoublyLinkedList():
    def __init__(self):
        super().__init__()
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, data):
        newnode = Node(data)
        if self.length == 0:
            self.head = newnode
            self.tail = newnode
        else:
            self.tail.next_node = newnode
            newnode.prev_node = self.tail
            self.tail = newnode
        self.length += 1
    def __len__(self):
        return self.length
    
    def __getitem__(self, index):
        for _ in range(index):
            
        
        
