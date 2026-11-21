# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1 2 3 4 5
        # 1 5 2 4 3
        if not head: return
        nodeStack=[]#1,2,3,4,5
        nodeStack.append(head)
        while head.next:
            print("in")
            head = head.next
            nodeStack.append(head)
        print("out")
        lenStack=len(nodeStack)
        for i in range(lenStack//2):
            #5 2+1
            print(f"i: {i}, correspond: {lenStack-i-1}")
            
            nodeStack[i].next = nodeStack[lenStack-i-1]
            nodeStack[lenStack-i-1].next = nodeStack[i+1]
            #[1,2] 1->2 2->2
            #[1,2,3,4] 1-4-2-3-3
            #[1,2,3,4,5] 1-5-2-4-3
        # if lenStack%2==0: 
        #     nodeStack[lenStack//2].next=None
        # else:
        nodeStack[lenStack//2].next=None
            
