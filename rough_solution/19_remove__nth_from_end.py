# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        cur = head
        reversed_node = None
        while cur is not None:
            temp = ListNode(cur.val)
            temp.next = reversed_node
            reversed_node = temp
            cur = cur.next

        # self.print_node(head)
        # self.print_node(cur)
        count = 0
        while reversed_node is not None:
            count += 1
            if count != n:
                temp = ListNode(reversed_node.val)
                temp.next = cur
                cur = temp
            reversed_node = reversed_node.next
        return cur

    def print_node(self, head):
        if head is not None:
            print(head.val)
            self.print_node(head.next)


if __name__ == '__main__':
    solution = Solution()
    node_val_list = [1, 2, 3, 4, 5]
    head = None
    for i in reversed(range(0, len(node_val_list))):
        temp = ListNode(node_val_list[i])
        temp.next = head
        head = temp
    n = 2

    # solution.print_node(head)
    deleted = solution.removeNthFromEnd(head, n)
    solution.print_node(deleted)