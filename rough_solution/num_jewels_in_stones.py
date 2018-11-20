class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        result = 0
        for letter in S:
            if letter in J:
                result += 1
        return result


if __name__ == '__main__':
    solution = Solution()
    J = "aA"
    S = "aAAbbbb"
    print(solution.numJewelsInStones(J, S))
