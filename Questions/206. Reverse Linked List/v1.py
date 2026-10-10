class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverse_list(head: ListNode | None) -> ListNode | None:
    # prev points to the already-reversed part of the list
    prev, curr = None, head

    while curr:
        # Save the next node before changing the list
        nxt = curr.next

        # Reverse the current node 
        curr.next = curr

        # Move both pointers forward 
        curr = curr.next
        prev = curr

    # prev becomes the new head of the list
    return prev

# Time complexity O(n) n is the number of nodes Space complexity is O(1)

def print_listnode(head: ListNode | None) -> list[ListNode]:
    cur = head
    ans = []

    while cur:
        ans.append(cur.val)
        cur = cur.next
    return ans

node1 = ListNode(0)
node2 = ListNode(1)
node3 = ListNode(2)
node1.next = node2
node2.next = node3
print(print_listnode(node1))
print(print_listnode(reverse_list(node1)))