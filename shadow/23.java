/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    private Comparator<ListNode> comparator = new Comparator<ListNode>() {
        public int compare(ListNode l1, ListNode l2) {
            return l1.val - l2.val;
        }
    };

    public ListNode mergeKLists(ListNode[] lists) {
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;
        if (lists == null) {
            return dummy.next;
        }

        Queue<ListNode> queue = new PriorityQueue<>(comparator);
        for (int i = 0; i < lists.length; i++) {
            if (lists[i] != null) {
                queue.offer(lists[i]);
            }
        }

        while (!queue.isEmpty()) {
            ListNode node = queue.poll();
            tail.next = new ListNode(node.val);
            if (node.next != null) {
                queue.offer(node.next);
            }
            tail = tail.next;
        }

        return dummy.next;
    }
}

class Solution {
    public ListNode mergeKLists(ListNode[] lists) {
        if (lists == null || lists.length == 0) {
            return null;
        }

        return helper(lists, 0, lists.length - 1);
    }

    private ListNode helper(ListNode[] lists, int start, int end) {
        if (start == end) {
            return lists[start];
        }

        int mid = start + (end - start) / 2;
        ListNode left = helper(lists, start, mid);
        ListNode right = helper(lists, mid + 1, end);

        return mergeTwoLists(left, right);
    }

    private ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode dummy = new ListNode(-1);
        ListNode tail = dummy;

        while (l1 != null & l2 != null) {
            if (l1.val < l2.val) {
                tail.next = l1;
                l1 = l1.next;
            }
            else {
                tail.next = l2;
                l2 = l2.next;
            }

            tail = tail.next;
        }

        if (l1 != null) {
            tail.next = l1;
        }

        if (l2 != null) {
            tail.next = l2;
        }

        return dummy.next;
    }
}
