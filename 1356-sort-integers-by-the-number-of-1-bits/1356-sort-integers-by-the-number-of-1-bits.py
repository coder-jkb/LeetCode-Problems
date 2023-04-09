class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort()
        def count1(num):
            count = 0
            while num:
                count += num % 2 
                num = num >> 1
                
            return count
             
        ones = [ (n, count1(n)) for n in arr ]
        ones.sort(key=lambda x: x[1]) # sort by count of ones
         
        return list(map(lambda x:x[0],ones))