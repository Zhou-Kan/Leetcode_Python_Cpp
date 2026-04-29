class ListNode{
    val: number
    next : ListNode | null = null
    constructor(val: number) {
        this.val = val
    }
}
function mergeTwoLists(list1: ListNode | null, list2: ListNode | null): ListNode | null {
    const dummy = new ListNode(-1)
    let cur = dummy
    while (list1 && list2) {
        if (list1.val > list2.val) {
            cur.next = new ListNode(list2.val)
            list2 = list2.next
        } else {
            cur.next = new ListNode(list1.val)
            list1 = list1.next
        }
        cur = cur.next
    }
    if (list1) cur.next = list1
    if (list2) cur.next = list2
    return dummy.next
}