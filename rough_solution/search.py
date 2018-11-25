class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        return -1


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solution.search(nums, target))
