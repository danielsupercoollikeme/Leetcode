class ListNode(object):
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists_myself(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        head = ListNode()
        a = head
        while list1 and list2:
            if list1.val < list2.val:
                a.next = list1
                list1 = list1.next
            else:
                a.next = list2
                list2 = list2.next
            a = a.next

        a.next = list1 or list2
        return head.next