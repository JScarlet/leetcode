class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        length = len(nums)
        nums = set(nums)

        result = []
        for i in range(0, length):
            if i+1 not in nums:
                result.append(i+1)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [4,3,2,7,8,2,3,1]
    print(solution.findDisappearedNumbers(nums))
