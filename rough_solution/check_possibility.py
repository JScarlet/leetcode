class Solution:
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        left = 0
        for i in range(0, len(nums) - 1):
            if nums[i] > nums[i + 1]:
                left = i

        right = 0
        for i in reversed(range(0, len(nums) - 1)):
            if nums[i] > nums[i + 1]:
                right = i

        print(left, right)
        if left != right:
            return False

        if left == 0 or right == len(nums) - 1:
            return True

        if 0 <= left - 1 and right + 2 <= len(nums) - 1:
            print(nums[left - 1] > nums[right + 1], nums[left] > nums[right + 2])
            if nums[left - 1] > nums[right + 1] and nums[left] > nums[right + 2]:
                return False
            return True

        # if 0 <= left and right + 2 < len(nums) - 1:
        #     if nums[left] > nums[right + 2]:
        #         return False
        #     return True

        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [3,4,2,3] #[1,2,4,5,3] [2,3,3,2,4]
    print(solution.checkPossibility(nums))
