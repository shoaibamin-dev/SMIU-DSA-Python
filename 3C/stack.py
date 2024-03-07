class MyStack:
    def __init__(self) -> None:
        self.vals = []
    def push (self, val):
        self.vals.append(val)
    def pop(self, ):
        self.vals.pop()
    def peak (self):
        return max(self.vals)
    def valueAt(self, idx):
        return self.vals[idx]
    def indexAt(self, val):
        count = 0
        for v in self.vals:
            if v == val: return count
            count += 1
        return -1 
    
bookStack = MyStack()
bookStack.push('OOP')
bookStack.push('DS')
bookStack.push('PF')
bookStack.pop()

print(bookStack.valueAt(1))