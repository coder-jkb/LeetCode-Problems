class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BS(l,r,target):
            if l > r:
                return -1
            
            mid = (l+r)//2

            if nums[mid] == target:
                return mid
            
            elif nums[mid] > target: # left half
                return BS(l, mid-1, target)
            
            # right half
            return BS(mid+1, r, target)
        
        return BS(0, len(nums)-1, target)