class Solution:
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = sorted(nums, reverse=True)
        max_num = temp[0]
        max_index = -1
        for i in range(0, len(nums)):
            if nums[i] != max_num:
                if max_num < nums[i] * 2:
                    return -1
            else:
                max_index = i
        return max_index


if __name__ == '__main__':
    solution = Solution()
    nums = [4]
    print(solution.dominantIndex(nums))