class PriorityQueue:
    def __init__(self):
        self.queue = []
        self.priority = []
    def push(self, item, priority):
        self.queue.append(item)
        self.priority.append(priority)
    
    
    
    def __len__(self):
        return len(self.queue)

    
    def __iter__(self):
        return iter(self.queue)
    
priority_queue = PriorityQueue()
priority_queue.push("Task 1", 3)
priority_queue.push("Task 2", 1)
priority_queue.push("Task 3", 2)

print("Priority Queue Length:", len(priority_queue))

print("Tasks in Priority Order:")
for task in priority_queue:
    print(task)

print("Processing tasks in Priority Order:")
while len(priority_queue) > 0:
    task = priority_queue.pop()
    print("Processing:", task)

# nejmensi cislo ma nejmensi prioritu