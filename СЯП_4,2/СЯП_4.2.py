class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income

class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return f"{self.name} {self.surname}"

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

employee = Position(name="John", surname="Doe", position="Developer", income={"wage": 5000, "bonus": 10000})

print("Name:", employee.name)
print("Surname", employee.surname)
print("Position:", employee.position)
print("Income:", employee._income)

print("Full Name:", employee.get_full_name())
print("Total Income:", employee.get_total_income())
