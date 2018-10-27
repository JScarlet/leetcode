class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        length = n//2 +1
        for i in range(0, length):
            j = n - 2 * i

            temp_1 = 1
            for m in range(1, i+1):
                temp_1 *= m

            temp_2 = 1
            for x in range(1, j+1):
                temp_2 *= x

            temp_3 = 1
            for l in range(1, (i + j + 1)):
                temp_3 *= l
            print(temp_3 // (temp_2 * temp_1))
            result += (temp_3 // (temp_2 * temp_1))

        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.climbStairs(1))

# 解题思路：
# 设走两级的有i个，走一级的就有j=n-2*i个，运用排列组合a(i+j)/(a(i)*a(j))