class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_map = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 1
            else:
                nums_map[nums[i]] += 1
        result = sorted(nums_map.items(), key=lambda x:x[0], reverse=True)
        if len(result) < 3:
            return result[0][0]
        return result[2][0]


if __name__ == '__main__':
    solution = Solution()
    nums = [2, 2, 3, 1]
    print(solution.thirdMax(nums))


# 解题思路：
# 把nums中的数放在dict中，然后对字典key进行排序
