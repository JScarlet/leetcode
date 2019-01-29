class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(nums) - 1
        middle = -1
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                break
            elif nums[middle] < target:
                left = middle + 1
            else:
                right = middle - 1
        if middle == -1 or nums[middle] != target:
            return [-1, -1]
        else:
            i = j = middle
            # print(i, j)
            while 0 <= i < len(nums) and nums[i] == target:
                i -= 1

            while 0 <= j < len(nums) and nums[j] == target:
                j += 1
            return [i + 1, j - 1]


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 7
    print(solution.searchRange(nums, target))
