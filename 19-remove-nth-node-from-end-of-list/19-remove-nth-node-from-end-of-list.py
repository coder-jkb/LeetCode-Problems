# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # delete the only element in liked list
        if head.next == None:
            return None # empty linked list
        
        length = 0
        p = head
        while p: # finding length
            length+=1
            p=p.next
            
        if length == n: # delete the head itself
            return head.next
            
        p1 = head
        p2 = head.next
        
        # traverse p1 and p2 such that p2 reaches the element to be deleted
        # p1 is previous to p2
        # p1.next will point p2.next
        # for this we will p1 and p2, length-n-1 times
        count = length-n-1
        while count > 0:
            p1 = p2
            p2 = p2.next
            count-=1
            
        p1.next = p2.next
        return head