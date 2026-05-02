
cc=int(input(' c code: '))
cn=input('c name:')
ci=input('c city: ')
rno=int(input('Roll no:'))
sn=input('S Name:')
m1=int(input('M1:'))
m2=int(input('M2:'))
m3=int(input('M3:'))


#project = college(ccode=cc,cname=cn,ccity=ci)
#
#project.welcome_messege()
#project.display_college_details()

project = student(ccode=cc,cname=cn,ccity=ci,rno=rn,sname=sn,
                   m1=m1,m2=m2,m3=m3)
project.welcome_messege()
project.display_college_details()
print(f'Roll no:{project.rollno} \t Name:{project.stuname} \n'
      f'Total:{project.calculate_total()} \nAverage:{project.calculate_average()}')