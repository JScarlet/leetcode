class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        result = 0
        minus = 100000
        nums.sort()
        for i in range(0, len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                print(sum)
                abs_minus = abs(sum - target)
                if abs_minus < minus:
                    minus = abs_minus
                    result = sum
                if sum < target:
                    left += 1
                elif sum > target:
                    right -= 1
                else:
                    return sum
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1,2,1,-4]
    target = 1
    print(solution.threeSumClosest(nums, target))


# 双指针问题一般都是首尾两个指针，然后依据某种规则想中间靠拢，最终当left = right的时候结束循环，得到最终结果
