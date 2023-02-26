class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # nums.sort() # one liner solution in python
        i=0; left=0; right=len(nums)-1
        
        def swap(a,b):
            nums[a], nums[b] = nums[b], nums[a]
            
        while i<=right:
            if nums[i]==0:
                swap(i,left)
                i+=1; left+=1
                
            elif nums[i]==1:
                i+=1
            
            else:
                swap(i,right)
                right-=1