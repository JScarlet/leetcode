class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n > 0:
            n //= 5
            res += n
        return res


if __name__ == '__main__':
    solution = Solution()
    print(solution.trailingZeroes(1808548329))

# 解题思路：
# 因为只要出现5就会有一个0，本质相当于求一共能拆分出多少个5，一直辗转相除求出前n个数里一共有多少个5的倍数即可
