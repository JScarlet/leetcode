class Solution:
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        result = set()
        for email in emails:
            left_right = email.split('@')
            left = left_right[0]
            right = left_right[1]
            left = left.replace('.', '')
            if '+' in left:
                left = left[:left.find('+')]
            result.add(left + '@' + right)
        return len(result)


if __name__ == '__main__':
    solution = Solution()
    emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(solution.numUniqueEmails(emails))
