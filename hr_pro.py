from datetime import datetime
class Employee:
    
    def __init__(self, name, age, salary,employment_year):
        self.name = name
        self.age = age
        self.salary = salary
        self.employment_year = employment_year
        self.emp = []
        self.emp.append({
            'name' : self.name ,
            'age' : self.age,
            'salary' : self.salary,
            'employment_year' : self.employment_year 
        })
    
    def get_working_years(self):
        return (datetime.today() - self.employment_year)
    
    def __str__(self):
        return super().__str__(self.emp)



class Manager(Employee):
    
    def __init__(self, name, age, salary, employment_year,bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = bonus_percentage
        self.man = []
        self.man.append([{
            'name' : self.name,
            'age' : self.age,
            'salary' : self.salary,
            'employment_year' : self.employment_year,
            'bonus_percentage' : self.bonus_percentage
        }])
    
    def get_bonus(self):
        return self.bonus_percentage * self.salary
    def __str__(self):
        return super().__str__(self.man)

        
def main():
    name = 'e'
    age = 25
    salary = 3000
    emp_year = 2018
    bonus_percentage = .3
    print('Welcome to HR Pro 2019')
    print('Options:')
    print("""
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit """)
    choice = input('\nWhat would you like to do? ')
    print('-'*15)
    if choice == '1':
        lst = Employee(name,age,salary,emp_year)
        print(lst.emp)
    elif choice == '2':
        lst = Manager(name,age,salary,emp_year,bonus_percentage)
        print(lst.man)
    elif choice == '3':
        name = input('Name: ')
        age = input('Age: ')
        salary = input('Salary: ')
        emp_year = input('Employement year: ')
        a = Employee(name,age,salary,emp_year)
        print(a.emp)
        #a.emp.append(name,age,salary,emp_year)

        #Not Finished Yet
       


if __name__ == '__main__':
	main()
