/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int carry = 0;
        int sum = 0;
        ListNode dummy = new ListNode(0);
        ListNode tail = dummy;
        while (l1 != null || l2 != null) {
            int x, y;
            if (l1 != null) {
                x = l1.val;
            }
            else {
                x = 0;
            }

            if (l2 != null) {
                y = l2.val;
            }
            else {
                y = 0;
            }

            sum = x + y + carry;
            carry = sum / 10;

            tail.next = new ListNode(sum % 10);
            tail = tail.next;

            if (l1 != null) {
                l1 = l1.next;
            }

            if (l2 != null) {
                l2 = l2.next;
            }
        }

        if (carry > 0) {
            tail.next = new ListNode(carry);
        }

        return dummy.next;
    }
}
