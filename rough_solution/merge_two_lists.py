# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        result = ''
        temp = self
        while temp is not None:
            if temp.next is not None:
                result += str(temp.val) + '->'
            else:
                result += str(temp.val)
            temp = temp.next
        return result

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = temp = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val <= l2.val:
                temp.next = l1
                temp = temp.next
                l1 = l1.next
            else:
                temp.next = l2
                temp = temp.next
                l2 = l2.next
        temp.next = l1 or l2
        return head.next


if __name__ == '__main__':
    solution = Solution()
    list1 = [1, 2, 4]
    list2 = [1, 3, 4]
    l1 = ListNode(list1[-1])
    for i in range(1, len(list1)):
        temp = ListNode(list1[len(list1) - 1 - i])
        temp.next = l1
        l1 = temp
    l2 = ListNode(list2[-1])
    for i in range(1, len(list2)):
        temp = ListNode(list2[len(list2) - 1 - i])
        temp.next = l2
        l2 = temp
    # print(l1)
    # print(l2)
    print(solution.mergeTwoLists(l1, l2))

    first = second = ListNode(0)
    temp = ListNode(1)
    second.next = temp
    print(first)
    print(second)