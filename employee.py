class Employee:
    def __init__(self, name, surname, age, salary):
        self.name=name
        self.surname=surname
        self.age=age
        self.salary=salary

    def info(self):
        print("saxeli:",self.name,"","gvari:",self.surname,"","asaki:",self.age,"","xelfasi:",self.salary)


employees = []

with open("dataset1.csv", "r") as dataset:
    data = [line.split(",") for line in dataset.read().split("\n")][1:-1]
    employees = [Employee(name, surname, age, salary) for [name, surname, age, salary] in data]

print({min(employees, key=lambda employee: employee.salary).info()})
print({max(employees, key=lambda employee: employee.age).info()})


