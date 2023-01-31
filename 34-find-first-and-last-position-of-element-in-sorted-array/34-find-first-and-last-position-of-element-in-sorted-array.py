class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        ans = [-1,-1]
        if nums:
            # binary search target
            left, right = 0, len(nums)-1
            
            while left<=right:
                mid = (left+right)//2
                
                if nums[mid] == target:
                    # code here to get the first ans last index
                    i, j = mid, mid
                    
                    # decrement i while previous index of i points to target
                    while i-1>=0 and nums[i-1]==target:
                        i-=1
                        
                    # increment j while next index of j points to target
                    while j+1<=len(nums)-1 and nums[j+1]==target:
                        j+=1
                        
                    ans = [i,j]
                    return ans
                        
                elif target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            
        return ans