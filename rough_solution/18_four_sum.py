class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        two_nums = {}
        for i in range(0, len(nums)-1):
            for j in range(i+1, len(nums)):
                temp = nums[i] + nums[j]
                two_nums.setdefault(temp, []).append([i, j])
        # print(two_nums)
        middle_result = []
        for key in two_nums:
            other = target - key
            if other == key:
                if len(two_nums[key]) > 1:
                    for i in range(0, len(two_nums[key])-1):
                        for j in range(i+1, len(two_nums[key])):
                            temp = two_nums[key][i] + two_nums[key][j]
                            middle_result.append(temp)
            else:
                if other in two_nums:
                    prefix_middle = []
                    if len(two_nums[key]) > 1:
                        for i in range(0, len(two_nums[key])):
                            prefix_middle.append(two_nums[key][i])
                    else:
                        prefix_middle.append(two_nums[key][0])
                    # print(prefix_middle)

                    for i in range(0, len(prefix_middle)):
                        if len(two_nums[other]) > 1:
                            for j in range(0, len(two_nums[other])):
                                temp = prefix_middle[i] + two_nums[other][j]
                                middle_result.append(temp)
                        else:
                            temp = prefix_middle[i] + two_nums[other][0]
                            middle_result.append(temp)
        # print(middle_result)
        result = set()
        for each in middle_result:
            if len(set(each)) == 4:
                temp = []
                for index in each:
                    temp.append(nums[index])
                result.add(tuple(sorted(temp)))

        final = []
        for each in result:
            final.append(list(each))
        return final


if __name__ == '__main__':
    solution = Solution()
    nums = [-3,-1,0,2,4,5]
    target = 0
    print(solution.fourSum(nums, target))
