class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # finding the index after which element decreases
        l, r = 0, len(nums)-1
        while l<=r:
            mid = (l+r)//2
            if nums[mid]==target:
                return mid
            
            # left sorted part
            if nums[l] <= nums[mid]:
                
            # if target is greater than mid then we search in right part
            # if our target is less than left then also we search in right part
                if target > nums[mid] or target < nums[l]:
                    l = mid+1
                    
            # otherwise target is less than mid but greater than left
            # we search in left of mid
                else:
                    r = mid-1
            
            # right sorted part
            else:
                # if target is less than mid we search in left part
                # if target is greater than right then we search in the left part
                if target < nums[mid] or target > nums[r]:
                    r = mid-1
                
                # otherwise target is less than mid but greater than left
                # we search in left of mid
                else:
                    l = mid+1
                    
        return -1
            