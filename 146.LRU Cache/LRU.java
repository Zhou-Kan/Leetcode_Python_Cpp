import java.util.*;

class Node {
    public int key;
    public int val;
    public Node left;
    public Node right;
    public Node(int key, int val) {
        this.key = key;
        this.val = val;
        this.left = null;
        this.right = null;
    }
}

public class LRU {
    private int capacity;
    private Map<Integer, Node> keys;
    private Node head;
    private Node tail;

    public LRU(int capacity) {
        this.capacity = capacity;
        this.keys = new HashMap<>();
        this.head = new Node(-1, -1);
        this.tail = new Node(-1, -1);
        this.head.left = this.tail;
        this.tail.right = this.head;
    }

    private void remove(int key) {
        Node node = this.keys.get(key);
        node.left.right = node.right;
        node.right.left = node.left;
    }

    private void add(int key) {
        Node node = this.keys.get(key);
        Node temp = this.head.left;
        temp.right = node;
        node.left = temp;
        node.right = this.head;
        this.head.left = node;
    }

    public int get(int key) {
        if (!this.keys.containsKey(key)) {
            return -1;
        }
        remove(key);
        add(key);
        return this.keys.get(key).val;
    }

    public void put(int key, int value) {
        if (this.keys.containsKey(key)) {
            remove(key);
            add(key);
            this.keys.get(key).val = value;
        } else {
            Node node = new Node(key, value);
            this.keys.put(key, node);
            add(key);
            if (this.keys.size() > this.capacity) {
                Node lastNode = this.tail.right;
                this.keys.remove(lastNode.key);
                remove(lastNode.key);
            }
        }
    }

}
