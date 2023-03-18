class Person:
    moods = ("happy", "tired", "lazy")

    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.__mood = "happy"  #private
        self.__healthRate = 100  #private

    def sleep(self, hours):
        if hours == 7:
            self.__mood = "happy"  #private
        elif hours < 7:
            self.__mood = "tired"  #private
        else:
            self.__mood = "lazy"  #private

    def eat(self, meals):
        if meals == 3:
            self.__healthRate = 100  #private
        elif meals == 2:
            self.__healthRate = 75  #private
        else:
            self.__healthRate = 50  #private

    def buy(self, items):
        self.money -= (10 * items)

    # Getter and setter for mood
    def get_mood(self):
        return self.__mood

    def set_mood(self, mood):
        self.__mood = mood

    # Getter and setter for healthRate
    def get_healthRate(self):
        return self.__healthRate

    def set_healthRate(self, healthRate):
        self.__healthRate = healthRate

class Employee(Person):
    def __init__(self, name, money, id, car, distanceToWork):
        super().__init__(name, money)
        self.__id = id  #private
        self.car = car
        self.__email = 'example@gmail.com'  #private
        self.__salary = min(1000, 1000)  #private

        self.distanceToWork = distanceToWork

    def work(self, hours):
        if hours == 8:
            self.set_mood("happy")
        elif hours < 8:
            self.set_mood("tired")
        else:
            self.set_mood("lazy")

    def drive(self, distance):
        time = distance / self.car.velocity
        self.car.run(self.car.velocity, distance)

    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount

    # Getter and setter for id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    # Getter and setter for email
    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    # Getter and setter for salary
    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = min(salary, 1000)

class Office:
    employeesNum = 0

    def __init__(self, name):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, empId):
        for employee in self.employees:
            if employee.get_id() == empId:
                return employee
        return None

    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1

    def fire(self, empId):
        for employee in self.employees:
            if employee.get_id() == empId:
                self.employees.remove(employee)
                Office.employeesNum -= 1
                return True
        return False

    def deduct(self, empId, deduction):
        employee = self.get
