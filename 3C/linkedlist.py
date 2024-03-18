class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
    
    
class Linkedlist:
    def __init__(self):
        self.head = None
    
    def add(self, val):
        if self.head == None:
            self.head = Node(val, None)
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = Node(val, None)
    
    def show(self):
        cur = self.head
        while cur != None:
            print(cur.val)
            cur = cur.next


ll = Linkedlist()
ll.add(1)
ll.add(2)
ll.add(3)
ll.add(4)

ll.show()