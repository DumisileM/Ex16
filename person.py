class Person:
    numCreated = 0

    def __init__(self, name, age, sex,):

        self.name = name
        self.age = age
        self.sex = sex
        Person.numCreated +=1

    #Methods
    def change_name (self, name):

        print("My name is: ", name)

    def change_age(self, age):

        print("I am {} years old".format(age))


    def change_sex(self, sex):

        print(sex)

class Employee(Person):

    def __init__(self,name,age,sex,job,salary=0):
        super().__init__(name,age,sex)
        self.job=job
        self._salary=salary


    def update_age(self):

        age=input("Please update your age: ")
        print(age)

    def request_salary(self):
        _salary=int(input("Enter Salary: "))




class Customer(Employee):
    def __init__(self,name,age,sex,job,customer_tier="standard",satisfaction=0):
        super().__init__(name,age,sex,job)
        self.customer_tier=customer_tier
        self.satisfaction=satisfaction

    def measure_satisfaction(self):
        make_value=input("On a scale of 1-5, how satisfied are you with our service? ")
        value=int(make_value)
        if value == 5:
            return "Customer is satisfied with service"

        elif 3 <= value <= 4:
            return "Customer is fairly satisfied"

        else:
            return "Customer is not satisfied"

