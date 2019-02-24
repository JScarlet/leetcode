class Solution(object):
    def splitIntoFibonacci(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        if len(S) < 3:
            return result
        for i in range(1, len(S) - 1):
            first = S[0:i]
            for j in range(i + 1, len(S)):
                second = S[i: j]
                if len(first) > 1:
                    if first[0] == '0':
                        continue
                if len(second) > 1:
                    if second[0] == '0':
                        continue
                self.dfs(int(first), int(second), S[j:], [int(first), int(second)], result)
                if len(result) != 0:
                    return result[0]
        return result

    def dfs(self, first, second, num, head, result):
        if len(num) == 0:
            result.append(head)
            return
        sum_str = str(first + second)
        if sum_str == num[0: len(sum_str)] and (first + second) <= 2 ** 31 - 1:
            self.dfs(second, first + second, num[len(sum_str):], head + [first + second], result)


if __name__ == '__main__':
    solution = Solution()
    S = "539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"
    print(solution.splitIntoFibonacci(S))

    # [539834657, 21, 539834678, 539834699, 1079669377, 1619504076, 2699173453, 4318677529, 7017850982, 11336528511]
    # "539834657  21  539834678  539834699  1079669377  1619504076  2699173453  4318677529  7017850982  11336528511"