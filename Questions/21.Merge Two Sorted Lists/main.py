class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_two_lists(list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
    # Create a dummy node
    dummy = ListNode(-1)
    cur = dummy

    # Loop until one of the lists are empty
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    
    # Append the remaining nodes from the non-empty list
    cur.next = list1 if list1 else list2
    return dummy.next




node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(4)
node1.next = node2
node2.next = node3

node4 = ListNode(1)
node5 = ListNode(3)
node6 = ListNode(4)
node4.next = node5
node5.next = node6

node = merge_two_lists(node1, node4)

while node:
    print(node.val)
    node = node.next