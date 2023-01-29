class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if len(strs) > 0:
            newstrs = sorted(strs)
            s1, s2 = newstrs[0], newstrs[-1]
            prevCharsMatch = True
            for ch1, ch2 in zip(s1, s2):
                print(ch1,ch2)
                if prevCharsMatch and ch1==ch2 :
                    prefix+=ch1
                else:
                    prevCharsMatch = False
            return prefix
        return ""