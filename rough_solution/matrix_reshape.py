class Solution:
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        total_length = len(nums) * len(nums[0])
        if r * c != total_length:
            return nums

        total = []
        for i in range(0, len(nums)):
            total.extend(nums[i])

        result = []
        for i in range(0, r):
            temp = []
            for j in range(0, c):
                temp.append(total[i*c+j])
            result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [[1,2],[3,4]]
    r = 2
    c = 4
    print(solution.matrixReshape(nums, r, c))
