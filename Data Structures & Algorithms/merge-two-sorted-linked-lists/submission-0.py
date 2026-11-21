# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        cur = ListNode()
        head=cur

        while True:
            l1value = list1.val
            l2value = list2.val
            if l1value<=l2value:
                cur.next=list1
                cur=cur.next
                if list1.next: 
                    list1=list1.next
                else:
                    cur.next=list2
                    return head.next
            else:
                cur.next=list2
                cur=cur.next
                if list2.next: 
                    list2=list2.next
                else:
                    cur.next=list1
                    # print(head)
                    return head.next


