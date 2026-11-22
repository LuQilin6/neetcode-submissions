# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #reimplementation on the second day
        if not head or not head.next: return
        fast, slow = head, head 
        while fast.next and fast.next.next: #1 2 3 4
            fast=fast.next.next
            slow = slow.next
        
        secondHalf = slow.next #3
        slow.next = None
        
        lastNode = None
        while secondHalf.next:
            nextNode = secondHalf.next #4
            secondHalf.next = lastNode
            lastNode=secondHalf
            secondHalf=nextNode
        secondHalf.next = lastNode

        while head and secondHalf:
            nextFront = head.next
            nextBack = secondHalf.next
            head.next = secondHalf
            secondHalf.next = nextFront
            head = nextFront
            secondHalf = nextBack
        