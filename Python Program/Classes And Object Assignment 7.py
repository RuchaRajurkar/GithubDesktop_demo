# Write a program to implement a class “student” with the following members. Name of the
# student. Marks of the student obtained in three subjects. Function to assign initial values.
# Function to compute total average. Function to display the student’s name and the total marks.
# Write an appropriate main() function to demonstrate the functioning of the above.

class Student:
    def __init__(self,name,physics,math,history):
        self.n=name
        self.p=physics
        self.m=math
        self.h=history
    def average(self):
        self.totalaverage=(self.p+self.m+self.h)/3
        self.totalmarks=(self.p+self.m+self.h)
    def show(self):
        print("Student Name:",self.n)
        print("Total Marks:",self.totalmarks)
        print("Total Average:", self.totalaverage)
n=input("Enter Name")
s1=Student(n,85,80,60)
s1.average()
s1.show()
print("**************************************")
s2=Student("Pooja Sonawane",80,80,90)
s2.average()
s2.show()