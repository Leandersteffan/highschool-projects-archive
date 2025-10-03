# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        original = head
        length = 0
        while head:
            length += 1
            head = head.next
        if n == length:
            if length == 1:
                return ListNode(val='')
            return original.next
        executer = ListNode(original.val)
        dummy = executer
        for i in range(length - n - 1):
            original = original.next
            executer.next = ListNode(original.val)
            executer = executer.next
        if n > 1:
            original = original.next.next
            executer.next = ListNode(original.val)
            executer = executer.next
            for i in range(n - 2):
                original = original.next
                executer.next = ListNode(original.val)
                executer = executer.next
        return dummy
