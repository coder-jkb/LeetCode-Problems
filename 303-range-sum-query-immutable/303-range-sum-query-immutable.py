class NumArray:

    def __init__(self, nums: List[int]):
        self.N = nums

    def sumRange(self, left: int, right: int) -> int:
        return sum(self.N[left:right])+self.N[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)