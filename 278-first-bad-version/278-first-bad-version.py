# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l = 0
        r = n-1
        calls = 0
        while l<=r:
            mid = (l+r)//2
            # print(l,r,mid)
            bad_adj = isBadVersion(mid), isBadVersion(mid+1)
            calls +=2
            if not bad_adj[0] and bad_adj[1]:
                return mid+1
            
            elif bad_adj[0] and bad_adj[1]:
                r = mid-1
                
            else:
                l = mid+1  
            
            
            
            
            