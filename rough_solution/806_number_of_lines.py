class Solution:
    def numberOfLines(self, widths, S):
        """
        :type widths: List[int]
        :type S: str
        :rtype: List[int]
        """
        line = 1
        length = 0
        for letter in S:
            letter_size = widths[ord(letter) - ord('a')]
            if length + letter_size > 100:
                line += 1
                length = letter_size
            else:
                length += letter_size
        return [line, length]


if __name__ == '__main__':
    solution = Solution()
    widths = [4, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
    S = "bbbcccdddaaa"
    print(solution.numberOfLines(widths, S))
