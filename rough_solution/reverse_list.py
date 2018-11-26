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
                result += str(temp.val) + '->NULL'
            temp = temp.next
        return result

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return None
        result = ListNode(head.val)
        head = head.next
        while head is not None:
            # print(result)
            temp = head
            head = head.next
            temp.next = result
            result = temp

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
    print(solution.reverseList(head))