class Solution:
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        nums.sort()
        for i in range(0, len(nums)):
            count += (nums[i] - nums[0])
        return count


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3]
    print(solution.minMoves(nums))

# 解题思路：
# 逆向思考，每次移动让剩余的n-1个数加1，相当于每次移动让选定的那个数减1，
# 所以最少移动次数其实就是所有元素减去最小元素的和
