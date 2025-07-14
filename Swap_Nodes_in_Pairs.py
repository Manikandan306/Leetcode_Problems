# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy

        while head and head.next:
            first = head
            second = head.next

            # Swap
            prev.next = second
            first.next = second.next
            second.next = first

            # Move forward
            prev = first
            head = first.next

        return dummy.next
