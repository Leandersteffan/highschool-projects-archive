# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = l3 = ListNode(0)
        while True:
            if list1 and list2:
                if list1.val <= list2.val:
                    #l3.next = ListNode(list1.val)  # Beides Möglich
                    l3.next = list1                 # Beides Möglich
                    list1 = list1.next
                elif list1.val > list2.val:
                    l3.next = ListNode(list2.val)
                    list2 = list2.next
            elif list1 and not list2:
                l3.next = ListNode(list1.val)
                list1 = list1.next
            elif list2 and not list1:
                l3.next = ListNode(list2.val)
                list2 = list2.next
            else:
                return dummy.next
            l3 = l3.next
        
        
        
        
        '''dummy = temp = ListNode(0)
        while list1 != None and list2 != None:

            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else: 
                temp.next = list2
                list2 = list2.next
            temp = temp.next
        temp.next = list1 or list2 
        return dummy.next'''
