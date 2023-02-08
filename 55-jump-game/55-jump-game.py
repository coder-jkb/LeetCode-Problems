class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_inx = 0
        for inx in range(len(nums)):
            if inx > max_inx:
                return False
            
            max_inx = max(inx+nums[inx], max_inx)
            
        return True
                
