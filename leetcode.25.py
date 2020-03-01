# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        tail = dummy

        while True:
            count = k
            while count and tail:
                count -= 1
                tail = tail.next
            if not tail:
                break
            head = prev.next

            while prev.next != tail:
                curr = prev.next
                prev.next = curr.next
                curr.next = tail.next
                tail.next = curr

            prev = head
            tail = head

        return dummy.next