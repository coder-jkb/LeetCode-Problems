class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        length = len(arr)
        # if length == 2:
        #     return True
        
        arr.sort()
        for i in range(1,length-1):
            if arr[i] - arr[i-1] != arr[i+1] - arr[i]:
                return False
            
        return True