class Employee:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def __str__(self):
        return f"Name : {self.name}\nAge : {self.age}\nSalary : {self.salary}\n"


class EmployeeManager:
    def __init__(self):
        self.employees = []

    def addEmployee(self):
        print("Please enter employee's information")
        name = input("Name: ")
        age = int(input("Age: "))
        salary = int(input("Salary: "))
        print()
        self.employees.append(Employee(name, age, salary))

    def showEmployees(self):
        if len(self.employees) == 0:
            print("Employee list is empty")
        else:   
            for employee in self.employees:
                print(employee)

    def deleteEmployeesByAgeRange(self, fromAge, toAge):
        self.employees = list(filter(lambda x: not (x.age >= fromAge and x.age <= toAge), self.employees))
        print("Deleted successfully\n")

    def searchEmployee(self, name):
        for employee in self.employees:
            if employee.name == name:
                return employee
        return None
              
    def updateSalary(self, name, salary):
        employee = self.searchEmployee(name)
        if employee is None:
            print("Employee not found!")
        else:
            employee.salary = salary
            print(f"{employee.name}'s salary updated successfully")

class FrontendManager:
    def __init__(self):
        self.EmployeeManager = EmployeeManager()

    def showMenu(self):
        while True:
            print("\n\t\t\tMain Menu\n")
            print("\t1.Add Employee")
            print("\t2.Show Existing Employees")
            print("\t3.Delete an Employee based on age range")
            print("\t4.Updating Employee Salary By Name")
            print("\t5.Exit\n")
            try:
                choice = int(input("Choose your option "))
                if choice == 1:
                    self.EmployeeManager.addEmployee()
                elif choice == 2:
                    self.EmployeeManager.showEmployees()
                elif choice == 3:
                    fromAge = int(input("From age: "))
                    toAge = int(input("To age: "))
                    self.EmployeeManager.deleteEmployeesByAgeRange(fromAge, toAge)
                elif choice == 4:
                    name = input("Enter employee's name: ")
                    salary = int(input("Enter employee's salary: "))
                    self.EmployeeManager.updateSalary(name, salary)
                elif choice == 5: 
                    break
            except Exception:
                print("Please enter a valid option!")
                





        

            

