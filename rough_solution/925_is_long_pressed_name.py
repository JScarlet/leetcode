class Solution:
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i, j = 0, 0
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                i += 1
                j += 1
            else:
                if j > 0 and typed[j] == typed[j - 1]:
                    j += 1
                else:
                    return False
        if i == len(name) and j == len(typed):
            return True
        elif i == len(name) and j < len(typed):
            for m in range(j, len(typed)):
                if typed[m] != name[-1]:
                    return False
            return True
        return False


if __name__ == '__main__':
    solution = Solution()
    name = "vtkgn"
    typed = "vttkgnn"
    print(solution.isLongPressedName(name, typed))
