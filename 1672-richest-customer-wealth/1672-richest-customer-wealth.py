class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        max_bal = float('-inf')
        for i, bal in enumerate(accounts):
            max_bal = max(sum(bal), max_bal)
                
        return max_bal
                
                
                