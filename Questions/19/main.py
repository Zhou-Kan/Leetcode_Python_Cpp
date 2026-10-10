class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
def remove_nth_from_end(head: ListNode | None, n: int) -> ListNode | None:

    # Set a dummy node pointing to the head node
    dummy = ListNode(0, head)

    # Locate the position jsut before the node we need to remove
    slow, fast = dummy, dummy
    for _ in range(n):
        fast = fast.next
    
    while fast.next:
        fast = fast.next
        slow = slow.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next


    