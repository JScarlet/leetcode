class Solution:
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        nums_map = {}
        for i in range(0, len(nums)):
            if nums[i] not in nums_map:
                nums_map[nums[i]] = 1
            else:
                nums_map[nums[i]] += 1

        result = 0

        if k == 0:
            for key in nums_map:
                if nums_map[key] >= 2:
                    result += 1
        else:
            for key in nums_map:
                other = key + k
                if other in nums_map:
                    result += 1

        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 3, 1, 5, 4]
    k = 2
    print(solution.findPairs(nums, k))


# 解题思路：
# 如果k=0的话，就看某一个数字是否出现次数大于等于两次；如果k>0的话，当成集合来做；如果k<0的话，直接返回0
