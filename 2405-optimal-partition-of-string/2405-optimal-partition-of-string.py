class Solution:
    def partitionString(self, s: str) -> int:
        count = 1
        substr = ""
        for i in range(len(s)):
            ch = s[i]
            if ch not in substr:
                substr+=ch
            else:
                count+=1
                substr = ch
            # print(substr)     
        return count