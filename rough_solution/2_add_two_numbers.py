# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l1_str = ''
        while l1 is not None:
            l1_str += str(l1.val)
            l1 = l1.next

        l2_str = ''
        while l2 is not None:
            l2_str += str(l2.val)
            l2 = l2.next
        l1_num = int(l1_str[::-1])
        l2_num = int(l2_str[::-1])
        count = str(l1_num + l2_num)

        root = None
        for i in range(0, len(count)):
            temp = ListNode(int(count[i]))
            temp.next = root
            root = temp
        return root

    def printNode(self, root):
        result = ''
        while root is not None:
            if root.next is not None:
                result += str(root.val) + '->'
            else:
                result += str(root.val)
            root = root.next
        print(result)


if __name__ == '__main__':
    solution = Solution()
    first = ListNode(2)
    second = ListNode(4)
    third = ListNode(3)
    first.next = second
    second.next = third

    first2 = ListNode(5)
    second2 = ListNode(6)
    third2 = ListNode(4)
    first2.next = second2
    second2.next = third2

    solution.printNode(first)
    solution.printNode(first2)
    root = solution.addTwoNumbers(first, first2)
    solution.printNode(root)