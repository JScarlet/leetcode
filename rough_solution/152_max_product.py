class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        A = nums
        B = A[::-1]
        for i in range(1, len(A)):
            A[i] *= A[i-1] or 1
            B[i] *= B[i-1] or 1
        return max(max(A), max(B))


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 3, -2, 4]
    print(solution.maxProduct(nums))