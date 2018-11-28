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
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next

        index = count // 2

        while index != 0:
            head = head.next
            index -= 1
        return head


if __name__ == '__main__':
    solution = Solution()
    node_list = [1, 2, 3, 4, 5]
    head = cur = ListNode(node_list[0])
    for i in range(1, len(node_list)):
        temp = ListNode(node_list[i])
        cur.next = temp
        cur = cur.next
    print(head)
    print(solution.middleNode(head))