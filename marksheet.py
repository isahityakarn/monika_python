#user input for marksheet
import os


name=input("Enter student name: ")
hindi=int(input("Enter Hindi marks: "))
english=int(input("Enter English marks: "))
maths=int(input("Enter Maths marks: "))

#using the input data to calculate total and percentage
total=hindi+english+maths
percentage=total/3
os.system('cls')
#displaying the marksheet
print("********** Marksheet **********")
print("Student Name:", name)
print("your English marks are:", english)
print("your Hindi marks are:", hindi)
print("your Maths marks are:", maths)
print("your total marks are:", total)
print("your percentage is:", percentage,"%")