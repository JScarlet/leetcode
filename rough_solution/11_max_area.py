class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left, right, max_area = 0, len(height) - 1, 0
        while left < right:
            temp = (right - left) * min(height[left], height[right])
            if temp > max_area:
                max_area = temp
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    solution = Solution()
    height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(solution.maxArea(height))
