class ListNode:
    def __init__(self, val: int, next: ListNode | None = None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode | None) -> ListNode | None:
    cur, prev = head, prev
    while cur:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    return prev
