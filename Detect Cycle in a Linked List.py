# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def has_cycle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next         # move 1 step
        fast = fast.next.next    # move 2 steps

        if slow == fast:
            return True  # cycle detected

    return False  # reached end, no cycle
