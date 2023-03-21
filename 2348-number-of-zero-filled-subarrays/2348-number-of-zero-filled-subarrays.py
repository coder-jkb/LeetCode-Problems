class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:

        def num_of_subarrays(n):
            return n*(n+1)/2
        
        i=0; j=1
        
        ans = 0
        count_cont_zeros = 0 # count of contiguous zeros
        for i in range(len(nums)):
            if nums[i] == 0:
                count_cont_zeros+=1
                
            else: # no more contiguous zeros
                ans += num_of_subarrays(count_cont_zeros)
                count_cont_zeros = 0
        
        if count_cont_zeros > 0:
            ans += num_of_subarrays(count_cont_zeros)
                
        return int(ans)
        