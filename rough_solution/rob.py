class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return nums[0]
        result = [0, nums[0], nums[1]]
        for i in range(3, len(nums)+1):
            max_front = 0
            for j in range(1, i - 1):
                temp = result[j]
                if temp > max_front:
                    max_front = temp
            result.append(max_front + nums[i-1])
        # print(result)
        return sorted(result)[-1]


if __name__ == '__main__':
    solution = Solution()
    nums = [2,7,9,3,1]
    print(solution.rob(nums))
