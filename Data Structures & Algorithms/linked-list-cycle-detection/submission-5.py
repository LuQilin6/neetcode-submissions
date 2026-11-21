# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # if not head or not head.next or not head.next.next: return False
        pFast=head
        pSlow=head
        
        while pFast and pFast.next:
            pSlow=pSlow.next
            pFast=pFast.next.next
            if pSlow == pFast: return True
        return False
        # pFast=head.next.next
        # pSlow=head.next
        # while pFast and pSlow:
        #     if pFast == pSlow: return True
        #     if not pFast.next: return False
        #     pFast=pFast.next.next
        #     pSlow=pSlow.next

        # return False

        
        