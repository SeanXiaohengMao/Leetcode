/**
 * Definition for singly-linked list with a random pointer.
 * class RandomListNode {
 *     int label;
 *     RandomListNode next, random;
 *     RandomListNode(int x) { this.label = x; }
 * };
 */
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        Map<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode tail = dummy;
        RandomListNode pointer = head;
        while (pointer != null) {
            tail.next = new RandomListNode(pointer.label);
            map.put(pointer, tail.next);
            tail = tail.next;
            pointer = pointer.next;
        }

        pointer = head;
        tail = dummy.next;
        while (pointer != null) {
            RandomListNode random = pointer.random;
            if (random != null) {
                tail.random = new RandomListNode(map.get(random).label);
            }

            tail = tail.next;
            pointer = pointer.next;
        }

        return dummy.next;
    }
}

// one pass
public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        Map<RandomListNode, RandomListNode> map = new HashMap<>();
        RandomListNode dummy = new RandomListNode(0);
        RandomListNode tail = dummy, newNode;

        while (head != null) {
            if (map.containsKey(head)) {
                newNode = map.get(head);
            }
            else {
                newNode = new RandomListNode(head.label);
                map.put(head, newNode);
            }

            if (head.random != null) {
                if (map.containsKey(head.random)) {
                    newNode.random = map.get(head.random);
                }
                else {
                    newNode.random = new RandomListNode(head.random.label);
                    map.put(head.random, newNode.random);
                }
            }

            tail.next = newNode;
            tail = tail.next;
            head = head.next;
        }

        return dummy.next;
    }
}
