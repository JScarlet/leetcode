# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        cur = ListNode(0)
        cur.next = head
        cur_ahead = ListNode(0)
        cur_ahead.next = cur
        while cur is not None and head is not None and head.next is not None:
            temp = head.next
            head.next = head.next.next
            temp.next = head
            head = temp
            cur.next = head
            # self.print_node(cur.next)
            cur = cur.next
            cur = cur.next
            head = head.next
            head = head.next

        return cur_ahead.next.next

    def print_node(self, node):
        if node is not None:
            print(node.val)
            self.print_node(node.next)


if __name__ == '__main__':
    solution = Solution()
    node_val_list = [1, 2, 3, 4]
    head = None
    for i in reversed(range(0, len(node_val_list))):
        temp = ListNode(node_val_list[i])
        temp.next = head
        head = temp
    solution.print_node(head)

    swapped = solution.swapPairs(head)
    solution.print_node(swapped)