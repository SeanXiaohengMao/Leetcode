/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode dummy = new ListNode(0);
        dummy.next = head;
        ListNode prev = dummy;

        while (head != null) {
            ListNode temp = head.next;
            prev.next = temp;
            insert(head, dummy, temp);
            if (prev.next != temp) {
                prev = prev.next;
            }
            head = temp;
        }

        return dummy.next;
    }

    private void insert(ListNode head, ListNode pointer, ListNode tail) {
        while (pointer.next != tail) {
            if (pointer.next.val < head.val) {
                pointer = pointer.next;
            }
            else {
                ListNode temp = pointer.next;
                pointer.next = head;
                head.next = temp;
                return;
            }
        }
        ListNode temp = pointer.next;
        pointer.next = head;
        head.next = temp;

    }
}
