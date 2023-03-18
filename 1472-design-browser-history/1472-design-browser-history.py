# Create the node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
# Create the doubly linked list class
class doubly_linked_list:
    def __init__(self):
        self.head = None
        self.curr = self.head

# Define the append method to add elements at the end
    def append(self, NewVal):
        NewNode = Node(NewVal)
        NewNode.next = None
        if self.head is None:
            NewNode.prev = None
            self.head = NewNode
            self.curr = NewNode
            return

        last = self.curr
        # while (last.next is not None):
        #     last = last.next
        last.next = NewNode
        NewNode.prev = last
        self.curr = NewNode
        return
    
class BrowserHistory:

    def __init__(self, homepage: str):
        self.dll = doubly_linked_list()
        self.dll.append(homepage)

    def visit(self, url: str) -> None:
        self.dll.append(url)

    def back(self, steps: int) -> str:
        while steps > 0 and self.dll.curr.prev:
            self.dll.curr = self.dll.curr.prev
            steps-=1
        return self.dll.curr.data

    def forward(self, steps: int) -> str:
        while steps > 0 and self.dll.curr.next:
            self.dll.curr = self.dll.curr.next
            steps -= 1
        return self.dll.curr.data
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)