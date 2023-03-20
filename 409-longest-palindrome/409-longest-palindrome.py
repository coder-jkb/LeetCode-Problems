class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        max_palindrome_length = 0
#       get count of each element in list
        for ch in s:
            if ch in count:
                count[ch]+=1
            else:
                count[ch] = 1

                
        odd = False
        
        for c in count.values():
            if c%2==0: # add even
                max_palindrome_length +=c
                
            else: # odd
                odd = True    
                max_palindrome_length += c-1
                
            # else:
            #     one = True
                
        if odd:
            max_palindrome_length+=1
            
        return max_palindrome_length