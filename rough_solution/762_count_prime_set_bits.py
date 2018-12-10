class Solution:
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        result = 0
        for i in range(L, R+1):
            num = bin(i)[2:]
            count = num.count('1')
            if self.isPrime(count):
                result += 1
        return result

    def isPrime(self, num):
        from math import sqrt
        if num == 1:
            return False
        if num == 2 or num == 3:  # 两个较小的数进行处理
            return True
        if num % 6 != 1 and num % 6 != 5:  # 不在6的倍数的两侧的一定不是质数
            return False
        tmp = int(sqrt(num))
        for i in range(5, tmp + 1):  # 在6的倍数两侧的也可能不是质数
            if num % i == 0 or num % (i + 2) == 0:
                return False
        return True  # 剩下的全是质数


if __name__ == '__main__':
    solution = Solution()
    L = 10
    R = 15
    print(solution.countPrimeSetBits(L, R))
