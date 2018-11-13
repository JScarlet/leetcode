class Solution:
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0
        for i in range(0, len(points)):
            for j in range(0, len(points)):
                for k in range(0, len(points)):
                    temp = self.calculate_square(points[i], points[j], points[k])
                    if temp > max_area:
                        max_area = temp
        return max_area

    def calculate_square(self, point_1, point_2, point_3):
        return 0.5 * abs(point_1[0]*point_2[1] + point_2[0]*point_3[1] + point_3[0]*point_1[1] - point_1[0]*point_3[1] - point_2[0]*point_1[1] - point_3[0]*point_2[1])


if __name__ == '__main__':
    solution = Solution()
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    print(solution.largestTriangleArea(points))
