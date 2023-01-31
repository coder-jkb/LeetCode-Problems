class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        popped = []
        opening = ['(','[','{']
        closing = [')',']','}']
        for brk in s:
            if brk in opening:
                stack.append(brk)
            if brk in closing:
                if len(stack) > 0 and opening[closing.index(brk)] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
