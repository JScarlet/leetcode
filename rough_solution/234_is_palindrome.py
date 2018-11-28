# Definition for singly-linked list.
class ListNode:
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
                result += str(temp.val) + '->NULL'
            temp = temp.next
        return result

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # reverse = None
        # cur = head
        # while cur is not None:
        #     temp = ListNode(cur.val)
        #     cur = cur.next
        #     temp.next = reverse
        #     reverse = temp
        #
        # while reverse is not None and head is not None:
        #     if reverse.val == head.val:
        #         reverse = reverse.next
        #         head = head.next
        #     else:
        #         return False
        # return True
        result = []
        while head is not None:
            result.append(head.val)
            head = head.next
        return result == result[::-1]


if __name__ == '__main__':
    solution = Solution()
    node_list = [1, 1, 2, 1]
    head = cur = ListNode(node_list[0])
    for i in range(1, len(node_list)):
        temp = ListNode(node_list[i])
        cur.next = temp
        cur = cur.next
    print(head)
    print(solution.isPalindrome(head))