class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if len(num) < 3:
            return False
        for i in range(1, len(num) - 1):
            first = num[0:i]
            for j in range(i + 1, len(num)):
                second = num[i: j]
                if len(first) > 1:
                    if first[0] == '0':
                        continue
                if len(second) > 1:
                    if second[0] == '0':
                        continue
                if self.dfs(int(first), int(second), num[j:], True):
                    return True
        return False

    def dfs(self, first, second, num, flag):
        if len(num) == 0:
            return flag
        sum_str = str(first + second)
        if sum_str == num[0: len(sum_str)]:
            flag =  self.dfs(second, first + second, num[len(sum_str):], flag) & flag
            return flag
        else:
            return False


if __name__ == '__main__':
    solution = Solution()
    num = "101"
    print(solution.isAdditiveNumber(num))
