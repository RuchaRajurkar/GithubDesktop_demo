# Create a class that captures students.Each student has first name,last name,class year and major.
# Create Two examples of students.

class Students:
    def __init__(self):
        self.firstname = input("Enter the first name:")
        self.lastname = input("Enter the last name:")
        self.classyear = input("Enter the class year:")

    def show(self):
        print("Students Detail".center(50,"*"))
        print("First Name:",self.firstname)
        print("Last Name:", self.lastname)
        print("Class Year:", self.classyear)


s1=Students()
s1.show()
s2=Students()
s2.show()

