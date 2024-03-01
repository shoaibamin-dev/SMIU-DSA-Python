class MyStack:
    def __init__(self) -> None:
        self.vals = []
    def push (self, val):
        self.vals.append(val)
    def pop(self, ):
        self.vals.pop()
    def peak (self):
        return max(self.vals)
    

bookStack = MyStack()
bookStack.push('OOP')
bookStack.push('DS')
bookStack.push('PF')
bookStack.pop()
print(bookStack.peak())