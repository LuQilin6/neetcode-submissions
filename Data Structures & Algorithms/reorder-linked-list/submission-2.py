# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: return
        i = 1
        mid, cur = head, head
        while cur.next:
            cur=cur.next
            i+=1
            if i % 2 == 1: 
                mid=mid.next

        second = mid.next
        mid.next = None
        lastNode=None
        while second:
            nextNode = second.next
            second.next = lastNode
            lastNode = second
            second = nextNode
        #self wrong implementation
        # lastNode=None
        # while mid.next:#3 4 5 -> 5 4 3
        #     nextNode = mid.next 
        #     mid.next=lastNode
        #     lastNode=mid
        #     mid = nextNode
        # mid.next = lastNode

        first = head
        second = lastNode
        while second:
            nextFrontNode = first.next #2 3 n
            nextBackNode=second.next #3 n n
            first.next=second
            second.next=nextFrontNode
            first = nextFrontNode
            second = nextBackNode

        #self wrong implementation
        # while head.next:#123n, 543n; 12n,432n ->second half is longer
        #     nextFrontNode = head.next
        #     nextBackNode=mid.next 
        #     head.next = mid 
        #     mid.next=nextFrontNode 
        #     head=nextFrontNode 
        #     mid=nextBackNode 


