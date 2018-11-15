class Solution:
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        result = ''
        for letter in str:
            result += letter.lower()
        return result


if __name__ == '__main__':
    solution = Solution()
    str = "LOVELY"
    print(solution.toLowerCase(str))
