class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_inx = 0
        for inx, jump in enumerate(nums):
            if inx > max_inx:
                return False
            max_inx = max(inx+jump, max_inx)
            
        return True
                
