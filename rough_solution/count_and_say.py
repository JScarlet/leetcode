class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        else:
            result = ''
            target = self.countAndSay(n - 1)
            key = target[0]
            count = 0
            for letter in target:
                if letter == key:
                    count += 1
                else:
                    result += (str(count) + key)
                    key = letter
                    count = 1
            result += (str(count) + key)
            return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.countAndSay(6))


# 解题思路：
# 初始为1，之后用递归依次计算后面的值