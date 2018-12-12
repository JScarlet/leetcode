class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        temp = []
        for i in range(0, len(nums)):
            for i in range(0, len(nums)):
                temp.append(nums[i])
            num = temp.pop(i)
            print(num)
            sum_dict = {}
            for j in range(0, len(temp)):
                another = -num - temp[j]
                if another in sum_dict:
                    sum_dict[another].append(temp[j])
                    sorted_single = sorted(sum_dict[another])
                    if sorted_single not in result:
                        result.append(sorted_single)
                        break
                sum_dict[another] = [another, num]
        return result


if __name__ == '__main__':
    solution = Solution()
    nums = [-1, 0, 1, 2, -1, -4]
    print(solution.threeSum(nums))