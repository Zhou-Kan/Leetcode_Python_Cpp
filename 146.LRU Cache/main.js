class Node{
    key
    val
    left = null
    right = null
    constructor(key, val) {
        this.key = key
        this.val = val
    }
}

class LRUCache{
    capacity
    keys = new Map()
    head = new Node(-1, -1)
    tail = new Node(-1, -1)
    constructor(capacity) {
        this.capacity = capacity
        this.head.left = this.tail
        this.tail.right = this.head
    }
}