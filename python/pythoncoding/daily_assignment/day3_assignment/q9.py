#Use the Datetime Module:
#Write a program that imports the datetime module and uses it to:
#Get and print the current date and time .
#Calculate and print the number of days between two dates.
#Format and print the current date in the format "DD-MM-YYYY"

from datetime import datetime

now = datetime.now()
print("Current date and time:",now)

date1= datetime(2025,1, 1)
date2= datetime(2026,1, 1)

difference = date2 - date1
print("Number of days between:",difference.days)

formatted_date = now.strftime("%d-%m-%y")
print("Fromatted date:", formatted_date)