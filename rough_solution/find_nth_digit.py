class Solution:
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        for i in range(0, 2**30):
            if n - (i+1) * 9 * 10 ** i <= 0:
                print(n, i)
                mod = n % (i+1)
                div = n // (i+1)
                if mod == 0:
                    target = 10 ** i - 1 + div
                else:
                    target = 10 ** i + div
                return int(str(target)[mod-1])
            else:
                n = n - (i+1) * 9 * 10 ** i


if __name__ == '__main__':
    solution = Solution()
    print(solution.findNthDigit(11))


# 解题思路：
# i位数的话一共会占i*9*10**(i-1)个数，n减去i位数的个数，如果小于0就说明在这个i位数内；
# 得到的数字除以i，如果余数是0的话，10**(i-1) - 1再加上商就是正常的数字，最后一位即是结果，
# 如果余数不是0的话，10**(i-1)再加上商就是正常的数字，余数-1位即是结果
