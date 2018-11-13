class Solution:
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        duplicate = sum(nums) - sum(set(nums))
        lack = sum([i for i in range(1, len(nums) + 1)]) - sum(set(nums))
        return [duplicate, lack]


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 2, 4]
    print(solution.findErrorNums(nums))
