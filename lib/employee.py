

class Employee:

    all = []
    
    def __init__(self, name, salary, manager):
        self.name = name
        self.salary = salary
        self.manager = manager
        Employee.all.append(self)
    
    @classmethod
    def paid_over(cls, amount):
        return [employee for employee in cls.all if employee.salary > amount]

    @classmethod
    def find_by_department(cls, department):
        for employee in Employee.all:
            if employee.manager.department == department:
                return employee

    def tax_bracket(self):
        employee_list = []
        for employee in Employee.all:
            if employee.salary >= self.salary - 1000 and employee.salary <= self.salary + 1000:
                employee_list.append(employee)
        return employee_list