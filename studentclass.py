class Student:
    t = 0.0
    gr = 0.0
    def __init__(self):
        self.name = " "
        self.math = 0
        self.physics = 0
        self.chemistry = 0
        self.english = 0
        self.hindi = 0
        print("Constructor Called")
    def inputData(self):
        self.name = str(input("Enter the name of student: "))
        self.math = int(input("Enter the marks of Maths: "))
        self.physics = int(input("Enter the marks of Physics: "))
        self.chemistry = int(input("Enter the marks of Chemistry: "))
        self.english = int(input("Enter the marks of English: "))
        self.hindi = int(input("Enter the marks of Hindi: "))
    def showData(self):
        print("Name of Student is : ",self.name)
        print("Marks of Maths : ",self.math)
        print("Marks of Physics : ",self.physics)
        print("Marks of Chemistry : ",self.chemistry)
        print("Marks of English : ",self.english)
        print("Marks of Hindi : ",self.hindi)
    def total(self):
        Student.t = self.math + self.physics + self.chemistry + self.english + self.hindi
        Student.gr = (Student.t/500)*100
        if (Student.gr > 70):
            print(self.name," Got total marks: ",Student.t," First Division with grade :",Student.gr)
        elif (Student.gr > 50):
            print(self.name," Got total marks: ",Student.t," Second Division with grade :",Student.gr)
        else:
            print(self.name," Got total marks: ",Student.t," Fail with grade :",Student.gr)

obj = Student()
obj.inputData()
obj.showData()
obj.total()
            
        
        
        
