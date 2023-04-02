class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        # s1, s2, s3 = nums[-3:]
        maxp = 0
        for i in range(len(nums)-1,1,-1):
            s1, s2, s3 = nums[i-2:i+1]
            if s1 + s2 > s3:
                # maxp = max(maxp, s1 + s2 + s3)
                return s1 + s2 + s3
                
        return 0