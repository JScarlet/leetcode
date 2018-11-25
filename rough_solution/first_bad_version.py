# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return self.isBadVersion(n)
        left = 1
        right = n
        middle = (left + right) // 2
        while True:
            if not self.isBadVersion(middle):
                left = middle + 1
            else:
                if not self.isBadVersion(middle-1) or middle == 1:
                    return middle
                else:
                    right = middle - 1
            middle = (left+right) // 2

    def isBadVersion(self, version):
        total = [False, False, False, True, True]
        # total = [False, True]
        return total[version - 1]


if __name__ == '__main__':
    solution = Solution()
    print(solution.firstBadVersion(5))
