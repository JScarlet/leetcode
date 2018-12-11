class Solution:
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B):
            return False
        new_A = A + A
        if B in new_A:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    A = 'abcde'
    B = 'abced'
    print(solution.rotateString(A, B))