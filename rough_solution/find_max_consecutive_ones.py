class Solution:
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max = 0
        temp = 0
        for i in range(0, len(nums)):
            if nums[i] == 0:
                if max < temp:
                    max = temp
                temp = 0
            else:
                temp += 1
            if max < temp:
                max = temp
        return max


if __name__ == '__main__':
    solution = Solution()
    nums = [1,1,0,1,1,1]
    print(solution.findMaxConsecutiveOnes(nums))
