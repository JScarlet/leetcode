class Solution:
    def sortArrayByParityII(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd = []
        even = []
        for each in A:
            if each % 2 == 0:
                even.append(each)
            else:
                odd.append(each)

        if len(even) != len(odd):
            return []
        else:
            result = []
            for i in range(0, len(odd)):
                result.append(even[i])
                result.append(odd[i])
            return result


if __name__ == '__main__':
    solution = Solution()
    A = [4,2,5,7]
    print(solution.sortArrayByParityII(A))
