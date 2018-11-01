class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_map = {}
        for each in nums:
            if each not in nums_map:
                nums_map[each] = 1
            else:
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [1,2,3,4]
    print(solution.containsDuplicate(nums))
