class Solution:
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        sum = 0
        i = 0
        while sum < target:
            i += 1
            sum += i
        if (sum - target) % 2 == 0:
            return i
        else:
            if i % 2 == 0:
                return i + 1
            else:
                return i + 2


if __name__ == '__main__':
    solution = Solution()
    target = 4
    print(solution.reachNumber(target))
