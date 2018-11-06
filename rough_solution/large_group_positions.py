class Solution:
    def largeGroupPositions(self, S):
        """
        :type S: str
        :rtype: List[List[int]]
        """
        start_index = 0
        count = 0
        result = []
        for i in range(0, len(S)):
            if S[start_index] == S[i]:
                count += 1
            else:
                if count >= 3:
                    temp = [start_index, start_index + count - 1]
                    result.append(temp)
                start_index = i
                count = 1
        if count >= 3:
            result.append([start_index, start_index + count - 1])
        return result


if __name__ == '__main__':
    solution = Solution()
    S = "aaa"
    print(solution.largeGroupPositions(S))


# 解题思路：
# 从前到后遍历，记录起始字母的index以及连续出现的长度
