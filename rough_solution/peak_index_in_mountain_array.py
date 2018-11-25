class Solution(object):
    def peakIndexInMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        left = 0
        right = len(A) - 1
        while left <= right:
            middle = (left + right) // 2
            print(middle)
            if A[middle - 1] < A[middle] > A[middle + 1]:
                return middle
            elif A[middle - 1] < A[middle] < A[middle + 1]:
                left = middle + 1
            else:
                right = middle - 1


if __name__ == '__main__':
    solution = Solution()
    A = [18,29,38,59,98,100,99,98,90]
    print(solution.peakIndexInMountainArray(A))
