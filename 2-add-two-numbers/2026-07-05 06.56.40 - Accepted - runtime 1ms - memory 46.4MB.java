/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
       ListNode p1 = l1;   
       ListNode p2 = l2; 
       ListNode head = new ListNode(0);  
       ListNode current = head;
       int sum;
       int c=0;
       while(p1!=null && p2!=null){
            sum = p1.val + p2.val + c;
            c=sum/10;
            
           current.next = new ListNode(sum%10);
            current = current.next;
            p1 = p1.next;
            p2 = p2.next;
       }
       while(c>0 || p1!=null || p2!=null){
       int x = p1 != null ? p1.val : 0;  
       int y = p2 != null ? p2.val : 0;  
    
        sum = x + y + c;
        current.next = new ListNode(sum % 10);
         c = sum / 10;
    
    
        if(p1 != null) p1 = p1.next;
        if(p2 != null) p2 = p2.next;
        current = current.next;
       }
        
       return head.next;
    }
}