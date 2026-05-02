from oopsconcept.employeedetails import EmployeeDetails

 # driver
eno = int(input('Emp no: '))
ename=input('Emp name: ')
bp = float(input('Basic pay: '))

employee = EmployeeDetails(eno,ename, bp)

print('Emp no:', employee.empno)
print('Emp name: ', employee.ename)
print('Basic pay:', employee.basic_pay)
print('salary:', employee.calculate_netsal())
