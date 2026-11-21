# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        if not head: return
        nodeList=[]
        nodeList.append(head)
        while head.next:
            print("in")
            head = head.next
            nodeList.append(head)
        print("out")
        lenList=len(nodeList)
        for i in range(lenList//2):
            nodeList[i].next = nodeList[lenList-i-1]
            nodeList[lenList-i-1].next = nodeList[i+1]
            #[1,2] 1->2 2->2
            #[1,2,3,4] 1-4-2-3-3
            #[1,2,3,4,5] 1-5-2-4-3

        nodeList[lenList//2].next=None
            
