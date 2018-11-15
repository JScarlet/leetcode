class Solution:
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        if (set(A) != set(B)):
            return -1
        temp = A
        count = 1
        if len(A) <= len(B):
            while 2 * len(B) >= len(temp):
                if B in temp:
                    return count
                else:
                    temp += A
                    count += 1
            return -1
        else:
            if B in A:
                return 1
            elif B in A * 2:
                return 2
            else:
                return -1


if __name__ == '__main__':
    solution = Solution()
    A = "abaabaa"
    B = "abaababaab"
    print(solution.repeatedStringMatch(A, B))
