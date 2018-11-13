class Solution:
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        result = []
        for i in range(left, right+1):
            str_i = str(i)
            count = 0
            length = 0
            if '0' in str_i:
                continue
            for letter in str_i:
                if letter != '0':
                    length += 1
                    if i % int(letter) == 0:
                        count += 1
            if count == length:
                result.append(i)
        return result


if __name__ == '__main__':
    solution = Solution()
    left = 1
    right = 22
    print(solution.selfDividingNumbers(left, right))