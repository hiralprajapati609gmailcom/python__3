class Student:
      def getData(self,fname,lname):
          self.f=fname
          self.l=lname
      def putData(self):
          print("first Name : ",self.f)
          print("last  Name : ",self.l)
s1=Student()
s1.getData("Hiral","Prajapati")
s1.putData()
