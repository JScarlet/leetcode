class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        temp = {}
        n_copy = n
        while n_copy not in temp:
            str_n = str(n_copy)
            n_copy = 0
            for num in str_n:
                n_copy += int(num) ** 2
            if n_copy == 1:
                return True
            temp[n] = 1
            n = n_copy
        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.isHappy(201))
