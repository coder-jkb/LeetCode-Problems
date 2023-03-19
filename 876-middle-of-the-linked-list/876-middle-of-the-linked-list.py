# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid, j = head, head
        while j and j.next:
            mid = mid.next
            j = j.next.next
        
        return mid