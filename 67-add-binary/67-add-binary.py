class Solution:
    def addBinary(self, a: str, b: str) -> str:
        s1 = a[::-1]
        s2 = b[::-1]
        while len(s1) < len(s2):
            s1 = s1+'0' # a is shorter
            
        while len(s1) > len(s2):
            s2 = s2+'0' # b is shorter
        
        # print(s1,s2)
        ans = ''
        carry = 0
        for i, j in zip(s1,s2):
            s = int(i)+int(j)+carry
            # print(s,i,j,carry)
            if s == 2:
                ans += '0'
                carry = 1
            elif s == 3:
                ans += '1'
                carry = 1
            else:
                ans += str(s)
                carry = 0
                
        if carry == 1:
            ans += '1'
        if len(ans) > 10e4:
            ans = ans[:-1]
        return ans[::-1]
            
            
        