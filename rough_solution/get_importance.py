# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: List(Employee)
        :type id: int
        :rtype: int
        """
        employee = None
        for each in employees:
            if each.id == id:
                employee = each
        subordinates = employee.subordinates
        importance = employee.importance
        if not subordinates:
            return importance
        else:
            total = importance
            for each_id in subordinates:
                total += self.getImportance(employees, each_id)
            return total


if __name__ == '__main__':
    solution = Solution()
    employees_list = [[1, 15, [2]], [2, 10, [3]], [3, 5, []]]
    employees = []
    for each in employees_list:
        employee = Employee(each[0], each[1], each[2])
        employees.append(employee)
    print(solution.getImportance(employees, 1))
