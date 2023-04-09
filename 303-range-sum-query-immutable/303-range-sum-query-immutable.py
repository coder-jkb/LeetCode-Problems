class NumArray:

    def __init__(self, nums: List[int]):
        self.N = [nums[0]]
        for n in nums[1:]:
            self.N.append(self.N[-1]+n)

    def sumRange(self, left: int, right: int) -> int:
        if left == 0:
            return self.N[right]
        
        return self.N[right] - self.N[left-1]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)