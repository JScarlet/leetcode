class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        letter_count = 0
        for letter in S:
            if letter.isalpha():
                letter_count += 1

        convert_times = 2 ** letter_count
        result = []
        for i in range(0, convert_times):
            temp = str(bin(i))[2:]
            while len(temp) < letter_count:
                temp = '0' + temp
            count = 0
            single = ''
            for letter in S:
                if letter.isalpha():
                    single += letter.lower() if temp[count] == '0' else letter.upper()
                    count += 1
                else:
                    single += letter
            result.append(single)
        return result


if __name__ == '__main__':
    solution = Solution()
    S = "2z3"
    print(solution.letterCasePermutation(S))
