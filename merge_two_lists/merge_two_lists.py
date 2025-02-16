# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def list_to_linked_list(self, lst):
        if not lst:
            return None
        head = ListNode(lst[0])
        current = head
        for val in lst[1:]:
            current.next = ListNode(val)
            current = current.next
        return head

    def linked_list_to_list(self, head) -> list:
        result = []
        while head:
            result.append(head.val)
            head = head.next
        return result
        
    def merge_two_lists(self, list1: list[int], list2: list[int]) -> list:
        list1 = self.list_to_linked_list(list1)
        list2 = self.list_to_linked_list(list2)

        newList = ListNode(-1)
        current = newList

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next
        current.next = list1 if list1 else list2

        return self.linked_list_to_list(newList.next)



obj = Solution()

list1 = [2,4,8,9]
list2 = [1,3,4,5,8,9,10]

result = obj.merge_two_lists(list1, list2)

print(result)
