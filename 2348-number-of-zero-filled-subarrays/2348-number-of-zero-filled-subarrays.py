class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        ans = 0
        count = 0 # count of contiguous zeros
        for i in range(len(nums)):
            if nums[i] == 0:
                count+=1
                
            else: # no more contiguous zeros
                ans += count*(count+1)//2
                count = 0
        
        if count > 0:
            ans += count*(count+1)//2
                
        return ans
        