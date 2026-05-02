from email.encoders import encode_noop
from tkinter.font import names


class EmployeeDetails:

    def __init__(self,empno,ename,basic_pay):
        self.empno =100
        self.ename =' abc '
        self.basic_pay = 1000.0
        self.da = 20.0
        self.hra = 10.0
        self.pf = 5.5

    @property
    def empno(self):
        return self.__empno

    @empno.setter
    def empno(self):
        self.__empno = eno

    @property
    def ename(self):
        return self.__ename

    @ename.setter
    def ename(self):
        self.__ename = name

    @property
    def basic_pay(self):
        return self.__basic_pay

    @basic_pay.setter
    def basic_pay(self):
        self.__basic_pay = pay
    #getter
    def get_empno(self):
        return self.__empno

    def get_ename(self):
        return self.__ename

    def get_basic_pay(self):
        return self.__basic_pay
    #setters:

    def set_ename(self,empno):
        self.__empno= empno

    def set_ename(self,ename):
        self.__ename = ename

        def set_basic_pay(self, basic_pay):
            self.__basic_pay = basic_pay

    def calculate_allowance(self):
        allowance = (self.basic_pay * self.da /100) + (self.basic_pay * self.hra /100)
        return allowance

    def calculate_deduction(self):
        deduction = (self.basic_pay * self.pf / 100)
        return deduction

    def calculate_netsal(self):
        netsal = self.basic_pay + self.calculate_allowance() - self.calculate_deduction()
        return netsal
