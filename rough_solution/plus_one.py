class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        flag = True
        digits = digits[::-1]
        for i in range(0, len(digits)):
            if flag:
                digits[i] += 1
                if digits[i] >= 10:
                    digits[i] -= 10
                    if i == len(digits) - 1:
                        digits.append(1)
                else:
                    flag = False
        return digits[::-1]


if __name__ == '__main__':
    solution = Solution()
    digits = [9]
    print(solution.plusOne(digits))
