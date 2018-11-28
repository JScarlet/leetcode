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
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head is None:
            return None
        while head is not None and head.val == val:
            head = head.next

        temp = head
        while temp is not None and temp.next is not None:
            if temp.next.val == val:
                temp.next = temp.next.next
            else:
                temp = temp.next
        return head


if __name__ == '__main__':
    solution = Solution()
    node_list = [1, 2, 3, 6, 4, 5, 6]
    head = cur = ListNode(node_list[0])
    for i in range(1, len(node_list)):
        temp = ListNode(node_list[i])
        cur.next = temp
        cur = cur.next
    print(head)
    val = 6
    print(solution.removeElements(head, val))