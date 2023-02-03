class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        if digits[-1] < 8:
            digits[-1] += 1
        else:
            i = len(digits)-1
            while digits[i] == 9:
                digits[i] = 0
                i-=1
            if i >= 0:
                digits[i]+=1
            else:
                digits.insert(0,1)

        return digits