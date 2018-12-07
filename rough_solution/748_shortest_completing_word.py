class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        letter_dict = {}
        for letter in licensePlate:
            if letter.isalpha():
                if letter.lower() not in letter_dict:
                    letter_dict[letter.lower()] = 1
                else:
                    letter_dict[letter.lower()] += 1

        result_dict = {}
        length = len(letter_dict.keys())
        for word in words:
            count = 0
            for key in letter_dict:
                if word.count(key) >= letter_dict[key]:
                    count += 1
            if count == length:
                if len(word) not in result_dict:
                    result_dict[len(word)] = [word]
                else:
                    result_dict[len(word)].append(word)
        sorted_result = sorted(result_dict.items(), key=lambda x:x[0])
        return sorted_result[0][1][0]


if __name__ == '__main__':
    solution = Solution()
    licensePlate = "1s3 PSt"
    words = ["step", "steps", "stripe", "stepple"]
    print(solution.shortestCompletingWord(licensePlate, words))