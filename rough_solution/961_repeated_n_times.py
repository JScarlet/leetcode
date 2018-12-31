class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        A.sort()
        print(A)
        if A[len(A)//2] == A[len(A)//2 + 1]:
            return A[len(A)//2]
        else:
            return A[len(A)//2 - 1]


if __name__ == '__main__':
    solution = Solution()
    A = [9,5,3,3]
    print(solution.repeatedNTimes(A))