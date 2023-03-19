# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid, j = head, head
        while j.next:
            mid = mid.next
            j = j.next
            if j.next:
                j = j.next
                
            
        if j.next == None:
            return mid
        
        else:
            return mid.next
        