import math
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

test = [1,2,3,4,5]
head = None
for i in range(len(test) - 1, 0, -1):
    if head is None:
        head = ListNode(test[i])
    if i - 1 >= 0:
        last = ListNode(test[i-1], head)
        head = last

solution = Solution()
print(solution.middleNode(head))