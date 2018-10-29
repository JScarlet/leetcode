class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = {}
        result = 0
        for i in range(len(nums)):
            if nums[i] not in temp:
                temp[nums[i]] = 1
                result += nums[i]
            else:
                result -= nums[i]
        return result

    def singleNumber2(self, nums):
        return sum(set(nums)) * 2 - sum(nums)

    def singleNumber3(self, nums):
        result = 0
        for each in nums:
            result ^= each
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,1,2,4]
    print(solution.singleNumber3(nums))


# 解题思路：
# 1. dict的查询效率远高于list
# 2. 转成set后的和*2 再减去nums的和正好等于未重复的数字
# 3. 异或运算，两个相等的数字异或运算后等于0，最后剩下的即为未重复的数字
