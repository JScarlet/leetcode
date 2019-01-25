class Solution:
    def kClosest(self, points, K):
        """
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        distance_dict = {}
        for point in points:
            distance = point[0] ** 2 + point[1] ** 2
            if distance in distance_dict:
                distance_dict[distance].append(point)
            else:
                distance_dict[distance] = [point]

        sorted_distance = sorted(distance_dict.items(), key=lambda x:x[0])
        print(sorted_distance)
        count = 0
        result = []
        for i in range(0, len(sorted_distance)):
            point_list = sorted_distance[i][1]
            for point in point_list:
                result.append(point)
                count += 1
                if count == K:
                    return result
        return result

        # 最优解
        # return sorted(points, key=lambda x: x[0] ** 2 + x[1] ** 2)[:k]


if __name__ == '__main__':
    solution = Solution()
    points = [[1,3],[-2,2]]
    K = 3
    print(solution.kClosest(points, K))
