/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (head != null && head.next != null) {
            ListNode temp = head.next.next;
            prev.next = head.next;
            prev.next.next = head;
            head.next = temp;

            prev = head;
            head = head.next;
        }

        return dummy.next;
    }
}
