#Define a class is a student
class STUDENT:
    #Method
    def getstudent(self):
        self.name=input("\nName:")
        self.age=input("Age:")
        self.genter=input("Gender:")
class TEST(STUDENT):
    def getmarks(self):
        self.stuClass=input("Class:")
        print("Enter the marks of respective subject:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.programming=int(input("Programming:"))
        self.calulas=int(input("Calulas:"))
        self.english=int(input("English:"))
        self.islamyat=int(input("Islamyat:"))
        self.physics=int(input(" Physics:"))
        self.computing=int(input("Computing:"))
        print("**************************************")
        
class MARKS(TEST):
    def display (self):
        print("\nName:",self.name)
        print("\nAge:",self.age)
        print("\nGender:",self.genter)
        print("\nStudy in:",self.stuClass)
        Total=(self.programming+self.calulas+self.english+self.islamyat+self.physics+self.computing)
        print("\nTotal marks:",Total)
        print (input("Enter the GPA:"))
 
m1=MARKS()
m1.getstudent()
m1.getmarks()
m1.display()

