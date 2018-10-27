class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x == 1:
            return 1
        half = x // 2
        old = half
        while True:
            temp = half * half
            if temp > x:
                old = half
                half = half // 2
            else:
                if (half + 1) * (half + 1) > x:
                    return half
                else:
                    half = (half + old) // 2

    def mySqrt2(self, x):
        min = 0
        max = x
        if x == 1:
            return 1
        while True:
            half = (min + max) // 2
            if half ** 2 > x:
                max = half
            else:
                if (half + 1) ** 2 > x:
                    return half
                else:
                    min = half


if __name__ == '__main__':
    solution = Solution()
    print(solution.mySqrt2(1))

# 解题思路：
# 运用二分法，或者用python的**直接 n**0.5再取整
