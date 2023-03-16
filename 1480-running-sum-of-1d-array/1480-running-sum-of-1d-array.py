class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        new = []
        for n in nums:
            s = s+n
            new.append(s)
            
        return new