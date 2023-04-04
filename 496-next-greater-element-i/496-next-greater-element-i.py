class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2len = len(nums2)
        ans = []
            
        for num in nums1:
            index = nums2.index(num)
            
            i = index+1
            while i < nums2len:
                if nums2[i] > num:
                    ans.append(nums2[i])
                    break
                else:
                    i+=1
                
            if i==nums2len:
                ans.append(-1)
                
        return ans
        
        