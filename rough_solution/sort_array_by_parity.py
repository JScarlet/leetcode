class Solution:
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        odd_list = []
        even_list = []
        for each in A:
            if each % 2 == 0:
                even_list.append(each)
            else:
                odd_list.append(each)
        # print(even_list, odd_list)
        even_list.extend(odd_list)
        return even_list


if __name__ == '__main__':
    solution = Solution()
    A = [3,1,2,4]
    print(solution.sortArrayByParity(A))
