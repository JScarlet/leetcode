class Solution:
    def isOneBitCharacter(self, bits):
        """
        :type bits: List[int]
        :rtype: bool
        """
        i = 0
        flag = 0
        while i < len(bits) - 1:
            if flag == 0:
                if bits[i] == 1:
                    flag = 1
                i += 1
            else:
                i += 1
                flag = 0

        if flag == 0:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    bits = [1, 0, 0]
    print(solution.isOneBitCharacter(bits))

# 解题思路：
# 1. 设置flag，flag=0表示该位之前的所有数字能用这两种表示方法表示，flag=1表示该位之前的所有数字不能用这两种方法表示，需要加上该位
# 2. 从第一位开始，如果是0就+1，否则就+2，如果恰好能到最后一位，表示前面都能完全表示，否则的话表示前面的不能完全表示
