from person import Person,Employee,Customer


person_profile_1 = Person(name="Rafika", age=23, sex="Female")

#We tried to access name attribute without print function and it do not work, but it work on Jupyter
# print(person_profile.name)

#Trying out our methods
person_profile_1.change_name("Ashley")

person_profile_1.change_age(25)

person_profile_1.change_sex("female")


#instantiate employee object and pass arguments
lilly_employee_profile= Employee("Lilly", 35, "female", "Sales Rep")

#Accessing the attributes
print(lilly_employee_profile.job)


print(lilly_employee_profile.name)

print(lilly_employee_profile.age)

#calling our update age method on our object
#which allows user to input their age
lilly_employee_profile.update_age()

#attempt encapsulation, when print, the output says:
#"AttributeError: 'Employee' object has no attribute 'salary'"
#is this because it is private?
lilly_employee_profile.request_salary()

# print(lilly_employee_profile.salary)


#instantiate the Customer class
customer=Customer("Jack",46,"Male","Accountant")

#calling our measure satisfaction method and change tier method
customer.measure_satisfaction()

customer.change_tier()

# print(customer.customer_tier)








