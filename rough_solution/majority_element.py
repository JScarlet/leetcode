class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = {}
        for each in nums:
            if each not in result:
                result[each] = 1
            else:
                result[each] += 1
        return sorted(result.items(), key=lambda x:x[1], reverse=True)[0][0]


if __name__ == '__main__':
    solution = Solution()
    nums = [2,2,1,1,1,2,2]
    print(solution.majorityElement(nums))


# 解题思路：
# 1. 把nums中的元素存到dict中，然后排序找出频数最高的
# 2. 因为题目中说众数都是多余一半的，所以另外一种方法是排好序后找中间值即可
