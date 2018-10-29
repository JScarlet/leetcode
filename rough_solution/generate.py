class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []

        result = []
        temp = []
        for i in range(0, numRows):
            if i == 0:
                result.append([1])
            elif i == 1:
                temp = [1, 1]
                result.append(temp)
            else:
                shorter = []
                for j in range(0, len(temp) - 1):
                    shorter.append(temp[j] + temp[j + 1])
                shorter.insert(0, 1)
                shorter.append(1)
                temp = shorter
                result.append(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.generate(5))


# 解题思路：
# 杨辉三角形的生成方式，每一个数字等于上面两数之和