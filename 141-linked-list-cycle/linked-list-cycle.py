# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        small = head
        fast = head
        while fast and fast.next:
            small = small.next
            fast = fast.next.next
            if small == fast:
                return True
        return False
        