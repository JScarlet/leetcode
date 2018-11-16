class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1_dict = {}
        nums2_dict = {}
        for i in range(0, len(nums1)):
            if nums1[i] not in nums1_dict:
                nums1_dict[nums1[i]] = 1
            else:
                nums1_dict[nums1[i]] += 1

        for i in range(0, len(nums2)):
            if nums2[i] not in nums2_dict:
                nums2_dict[nums2[i]] = 1
            else:
                nums2_dict[nums2[i]] += 1

        common_set = set(nums1_dict.keys()) & set(nums2_dict.keys())
        result = []
        for each in common_set:
            length = min(nums1_dict[each], nums2_dict[each])
            for i in range(0, length):
                result.append(each)
        return result


if __name__ == '__main__':
    solution = Solution()
    nums1 = [4,9,5]
    nums2 = [9,4,9,8,4]
    print(solution.intersect(nums1, nums2))
