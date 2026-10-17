# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head # tow pointers with different speed
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow: # if there is a cycle, those two will meet at some point
                return True
        return False
        