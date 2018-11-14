class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        vowel_str_list = []
        for letter in s:
            if letter in vowels:
                vowel_str_list.append(letter)

        vowel_str_list = vowel_str_list[::-1]
        count = 0
        result = ''
        for i in range(0, len(s)):
            if s[i] in vowels:
                result += vowel_str_list[count]
                count += 1
            else:
                result += s[i]
        return result


if __name__ == '__main__':
    solution = Solution()
    s = "aA"
    print(solution.reverseVowels(s))
