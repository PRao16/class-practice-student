# Create Class called Student and create objects as Students. Create Methods for first Name , Last Name. Print out names. Created a method called grades
#and give grades. create a method for average grades. Highest grade and lowest grade. Add more methods that objects(students can use)

class student:
    def __init__(self,FN,LN,age,Math,English,Sciene):
        self.FName=FN
        self.LName=LN
        self.age=age
        self.MathGrade=Math
        self.EnglishGrade=English
        self.ScienceGrade=Sciene
    def fullName(self):
        self.fullName=self.FName + ' ' + self.LNameubd
        return self.fullName
    def GradeAverage(self):
        self.GradeAverage=(self.MathGrade+self.EnglishGrade+self.ScienceGrade)/3
        return self.GradeAverage
    def MathplusArt(self,Art):
        self.ArtGrade=Art
        self.MathplusArt=self.MathGrade + self.ArtGrade
        return self.MathplusArt
    def namechange(self,NewLN):
        LName=NewLN
        return self.namechange








student1=student('John','Davis',8,34,45,56)
print(student1.FName)
print('student1 is ' + str(student1.age) + ' years old')
print("student1's full name is ", student1.fullName())
print("student1's average grade is " ,  str(student1.GradeAverage()))
MathplusArt=student1.MathplusArt(70)
print("student1's total of Math and Art Grades is ",MathplusArt)
self.NewLN='Peters'
print("student1's full name is ", student1.fullName())

student2=student('Paul','Simon',10,45,78,90)
print(student2.FName + ' ' + student2.LName)
print('student2 is ' + str(student2.age) + ' years old')
print("student2's full name is ", student2.fullName())
print("student2's average grade is " ,  str(student2.GradeAverage()))




