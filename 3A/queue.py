class Queue:
    def __init__(self) -> None:
        self.vals = []
    def enqueue (self, val):
        self.vals.append(val)
    def dequeue(self):
        count = 0
        for _ in self.vals:
            if count == len(self.vals)-1: break
            self.vals[count] = self.vals[count+1]
            count += 1
        self.vals.pop()
    def valueAt(self, idx):
        return self.vals[idx]
    def indexAt(self, val):
        count = 0
        for v in self.vals:
            if v == val: return count
            count += 1
        return -1 
    
bookQueue = Queue()
bookQueue.enqueue('OOP')
bookQueue.enqueue('DS')
bookQueue.enqueue('PF')
bookQueue.dequeue()

print(bookQueue.vals)