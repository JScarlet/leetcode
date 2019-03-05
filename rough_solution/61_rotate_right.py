# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        depth = 1
        while cur.next is not None:
            depth += 1
            cur = cur.next
        right_rotate = k % depth
        left_rotate = depth - right_rotate
        tail = cur
        cur.next = head
        cur = head
        for i in range(0, left_rotate):
            cur = cur.next
            tail = tail.next
        tail.next = None
        return cur

    def print_node_list(self, head):
        result = ''
        temp = head
        while temp is not None:
            if temp.next is not None:
                result += str(temp.val) + '->'
            else:
                result += str(temp.val) + '->NULL'
            temp = temp.next
        print(result)


if __name__ == '__main__':
    solution = Solution()
    node_list = [1, 2, 3, 4, 5]
    head = None
    for i in reversed(range(0, len(node_list))):
        node = ListNode(node_list[i])
        node.next = head
        head = node
    rotated = solution.rotateRight(head, 2)
    solution.print_node_list(rotated)