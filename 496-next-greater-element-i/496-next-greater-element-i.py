class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums2i = {}
        nums2len = len(nums2)
        ans = []
        for i, num in enumerate(nums2):
            nums2i[num] = i
            
        for num in nums1:
            index = nums2i[num]
            
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
        
        