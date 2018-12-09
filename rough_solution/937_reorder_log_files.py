class Solution:
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        result = []
        num_result = []
        alphabet_result = []
        for each in logs:
            identifiers_list = each.split()
            if identifiers_list[1].isnumeric():
                num_result.append(each)
            else:
                alphabet_result.append(each)
        alphabet_result = sorted(alphabet_result, key=lambda x:x[x.find(' ')+1:])
        result.extend(alphabet_result)
        result.extend(num_result)
        return result


if __name__ == '__main__':
    solution = Solution()
    logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
    print(solution.reorderLogFiles(logs))