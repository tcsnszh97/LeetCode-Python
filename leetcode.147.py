# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head:
            return None
        if not head.next:
            return head

        dummy = ListNode(float("-inf"))
        dummy.next = head
        pre = dummy
        tail = dummy
        cur = head

        while cur:
            if tail.val <= cur.val:
                tail = cur
                cur = cur.next
            else:
                tail.next = cur.next

                while pre and pre.next.val < cur.val:
                    pre = pre.next
                cur.next = pre.next
                pre.next = cur

                cur = tail.next
                pre = dummy
                
        return dummy.next