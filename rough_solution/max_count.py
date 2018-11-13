class Solution:
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        if len(ops) == 0:
            return m*n
        min_m = ops[0][0]
        min_n = ops[0][1]
        for each in ops:
            if each[0] < min_m:
                min_m = each[0]
            if each[1] < min_n:
                min_n = each[1]
        return min_m * min_n


if __name__ == '__main__':
    solution = Solution()
    m = 6
    n = 17
    operations = [[1,4],[5,5],[4,9],[1,10],[6,2],[1,11],[4,6],[2,2],[3,15],[6,14],[1,17],[2,8],[4,7],[2,7]]
    print(solution.maxCount(m, n, operations))
