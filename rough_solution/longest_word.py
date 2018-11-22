class Solution:
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        words = sorted(words, key=lambda x:len(x))
        # print(words)
        word_dict = {}
        for word in words:
            if len(word) == 1:
                temp = {1: word}
                word_dict[word] = temp
            else:
                if word[0] in word_dict:
                    temp = word_dict[word[0]]
                    if len(word) - 1 in temp:
                        less = temp[len(word) - 1]
                        if word[:-1] in less:
                            if len(word) in temp:
                                temp[len(word)].append(word)
                            else:
                                temp[len(word)] = [word]
        # print(word_dict)

        max_key_count_dict = {}
        for key in word_dict:
            if max(word_dict[key].keys()) not in max_key_count_dict:
                max_key_count_dict[max(word_dict[key].keys())] = [key]
            else:
                max_key_count_dict[max(word_dict[key].keys())].append(key)

        # print(sorted(max_key_count_dict.items(), key=lambda x:x[0]))
        target_key = sorted(sorted(max_key_count_dict.items(), key=lambda x:x[0])[-1][1])[0]
        result_list = sorted(word_dict[target_key][max(word_dict[target_key].keys())])
        return result_list[0]


if __name__ == '__main__':
    solution = Solution()
    words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
    print(solution.longestWord(words))

