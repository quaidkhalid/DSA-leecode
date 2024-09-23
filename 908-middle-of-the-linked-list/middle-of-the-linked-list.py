# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None or head.next == None:
            return head

        slow = head
        fast = head.next

        while fast != None:
            fast = fast.next
            if fast != None:
                fast = fast.next
            slow = slow.next
        return slow

        