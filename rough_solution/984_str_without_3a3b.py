class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A > B:
            if A == 2 * B + 2:
                return 'aa' + 'baa' * B
            elif A < 2 * B + 2:
                temp = ''
                while A > B > 0:
                    temp += 'aab'
                    A -= 2
                    B -= 1
                if B == 0:
                    temp += 'a' * A
                    return temp
                if A == B:
                    temp += 'ab' * A
                return temp
        elif A < B:
            if B == 2 * A + 2:
                return 'bb' + 'abb' * A
            elif B < 2 * A + 2:
                temp = ''
                while B > A > 0:
                    temp += 'bba'
                    B -= 2
                    A -= 1
                if A == 0:
                    temp += 'b' * B
                    return temp
                if A == B:
                    temp += 'ba' * B
                return temp
        else:
            return 'ab' * A


if __name__ == '__main__':
    solution = Solution()
    A = 1
    B = 4
    print(solution.strWithout3a3b(A, B))