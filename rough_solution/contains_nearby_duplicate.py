class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k >= len(nums):
            k = len(nums) - 1

        if len(set(nums)) == len(nums):
            return False

        for i in range(0, len(nums) - k):
            temp = nums[i: i+k+1]
            if len(set(temp)) < len(temp):
                return True
        return False


if __name__ == '__main__':
    solution = Solution()
    nums = [99, 99]
    k = 2
    print(solution.containsNearbyDuplicate(nums, k))
