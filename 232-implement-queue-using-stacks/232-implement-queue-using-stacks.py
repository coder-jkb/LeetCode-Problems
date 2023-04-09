class MyQueue:

    def __init__(self):
        self.s1 = []

    def push(self, x: int) -> None:
        s2 = []
        while self.s1:
            val = self.s1.pop()
            s2.append(val)
            
        self.s1.append(x)
        while s2:
            val = s2.pop()
            self.s1.append(val)
            
        

    def pop(self) -> int:
        return self.s1.pop()
        

    def peek(self) -> int:
        return self.s1[-1]
        

    def empty(self) -> bool:
        return len(self.s1) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

'''
Stack S1 (represents Queue)
1 2 3 4 5 6 7 ]
^

Stack S2: helper stack
 ]
^

QPush:
Copy S1 to S2
SPush in S2
Copy S2 to S1
Reset S2 to empty stack 

QPop:
SPop S1

Qpeek:
Speek S1

QEmpty:
SEmpty S1
'''