function ListNode(val) {
    this.val = val
    this.next = null
}

function reverse_list(head) {
    let cur = head, prev = null
    while (cur) {
        let nextNode = cur.next
        cur.next = prev
        prev = cur
        cur = nextNode
    }
    return prev
}