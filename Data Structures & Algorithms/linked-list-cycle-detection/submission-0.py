# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        if not head: return False

        nodeSet = set()
        # for n in head:
        curNode=head
        while curNode.next:
            if curNode in nodeSet: return True
            nodeSet.add(curNode)
            curNode=curNode.next
            # if curNode == n:
            #     return True

        return False
        