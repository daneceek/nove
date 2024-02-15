

class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.priority_array = []
        self.completed_sort = 0
    def push(self, item, priority):
        dictionary = {}
        dictionary[item] = priority
        self.queue.append(dictionary)
        self.priority_array.append(priority)
        
    def __len__(self):
        return len(self.queue)

    def pop(self):
        if len(self.queue) == 0:
            raise IndexError
        
        for _ in range(1, len(self.queue)):
            for item in self.queue:
                for task, priority in item.items():
                    if priority == min(self.priority_array):
                        self.queue.remove(item)
                        return task
    
    def __iter__(self):
        self.position = 0
        return self
    def __next__(self):
            if self.queue == []:
                    raise StopIteration
            item = self.queue[self.position]
            self.position += 1
            for task, priority in item.items():
                        if priority == min(self.priority_array):
                            self.priority_array.remove(min(self.priority_array))
                            self.queue.remove(item)
                            self.position = 0
                            return task 
                        else:
                            return next(self)
            if self.priority_array == []:
                            raise StopIteration
             

                    
        
        

    
        

# nejmensi cislo ma nejmensi prioritu