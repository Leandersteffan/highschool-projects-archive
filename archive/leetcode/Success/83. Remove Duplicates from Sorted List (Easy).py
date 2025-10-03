# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return head
        clip = head.val
        dummy = head
        while head.next != None:
            if clip ==  head.next.val:
                head.next = head.next.next
            else:
                clip = head.next.val
                head = head.next
        return dummy
