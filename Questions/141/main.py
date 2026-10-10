class ListNode:
    def __init__(self, val=0):
        self.val = val
        self.next = next

def has_cycle(head: ListNode | None) -> bool:
    if not head:
        return False
    
    # create a hash set to track if the node exists
    vis = set()
    cur = head
    while cur:
        if cur in vis:
            return True
        vis.add(cur)
        cur = cur.next

    return False



node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node1
print(has_cycle(node1))


        