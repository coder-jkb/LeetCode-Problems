class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_bal = float('-inf')
        for i, bal in enumerate(accounts):
            sum_bal = sum(bal)
            if sum_bal > max_bal:
                max_bal = sum_bal
                
        return max_bal
                
                
                