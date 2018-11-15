class Solution:
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        A_count = 0
        for letter in s:
            if letter == 'A':
                A_count += 1

        if 'LLL' in s or A_count > 1:
            return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "PPALLL"
    print(solution.checkRecord(s))
