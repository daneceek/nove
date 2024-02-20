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
            if self.length == 1:
                self.head.next_node = newnode
                
                newnode.prev_node = self.head
                self.tail = newnode
            else:
                self.tail.next_node = newnode
                newnode.prev_node = self.tail
                self.tail = newnode
        self.length += 1
    def __len__(self):
        return self.length
    
    def __getitem__(self, index):
        if index == 0:
            return self.head.data
        if (index >= self.length) or ((index * -1) > self.length):
            raise IndexError
        if index < 0:
            this_node = self.tail
            for _ in range((-1*index) - 1):
                print(this_node.data)
                this_node = this_node.prev_node
            return this_node.data
        else:
            this_node = self.head
            for _ in range(index):
                this_node = this_node.next_node
            return this_node.data
    def __setitem__(self, index, number):
        if index == 0:
             self.head.data = number  
        if (index >= self.length) or ((index * -1) > self.length):
            raise IndexError
        if index < 0:
            this_node = self.tail
            for _ in range((-1*index) - 1):
                this_node = this_node.prev_node
            this_node.data = number
        else:
            this_node = self.head
            for _ in range(index):
                this_node = this_node.next_node
            this_node.data = number

    def __delitem__(self, index):
        if (index == 0) or ((-1*self.length) == index) :
             self.head = self.head.next_node
             del self.head.prev_node
        elif ((index+1) == self.length) or (index == -1):
            self.tail = self.tail.prev_node
            del self.tail
        elif (index >= self.length) or ((index * -1) > self.length):
            raise IndexError
        elif index < 0:
            
            this_node = self.tail
            for _ in range((-1*index) - 1):
                this_node = this_node.prev_node
            this_node.next_node.prev_node = this_node.prev_node
            this_node.prev_node.next_node = this_node.next_node
            del this_node
        
        elif index > 0:
            this_node = self.head
            for _ in range(index):
                this_node = this_node.next_node
            
            this_node.next_node.prev_node = this_node.prev_node
            this_node.prev_node.next_node = this_node.next_node
            del this_node
        self.length -= 1
    
    
    

