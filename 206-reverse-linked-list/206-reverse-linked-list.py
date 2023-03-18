# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

# \<-1  2->3->4->5->\
#    p  c  n
#       
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        prev = None
        
        while curr:
            new = curr.next
            curr.next = prev
            prev = curr
            curr = new
            
        return prev