class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


E1 = Employee("Mehak", 40000)
E2 = Employee("Ashok", 50000)
E3 = Employee("Viren", 60000)
# part(a)
E1.salary = 70000

# part(b)
del E3
