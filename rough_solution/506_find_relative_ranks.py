class Solution:
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        nums_dict = {}
        sorted_nums = sorted(nums, reverse=True)
        for i in range(0, len(sorted_nums)):
            nums_dict[sorted_nums[i]] = i+1
        result = []
        for i in range(0, len(nums)):
            score = nums_dict[nums[i]]
            if score == 1:
                result.append('Gold Medal')
            elif score == 2:
                result.append('Silver Medal')
            elif score == 3:
                result.append('Bronze Medal')
            else:
                result.append(str(score))
        return result


if __name__ == "__main__":
    solution = Solution()
    nums = [5, 4, 3, 2, 1]
    print(solution.findRelativeRanks(nums))