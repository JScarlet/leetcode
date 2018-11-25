class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        letters_set = set(letters)
        letters = sorted(letters_set)

        if ord(target) >= ord(letters[-1]):
            return letters[0]

        if ord(target) < ord(letters[0]):
            return letters[0]

        left = 0
        right = len(letters) - 1
        while left <= right:
            middle = (left + right) // 2
            print(middle)
            if letters[middle] == target:
                return letters[middle + 1]
            elif ord(letters[middle]) < ord(target):
                left = middle + 1
            else:
                if ord(letters[middle - 1]) <= ord(target):
                    return letters[middle]
                else:
                    right = middle - 1


if __name__ == '__main__':
    solution = Solution()
    letters = ["e","e","e","e","e","e","n","n","n","n"]
    target = "e"
    print(solution.nextGreatestLetter(letters, target))
