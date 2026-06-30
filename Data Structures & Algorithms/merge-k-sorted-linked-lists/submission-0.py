# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # out = None
        # for list_ in lists:
        #     out = self.merge2Lists(out, list_)
        # return out
        
        if not len(lists):
            return None
        
        groupSize = 2
        while groupSize <= len(lists)*2:
            for i in range(0, len(lists), groupSize):
                if i+groupSize//2 >= len(lists): 
                    break
                lists[i] = self.merge2Lists(lists[i], lists[i+groupSize//2])
            groupSize *= 2
        return lists[0]




    def merge2Lists(self, list1, list2):
        curr1 = list1
        curr2 = list2

        if not curr1 and not curr2:
            return None
        if not curr1: return curr2
        if not curr2: return curr1

        if curr1.val < curr2.val:
            out = curr1
            curr1 = curr1.next
        else:
            out = curr2
            curr2 = curr2.next

        curr = out
        while curr1 and curr2:
            if curr1.val < curr2.val:
                curr.next = curr1
                curr = curr1
                curr1 = curr1.next
            else:
                curr.next = curr2
                curr = curr2
                curr2 = curr2.next
        if curr1:
            curr.next = curr1
        if curr2:
            curr.next = curr2
        return out