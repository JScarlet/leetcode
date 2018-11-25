# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):

def guess(num):
    if num < pick:
        return -1
    elif num == pick:
        return 0
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        left = 1
        right = n
        middle = (left + right) // 2
        while True:
            if guess(middle) == 0:
                return middle
            elif guess(middle) == -1:
                left = middle + 1
            else:
                right = middle - 1
            middle = (left + right) // 2


if __name__ == '__main__':
    solution = Solution()
    n = 10
    pick = 6
    print(solution.guessNumber(n))


