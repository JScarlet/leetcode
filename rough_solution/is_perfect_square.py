class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        min = 1
        max = num
        i = (min + max) // 2
        while min < i < max:
            temp = i ** 2
            if temp == num:
                return True
            elif temp > num:
                max = i
            elif temp < num:
                min = i
            i = (min + max) // 2
            print(i, min, max)
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isPerfectSquare(2))