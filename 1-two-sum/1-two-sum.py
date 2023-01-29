class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}
        for inx, num in enumerate(nums):
            difference = target-num
            if difference in visited:
                return [visited[difference], inx]

            visited[num] = inx