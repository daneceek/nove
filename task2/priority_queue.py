

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
        
        if self.position < len(self.queue):
            item = self.queue[self.position]
            self.position += 1
            for task, priority in item.items():
                print(self.position)
                print(self.priority_array)
                print(bool(self.priority_array))
                if self.priority_array == False:
                    return StopIteration
                else:
                    print(("jys"))
                    if priority == min(self.priority_array):
                        print(task)
                        
                        self.priority_array.remove(min(self.priority_array))
                        return task 
                    else:
                        return next(pq)
               

                    
        
        

    
        
pq = PriorityQueue()
pq.push("Task 1", 3)
pq.push("Task 2", 1)
pq.push("Task 3", 2)
pq.push("Task 4", 6)
tasks = list(pq)
print(tasks)

# nejmensi cislo ma nejmensi prioritu