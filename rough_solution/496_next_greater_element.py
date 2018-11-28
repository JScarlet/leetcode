class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # result = []
        # for num in nums1:
        #     index = nums2.index(num)
        #     next_index = -1
        #     for i in range(index + 1, len(nums2)):
        #         if nums2[i] > num:
        #             next_index = nums2[i]
        #             break
        #     result.append(next_index)
        # return result

        dic, stack = {}, []
        for number in nums2:
            print(stack)
            print(dic)
            while stack and stack[-1] < number:
                dic[stack.pop()] = number
            stack.append(number)
        return [dic.get(i, -1) for i in nums1]


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(solution.nextGreaterElement(nums1, nums2))
