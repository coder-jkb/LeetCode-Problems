class Solution:
    def interpret(self, command: str) -> str:
        ans = ""
        i=0
        while i < len(command):
            c = command[i]
            if c=='G':
                ans+='G'
                i+=1
                
            elif c=='(' and command[i+1] == ')':
                ans+='o';
                i+=2
                
            elif c=='(' and command[i+1] == 'a':
                ans+='al'
                i+=4
                
        return ans
            
            