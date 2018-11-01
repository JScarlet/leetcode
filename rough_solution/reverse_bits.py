class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        result = str(bin(n))[2:][::-1]
        remain = 34 - len(bin(n))
        for i in range(0, remain):
            result += '0'
        print(result)
        return int(result, 2)


if __name__ == '__main__':
    solution = Solution()
    print(solution.reverseBits(43261596))
