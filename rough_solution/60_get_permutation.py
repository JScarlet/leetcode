class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        per_list = [i for i in range(1, n+1)]
        result = ''
        length = n
        for i in range(0, length):
            factorial = 1
            for j in range(1, n):
                factorial *= j
            index = (k - 1) // factorial
            result += str(per_list.pop(index))
            k -= factorial * index
            n -= 1
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.getPermutation(3, 3))
