#python object oriented programming series
import datetime
my_date = datetime.date(2016, 7 ,10)
class Employee:
	#pass
	num_of_employees = 0
	raise_amount = 1.04
	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.pay = pay
		self.email = first + '.' + last + '@company.com'

		Employee.num_of_employees += 1
	def fullname(self):
		return '{} {}'.format(self.first, self.last)

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amount)

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
	@classmethod #must have class decoration PER method 
	def from_string(cls, emp):
		first, last, pay = emp.split('-')
		return cls(first, last, pay)

	@staticmethod # statics dont take in a self of cls
	def is_workday(day):
		if day.weekday() == 5 or day.weekday() == 6:
			return False
		return True

emp1 = Employee('bob','smith', 60000)
emp2 = Employee('sue', 'jenkins', 50000)

print(Employee.is_workday(my_date))
# emp_str_1 = 'John-Doe-70000'

# new_emp_1 = Employee.from_string(emp_str_1)

# print(new_emp_1.email)
# print(new_emp_1.pay)

# print(Employee.num_of_employees)

