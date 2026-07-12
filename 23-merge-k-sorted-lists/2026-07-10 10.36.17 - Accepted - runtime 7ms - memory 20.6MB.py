# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[Optional[ListNode]]
        :rtype: Optional[ListNode]
        """
        l = []
        for  head in  lists:
            while(head != None):
                l.append(head.val)
                head = head.next
        l.sort()
        result = ListNode(0)
        curr = result
        for num in l:
            curr.next = ListNode(num)
            curr = curr.next
        return result.next

            
        