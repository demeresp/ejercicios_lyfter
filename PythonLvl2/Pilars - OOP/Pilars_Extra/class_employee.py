class Employee:
    def __init__(self, name, salary):
        self._name = name
        self.employee_salary = salary


    @property
    def employee_salary(self):
        return self._salary


    @employee_salary.setter
    def employee_salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative.")
        self._salary = value


    @property
    def show_info(self):
        return f"Employee Name: {self._name}, Salary: {self._salary}"


emp1 = Employee("John", 100)
print(emp1.show_info)