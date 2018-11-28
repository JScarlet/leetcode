class Solution:
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        points = []
        for each in ops:
            if each == '+':
                points.append(sum(points[-2:]))
            elif each == 'D':
                points.append(points[-1] * 2)
            elif each == 'C':
                points.pop()
            else:
                points.append(int(each))
        return sum(points)


if __name__ == '__main__':
    solution = Solution()
    ops = ["5","-2","4","C","D","9","+","+"]
    print(solution.calPoints(ops))
