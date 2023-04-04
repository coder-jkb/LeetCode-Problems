class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        nums = []
        l1, l2 = len(nums1), len(nums2)
        while i<l1 and j<l2:
            if nums1[i] < nums2[j]:
                nums.append(nums1[i])
                i+=1
                
            else:
                nums.append(nums2[j])
                j+=1
                
        if i < l1:
            nums.extend(nums1[i:])
            
        if j < l2:
            nums.extend(nums2[j:])
            
        l = len(nums)
        if l%2 == 0:
            return (nums[l//2 - 1] + nums[l//2])/2
        else:
            return nums[l//2]