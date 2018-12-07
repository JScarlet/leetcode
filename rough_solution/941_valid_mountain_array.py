class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        if A is None:
            return False
        less_count = 0
        more_count = 0
        change_count1 = 0
        change_count2 = 0
        if len(A) <= 2:
            return False
        for i in range(1, len(A) - 1):
            if A[i-1] < A[i]:
                less_count += 1
            if A[i-1] > A[i]:
                more_count += 1
            if A[i-1] < A[i] and A[i] > A[i+1]:
                change_count1 += 1
            if A[i-1] > A[i] and A[i] < A[i+1]:
                change_count2 += 1
        if A[len(A) - 2] < A[len(A) - 1]:
            less_count += 1
        if A[len(A) - 2] > A[len(A) - 1]:
            more_count += 1
        if less_count + more_count == len(A) - 1 and change_count1 == 1 and change_count2 == 0:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    A = [0,3,2,3]
    print(solution.validMountainArray(A))