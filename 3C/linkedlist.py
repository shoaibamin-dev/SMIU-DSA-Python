class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next
    
    def show(self):
        cur = self
        while cur != None:
            print(cur.val)
            cur = cur.next

n5 = Node("there", None)
n4 = Node("you", n5)
n3 = Node("are", n4)
n2 = Node("how", n3)
n1 = Node("hello", n2)

n1.show()