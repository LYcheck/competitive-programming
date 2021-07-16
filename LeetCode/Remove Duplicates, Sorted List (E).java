 public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
}
 
class Solution {
    public ListNode deleteDuplicates(ListNode head) {
    
        if (head == null) {
            return null;
        }

        ListNode cur1 = head;
        ListNode cur2 = head;

        while (cur2 != null) {
            if (cur1.val != cur2.val) {
                cur1.next = cur2;
                cur1 = cur2;
            }
            cur2 = cur2.next;
        }

        cur1.next = null;

        return head;
    }
}