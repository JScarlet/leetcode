class Solution:
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        set1 = set(list1)
        set2 = set(list2)
        common = set1 & set2
        result_dict = {}
        for each in common:
            temp = list1.index(each) + list2.index(each)
            if temp not in result_dict:
                result_dict[temp] = [each]
            else:
                result_dict[temp].append(each)
        result = sorted(result_dict.items(), key=lambda x:x[0])
        return result[0][1]


if __name__ == '__main__':
    solution = Solution()
    list1 = ["Shogun", "Tapioca Express", "Burger King", "KFC"]
    list2 = ["KFC", "Shogun", "Burger King"]
    print(solution.findRestaurant(list1, list2))
