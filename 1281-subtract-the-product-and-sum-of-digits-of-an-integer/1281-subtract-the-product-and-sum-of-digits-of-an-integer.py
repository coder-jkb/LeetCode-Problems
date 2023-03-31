class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod_dig = 1
        sum_dig = 0
        while n > 0:
            dig = n%10
            prod_dig *= dig
            sum_dig += dig
            n = n//10
            
        return prod_dig - sum_dig