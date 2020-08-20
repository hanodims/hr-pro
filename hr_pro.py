from datetime import datetime
class Employee:
    
    def __init__(self, name, age, salary,employment_year):
        self.name = name
        self.age = age
        self.salary = int(salary)
        self.employment_year = self.get_working_years(int(employment_year))
        
    
    def get_working_years(self,employment_year):
        return (datetime.today().year - employment_year )
    
    def __str__(self):
        employee = self.name
        return  f"\nName: {self.name}, Age: {self.age}, Salary: {self.salary}, Working year: {self.employment_year}"
        



class Manager(Employee):
    
    def __init__(self, name, age, salary, employment_year,bonus_percentage):
        super().__init__(name, age, salary, employment_year)
        self.bonus_percentage = self.get_bonus(float(bonus_percentage))
    
    def get_bonus(self,bonus_percentage):
        return bonus_percentage * self.salary
    def __str__(self):
        return super().__str__() + f", Bonus: {self.bonus_percentage} "

        
def main():
    emp = []
    man = []
    print('\nWelcome to HR Pro 2019')
    print('Options:')
    print("""
    1. Show Employees
    2. Show Managers
    3. Add An Employee
    4. Add A Manager
    5. Exit """)
    choice = input('\nWhat would you like to do? ')
    print('-'*20)
    while choice != '5':
        
        print()
        if choice == '1':
            print("Employees")
            for i in emp:
                print(i)
        if choice == '2':
            print('Managers')
            for i in man:
                print(i)
        if choice == '3':
            name = input('Name: ')
            age = input('Age: ')
            salary = input('Salary: ')
            emp_year = input('Employement year: ')
            print()
            a = Employee(name,age,salary,emp_year)
            emp.append(a)
            print("\nEmployee added succesfully")
            print('-'*15)
            
        if choice == '4':
            name = input('Name: ')
            age = input('Age: ')
            salary = input('Salary: ')
            emp_year = input('Employement year: ')
            bonus_percent = input('Bonus percentage: ')
            print()
            a = Manager(name,age,salary,emp_year,bonus_percent)
            man.append(a)
            print("\nManager added succesfully")
            print('-'*15)

        choice = input('\nWhat would you like to do? ')
        

        #Not Finished Yet
       


if __name__ == '__main__':
	main()
