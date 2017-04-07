class Company(object):
    """This represents a company in which people work"""

    def __init__(self, name, title, start_date):
        self.name = name
        self.title = title
        self.start_date = start_date
        self.employees = set()

    def get_name(self):
        """Returns the name of the company"""
 
        return self.name


    def add_employee(self, employee):
    	self.employees.add(employee)

    def list_employees(self):
    	for each in self.employees:
    		print("{} is the {} who works for {}".format(each.name, each.title, self.name) + ".") 


class Employee():
	'''This represents an employee of a company'''
	def __init__(self, name, title, start_date):	
		self.name = name
		self.title = title
		self.start_date = start_date

	def get_name(self):

		return self.name

	def get_title(self):

		return self.title

	def get_start_date(self):

		return self.start_date

company = Company("Starting Over", "One More Time", "April 4, 2017")
print(("{}, whose title is {}, began on {}").format(company.name, company.title, company.start_date) + ".")
jeremy = Employee("Jeremy", "Software Developer", "January 2, 2017")
print(("{} is a {} who started on {}.").format(jeremy.name, jeremy.title, jeremy.start_date))
shawn = Employee("Shawn", "President", "April 6, 2017")
elijah = Employee("Elijah", "Intern", "April 1, 2017")
company.add_employee(jeremy)
company.add_employee(shawn)
company.add_employee(elijah)
company.list_employees()