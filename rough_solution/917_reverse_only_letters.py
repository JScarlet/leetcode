class Solution:
    def reverseOnlyLetters(self, S):
        """
        :type S: str
        :rtype: str
        """
        result = ''
        temp = []
        for i in range(0, len(S)):
            if S[i].isalpha():
                temp.append(S[i])

        for i in range(0, len(S)):
            if S[i].isalpha():
                result += temp.pop()
            else:
                result += S[i]
        return result


if __name__ == '__main__':
    solution = Solution()
    S = "a-bC-dEf-ghIj"
    print(solution.reverseOnlyLetters(S))
