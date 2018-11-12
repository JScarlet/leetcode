class Solution:
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return False
        result = 0
        length = int(abs(num)**0.5)
        for i in range(2, length+1):
            if num % i == 0:
                result += i + num//i
        result += 1
        if result == num:
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkPerfectNumber(1000000000))