class Solution:
    def largestTimeFromDigits(self, A):
        """
        :type A: List[int]
        :rtype: str
        """
        result = []
        hour_dict = {}
        for i in range(0, len(A)-1):
            for j in range(i+1, len(A)):
                if 0 <= A[i] * 10 + A[j] <= 23:
                    key = str(i) + '-' + str(j)
                    hour_dict[key] = A[i] * 10 + A[j]
                if 0 <= A[j] * 10 + A[i] <= 23:
                    key = str(j) + '-' + str(i)
                    hour_dict[key] = A[j] * 10 + A[i]
        if len(hour_dict) == 0:
            return ''
        for key in hour_dict:
            index_list = key.split('-')
            temp = []
            for i in range(0, len(A)):
                if str(i) not in index_list:
                    temp.append(i)
            if hour_dict[key] < 10:
                hour_str = '0' + str(hour_dict[key])
            else:
                hour_str = str(hour_dict[key])

            minute1 = A[temp[0]] * 10 + A[temp[1]]
            minute2 = A[temp[1]] * 10 + A[temp[0]]

            if minute1 <= 59 and minute2 <= 59:
                max_minute = max(minute1, minute2)
                if max_minute < 10:
                    hour_str += '0' + str(max_minute)
                else:
                    hour_str += str(max_minute)
                result.append(hour_str)
            elif minute1 <= 59 and minute2 > 59:
                if minute1 < 10:
                    hour_str += '0' + str(minute1)
                else:
                    hour_str += str(minute1)
                result.append(hour_str)
            elif minute2 <= 59 and minute1 > 59:
                if minute2 < 10:
                    hour_str += '0' + str(minute2)
                else:
                    hour_str += str(minute2)
                result.append(hour_str)
        if len(result) == 0:
            return ''
        sorted_result = sorted(result, key=lambda x:int(x), reverse=True)
        return sorted_result[0][:2] + ':' + sorted_result[0][2:]


if __name__ == '__main__':
    solution = Solution()
    A = [9,0,7,7]
    print(solution.largestTimeFromDigits(A))
