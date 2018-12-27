class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num2letter = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'], '6': ['m', 'n', 'o'], '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y', 'z']}
        result = []
        if len(digits) > 0:
            for each in num2letter[digits[0]]:
                result.append(each)
        # print(result)
        for i in range(1, len(digits)):
            temp = []
            letters = num2letter[digits[i]]
            # print(letters)
            while len(result) > 0:
                comb = result.pop()
                # print(comb)
                # print(letters)
                for each in letters:
                    # print(comb+each)
                    temp.append(comb + each)
            # print(temp)
            result.extend(temp)
        return result


if __name__ == '__main__':
    solution = Solution()
    digits = '22'
    print(solution.letterCombinations(digits))
    # temp = {1: ['a', 'b'], 2: ['b', 'c'], 3: ['c', 'd']}
    # test = temp[1]
    # test.pop()
    # print(temp)
    # test.append('c')
    # print(temp)
    # temp = {1: 'ab', 2: 'bc', 3: 'cd'}
    # test = temp[1]
    # test += 'c'
    # print(temp)