# Person class has four instance attributes: name, money, mood, and healthRate
# It also has three methods: sleep(), eat(), and buy().
class Person:
    moods = ("happy", "tired", "lazy")
    
    def __init__(self, name, money):
        self.name = name
        self.money = money
        self.__mood = mood  #private
        self.__healthRate = healthRate   #private
        
    def sleep(self, hours):
        if hours == 7:
            self.mood = "happy"
        elif hours < 7:
            self.mood = "tired"
        else:
            self.mood = "lazy"
            
    def eat(self, meals):
        if meals == 3:
            self.healthRate = 100
        elif meals == 2:
            self.healthRate = 75
        else:
            self.healthRate = 50
            
    def buy(self, items):
        self.money -= (10 * items)
   
# Employee class is a subclass of Person and adds five more instance attributes: id, car, email, salary, and distanceToWork.
# It also has three methods: work(), send_mail(), and drive().         
class Employee(Person):
    def __init__(self, name, money, id, car, distanceToWork):
        super().__init__(name, money)
        self.id = id #private
        self.car = car
        self.email = 'example@gmail.com' #private, stter and getter
        self.salary = 1000
        # min(1000, salary)  #private, stter and getter
        self.distanceToWork = distanceToWork
        
    def work(self, hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "tired"
        else:
            self.mood = "lazy"
               
        
    def drive(self, distance):
        time = distance / self.car.velocity
        self.car.run(self.car.velocity, distance)
        
    def refuel(self, gasAmount=100):
        self.car.fuelRate += gasAmount
        
#  Office class has two class attributes: employeesNum and name. 
# It also has five methods: get_all_employees(), get_employee(), hire(), fire(), deduct(), reward(), and check_lateness(). 
       
class Office:
    employeesNum = 0
    
    def __init__(self, name):
        self.name = name
        self.employees = []
        
    def get_all_employees(self):
        return self.employees
    
    def get_employee(self, empId):
        for employee in self.employees:
            if employee.id == empId:
                return employee
        return None
    
    def hire(self, employee):
        self.employees.append(employee)
        Office.employeesNum += 1
        
    def fire(self, empId):
        for employee in self.employees:
            if employee.id == empId:
                self.employees.remove(employee)
                Office.employeesNum -= 1
                return True
        return False
    
    def deduct(self, empId, deduction):
        employee = self.get_employee(empId)
        if employee:
            employee.salary -= deduction
            
    def reward(self, empId, reward):
        employee = self.get_employee(empId)
        if employee:
            employee.salary += reward
            
    def check_lateness(self, empId, moveHour):
        employee = self.get_employee(empId)
        if not employee:
            return False
        targetHour = 9
        distance = employee.distanceToWork
        velocity = employee.car.velocity
        if Office.calculate_lateness(targetHour, moveHour, distance, velocity):
            employee.salary -= 10
        else:
            employee.salary += 10
            
   
