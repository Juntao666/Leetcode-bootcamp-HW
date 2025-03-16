# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head
        prev = slow
        while fast != None:
            prev = slow
            slow = slow.next
            fast = fast.next
            if fast == None:
                break
            fast = fast.next
        prev.next = None

        prev = None
        curr = slow
        while curr != None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        second = prev
        first = head
        while second != None:
            nxt1 = first.next
            nxt2 = second.next
            first.next = second
            second.next = nxt1
            first = nxt1
            second = nxt2
        return head