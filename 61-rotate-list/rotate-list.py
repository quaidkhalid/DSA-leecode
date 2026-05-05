# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Edge case: empty list or single node
        if not head or not head.next:
            return head
        
        # Step 1: Find length of the list
        l = 1
        tail = head
        while tail.next:
            tail = tail.next
            l += 1
        
        # Step 2: k = k % l
        k = k % l
        if k == 0:
            return head  # No rotation needed
        
        # Step 3: Connect tail node to head node (make it circular)
        tail.next = head
        
        # Step 4: Find new tail (last node of remaining nodes)
        # remain nodes = l - k
        remain = l - k
        new_tail = head
        for _ in range(remain - 1):
            new_tail = new_tail.next
        
        # Step 5: New head = new tail's next
        new_head = new_tail.next
        
        # Step 6: New tail's next = null (break the circle)
        new_tail.next = None
        
        # Step 7: Return new head
        return new_head
        