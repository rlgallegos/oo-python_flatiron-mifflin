from lib.employee import Employee

class Manager:

    all = []
    departments = set()
    
    def __init__(self, name, department, age):
        self.name = name
        self.department = department
        self.age = age
        self.employees = []
        self.add_manager()
        Manager.departments.add(self.department)
    
    def add_manager(self):
        Manager.all.append(self)

    def hire_employee(self, employee_name, employee_salary):
        new_employee = Employee(employee_name, employee_salary, self)
        self.employees.append(new_employee)

    @classmethod
    def all_departments(cls):
        return list(cls.departments)
    
    @classmethod
    def average_age(cls):
        age_list = [manager.age for manager in cls.all]
        return float( sum(age_list) / len(age_list) )