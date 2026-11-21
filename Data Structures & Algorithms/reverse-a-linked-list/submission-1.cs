/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int val=0, ListNode next=null) {
 *         this.val = val;
 *         this.next = next;
 *     }
 * }
 */
 
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head == null){
            return head;
        }
        ListNode nextNode= head.next;
        ListNode prev = head;
        head.next = null;
        while(nextNode!= null){
            
            ListNode temp = nextNode.next;
            nextNode.next = prev;
            prev = nextNode;
            nextNode = temp;
        }
        return prev;
    }
}
