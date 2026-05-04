public class Solution {
    class Node{
        int val;
        Node next;
        Node() {};
        Node(int val) {
            this(val, null);
        }
        Node(int val, Node next) {
            this.val = val;
            this.next = next;
        }
    }

    public Node mergeTwoLists(Node list1, Node list2) {
        Node dummy = new Node(-1);
        Node cur = dummy;
        Node cur1 = list1, cur2 = list2;

        while (cur1 != null && cur2 != null) {
            if (cur1.val > cur2.val) {
                cur.next = new Node(cur2.val);
                cur2 = cur2.next;
            } else {
                cur.next = new Node(cur1.val);
                cur1 = cur1.next;
            }
            cur = cur.next;
        }
        if (cur1 != null) cur.next = cur1;
        if (cur2 != null) cur.next = cur2;
        return dummy.next;
    }
    
}
