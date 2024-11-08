class student:
    def getstudent(self):
        self.name=input("\nName:")
        self.age=input("Age:")
        self.genter=input("Gender:")
class test(student):
    def getmarks(self):
        self.stuClass=input("Class:")
        print("Enter the marks of respective subject:")
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
        self.programming=int(input("Programming:"))
        self.calulas=int(input("Calulas:"))
        self.english=int(input("English:"))
        self.islamyat=int(input("Islamyat:"))
        self.physics=int(input("Physics:"))
        self.computing=int(input("Computing:"))
        print("**************************************")
        
class marks(test):
    def display (self):
        print("\nName:",self.name)
        print("\nAge:",self.age)
        print("\nGender:",self.genter)
        print("\nStudy in:",self.stuClass)
        Total=(self.programming+self.calulas+self.english+self.islamyat+self.physics+self.computing)
        print("\nTotal marks:",Total)
        percentage = (round(Total / 6, 0))
        print("The total percentage is:"+ str(percentage),"%")
        
        if percentage >=85 and percentage <=85:
            print("GPA:",4.0 )
        elif percentage >=80 and percentage <=84:
            print ("GPA:",3.67)
        elif percentage >=75 and percentage <=79:
            print ("GPA:",3.33)
        elif percentage >=70 and percentage <=74:
            print ("GPA:",3.00)
        elif percentage >=65 and percentage <=69:
            print ("GPA:",2.67)
        elif percentage >=61 and percentage <=64:
            print ("GPA:",2.33)
        elif percentage >=58 and percentage <=60:
            print ("GPA:",2.00)
        elif percentage >=55 and percentage <=57:
            print ("GPA:",1.67)
        elif percentage >=53 and percentage <=54:
            print ("GPA:",1.33)
        elif percentage >=50 and percentage <=52:
            print ("GPA:",1.00)
        else:
            print ("GPA:",0)
        
   
m1=marks()
m1.getstudent()
m1.getmarks()
m1.display()

