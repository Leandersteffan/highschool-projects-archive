
'slow'

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        head_list = []
        while head:
            head_list.append(head.val)
            head = head.next
        if len(head_list) <= 1:
            return ListNode(val='')
        pos = int(len(head_list) / 2)
        head_list.pop(pos)
        dummy = out = ListNode(head_list[0])
        for i in range(1, len(head_list)):
            out.next = ListNode(head_list[i])
            out = out.next
        return dummy


'even slower'
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        original = head
        length = 0
        while head:
            length += 1
            head = head.next
        if length <= 1:
            return ListNode(val='')
        executer = ListNode(original.val)
        dummy = executer
        for i in range(int(length / 2) - 1):
            original = original.next
            executer.next = ListNode(original.val)
            executer = executer.next
        print(dummy)
        if int(length / 2) + 1 < length:
            original = original.next.next
            executer.next = ListNode(original.val)
            executer = executer.next
            print(dummy)
            if int(length / 2) + 2 < length and length % 2 != 0:
                for i in range(length - int(length / 2) + 1, length):
                    original = original.next
                    executer.next = ListNode(original.val)
                    executer = executer.next
                    print(dummy)
            elif int(length / 2) + 2 < length and length % 2 == 0:
                for i in range(length - int(length / 2) + 2, length):
                    original = original.next
                    executer.next = ListNode(original.val)
                    executer = executer.next
        return dummy
