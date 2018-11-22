class Solution:
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        nums_dict = {}
        result = 0
        for i in range(0, len(nums)):
            if nums[i] not in nums_dict:
                nums_dict[nums[i]] = 1
            else:
                nums_dict[nums[i]] += 1
        nums_items = sorted(nums_dict.items(), key=lambda x:x[0])
        print(nums_items)
        for i in range(0, len(nums_items) - 1):
            if abs(nums_items[i][0] - nums_items[i+1][0]) <= 1:
                if result < (nums_items[i][1] + nums_items[i+1][1]):
                    result = nums_items[i][1] + nums_items[i+1][1]
        # if result < nums_items[-1][1]:
        #     result = nums_items[-1][1]
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,1,1]
    print(solution.findLHS(nums))
