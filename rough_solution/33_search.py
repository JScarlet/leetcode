class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        num_dict = {}
        for i in range(0, len(nums)):
            num_dict[nums[i]] = i

        nums = sorted(nums)
        left = 0
        right = len(nums) - 1
        while left <= right:
            # print(left, right)
            middle = (left + right) // 2
            if nums[middle] == target:
                return num_dict[target]
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    target = 3
    print(solution.search(nums, target))