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
                result += str(temp.val)
            temp = temp.next
        return result


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        result = head
        while head is not None:
            next = head.next
            if next is not None:
                if head.val == next.val:
                    head.next = next.next
                else:
                    head = head.next
            else:
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    node_list = [1, 1, 2, 3, 3]
    head = cur = ListNode(node_list[0])
    for i in range(1, len(node_list)):
        temp = ListNode(node_list[i])
        cur.next = temp
        cur = cur.next
    print(head)
    print(solution.deleteDuplicates(head))