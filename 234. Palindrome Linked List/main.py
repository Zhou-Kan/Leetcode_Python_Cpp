class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def is_palindrome(head: ListNode | None) -> bool:
    if not head:
        return True
    
    # locate the middile node of the linked list
    slow = head 
    fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    half_node = slow
    second_head = slow.next

    # reverse the first part of the linked list
    prev = None
    cur = head
    while cur != second_head:
        next_node = cur.next
        cur.next = prev
        prev = cur
        cur = next_node
    
    # check 
    first_head = prev
    while second_head:
        if first_head.val != second_head.val:
            return False
        first_head = first_head.next
        second_head = second_head.next

    return True


node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(1)
node4 = ListNode(0)
node1.next = node2
node2.next = node3
node3.next = node4
print(is_palindrome(node1))