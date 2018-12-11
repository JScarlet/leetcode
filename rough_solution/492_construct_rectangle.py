class Solution:
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        middle = int(area ** 0.5)
        if middle ** 2 == area:
            return [middle, middle]
        else:
            for i in range(middle, 0, -1):
                if area % i == 0:
                    return [area // i, i]


if __name__ == '__main__':
    solution = Solution()
    print(solution.constructRectangle(9999991))
