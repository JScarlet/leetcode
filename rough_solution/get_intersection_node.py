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
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        A_list = []
        B_list = []
        tempA = headA
        tempB = headB
        while tempA is not None:
            A_list.append(tempA)
            tempA = tempA.next

        while tempB is not None:
            B_list.append(tempB)
            tempB = tempB.next

        A_list = A_list[::-1]
        B_list = B_list[::-1]

        count = 0
        for i in range(0, min(len(A_list), len(B_list))):
            if A_list[i].val != B_list[i].val:
                break
            else:
                count += 1
        if count == 0:
            return None
        else:
            return A_list[count-1]


if __name__ == '__main__':
    solution = Solution()
    node_list_A = [1, 2, 3, 4, 5]
    node_list_B = [7, 8, 3, 4, 5]
    head_A = cur_A = ListNode(node_list_A[0])
    for i in range(1, len(node_list_A)):
        temp_A = ListNode(node_list_A[i])
        cur_A.next = temp_A
        cur_A = cur_A.next
    print(head_A)

    head_B = cur_B = ListNode(node_list_B[0])
    for i in range(1, len(node_list_B)):
        temp_B = ListNode(node_list_B[i])
        cur_B.next = temp_B
        cur_B = cur_B.next
    print(head_B)
    print(solution.getIntersectionNode(head_A, head_B))