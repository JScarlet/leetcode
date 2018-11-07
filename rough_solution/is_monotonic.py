class Solution:
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if len(A) <= 2:
            return True
        less_count = 0
        more_count = 0
        for i in range(0, len(A)-1):
            if A[i] < A[i+1]:
                less_count += 1
            elif A[i] > A[i+1]:
                more_count += 1
        if less_count == 0 or more_count == 0:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    A = [1,2,4,5]
    print(solution.isMonotonic(A))
