#inheritance
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

class Developer(Employee):
	raise_amount = 1.10
	def __init__(self, first, last, pay, prog_lang):
		super().__init__(first,last,pay) # this allows the parent class to handle the items it already has handled.
		self.prog_lang = prog_lang #thanks to super all we need to assign is the prog_lang

class Manager(Employee):
	def __init__(self,first,last,pay, employees=None):
		super().__init__(first,last,pay)
		if employees is None:
			self.employees = []
		else:
			self.employees = employees

	def add_employee(self, emp):
		if emp not in self.employees:
			self.employees.append(emp)

	def remove_employee(self, emp):
		if emp in self.employees:
			self.employees.remove(emp)

	def print_emps(self):
		for emp in self.employees:
			print('-->', emp.fullname())


############ Action code #######################
dev_1 = Developer('Bob', 'smith', 50000, 'Java')
dev_2 = Developer('Jill', 'smith', 50000, 'Python')

mgr_1 = Manager('Sue', 'Jackson', 90000, [dev_1])

mgr_1.add_employee(dev_2)
print(mgr_1.email)
mgr_1.print_emps()

mgr_1.remove_employee(dev_1)

mgr_1.print_emps()

# print(dev_1.prog_lang)
# print(dev_2.prog_lang)


