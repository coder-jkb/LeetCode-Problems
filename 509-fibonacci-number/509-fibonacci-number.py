class Solution:
    def fib(self, n: int) -> int:
        store = {0: 0, 1: 1}
        if n > 1 and n not in store:
            store[n] = self.fib(n-1) + self.fib(n-2)
                
        return store[n]