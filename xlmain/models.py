from djongo import models

# Create your models here.
class CSE(models.Model):
    Id_Number                =   models.CharField(max_length=10)
    Student_Name             =   models.CharField(max_length=50)
    Discrete_Mathematics     =   models.CharField(max_length=2)
    Engineering_Physics      =   models.CharField(max_length=2)
    Programming_through_Cpp  =   models.CharField(max_length=2)
    Data_Structures          =   models.CharField(max_length=2)
    Environmental_Sciences   =   models.CharField(max_length=2)
    Physics_Lab              =   models.CharField(max_length=2)
    Cpp_Lab                  =   models.CharField(max_length=2)
    Data_Structures_Lab      =   models.CharField(max_length=2)
    CGPA                     =   models.FloatField()

    def values(self):#function to return keys
        return [self.Id_Number,self.Student_Name,self.Discrete_Mathematics,self.Engineering_Physics,self.Programming_through_Cpp,self.Data_Structures,self.Environmental_Sciences,self.Physics_Lab,self.Cpp_Lab,self.Data_Structures_Lab,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Discrete_Mathematics","Engineering_Physics","Programming_through_Cpp","Data_Structures","Environmental_Sciences","Physics_Lab","Cpp_Lab","Data_Structures_Lab","CGPA"]
class ECE(models.Model):
    Id_Number	             = models.CharField(max_length=10)
    Student_Name	         = models.CharField(max_length=50)
    Basic_Electronics	     = models.CharField(max_length=2)
    Basic_Electronics_Lab	 = models.CharField(max_length=2)
    Computational_Lab	     = models.CharField(max_length=2)
    English_1	             = models.CharField(max_length=2)
    Mathematical_Methods	 = models.CharField(max_length=2)
    Network_Theory	         = models.CharField(max_length=2)
    OOPS                     = models.CharField(max_length=2)
    OOPS_Lab	             = models.CharField(max_length=2)
    Signals_and_Systems	     = models.CharField(max_length=2)
    CGPA                     = models.FloatField()

    def values(self):
        return [self.Id_Number,self.Student_Name,self.Basic_Electronics,
                self.Basic_Electronics_Lab,self.Computational_Lab,
                self.English_1,self.Mathematical_Methods,self.Network_Theory,
                self.OOPS,self.OOPS_Lab,self.Signals_and_Systems,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Basic_Electronics",
                "Basic_Electronics_Lab","Computational_Lab",
                "English_1","Mathematical_Methods","Network_Theory",
                "OOPS","OOPS_Lab","Signals_and_Systems","CGPA"]

class MECH(models.Model):
    Id_Number= models.CharField(max_length=10)
    Student_Name= models.CharField(max_length=50)
    Engineering_Mechanics= models.CharField(max_length=2)
    Material_Science_and_Metallurgy = models.CharField(max_length=2)
    Material_Science_and_Metallurgy_Lab= models.CharField(max_length=2)
    Mathematical_Methods = models.CharField(max_length=2)
    PDS = models.CharField(max_length=2)
    PDS_Lab= models.CharField(max_length=2)
    Environmental_Sciences = models.CharField(max_length=2)
    CGPA = models.CharField(max_length=2)

    def values(self):
        return [self.Id_Number,self.Student_Name,self.Engineering_Mechanics,
                self.Material_Science_and_Metallurgy,self.Material_Science_and_Metallurgy_Lab,
                self.Mathematical_Methods,self.PDS,self.PDS_Lab,
                self.Environmental_Sciences,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Engineering_Mechanics",
                "Material_Science_and_Metallurgy","Material_Science_and_Metallurgy_Lab",
                "Mathematical_Methods","PDS","PDS_Lab",
                "Environmental_Sciences","CGPA"]


class CIVIL(models.Model):
    Id_Number= models.CharField(max_length=10)
    Student_Name= models.CharField(max_length=50)
    Engineering_Physics= models.CharField(max_length=2)
    Mathematical_Methods = models.CharField(max_length=2)
    BEEE= models.CharField(max_length=2)
    Engineering_mechanics = models.CharField(max_length=2)
    Engineering_Geology = models.CharField(max_length=2)
    Environmental_Studies= models.CharField(max_length=2)
    Engineering_Physics_Lab = models.CharField(max_length=2)
    Workshop = models.CharField(max_length=2)
    CGPA                     = models.FloatField()


    def values(self):
        return [self.Id_Number,self.Student_Name,self.Engineering_Physics,
                self.Mathematical_Methods,self.BEEE,
                self.Engineering_mechanics,self.Engineering_Geology,self.Environmental_Studies,
                self.Engineering_Physics_Lab,self.Workshop,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Engineering_Physics",
                "Mathematical_Methods","BEEE",
                "Engineering_mechanics","Engineering_Geology","Environmental_Studies",
                "Engineering_Physics_Lab","Workshop","CGPA"]
        


class CHEM(models.Model):
    Id_Number= models.CharField(max_length=10)
    Student_Name= models.CharField(max_length=50)
    Engineering_Physics= models.CharField(max_length=2)
    Engineering_Mathematics_2 = models.CharField(max_length=2)
    PDS= models.CharField(max_length=2)
    Chemical_Process_Calculations = models.CharField(max_length=2)
    Fluid_Mechanics = models.CharField(max_length=2)
    Environmental_Sciences= models.CharField(max_length=2)
    PDS_Lab = models.CharField(max_length=2)
    CGPA = models.CharField(max_length=2)

    def values(self):
        return [self.Id_Number,self.Student_Name,self.Engineering_Physics,
                self.Engineering_Mathematics_2,self.PDS,
                self.Chemical_Process_Calculations,self.Fluid_Mechanics,self.Environmental_Sciences,
                self.PDS_Lab,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Engineering_Physics",
                "Engineering_Mathematics_2","PDS",
                "Chemical_Process_Calculations","Fluid_Mechanics","Environmental_Sciences",
                "PDS_Lab","CGPA"]


class MME(models.Model):
    Id_Number= models.CharField(max_length=10)
    Student_Name= models.CharField(max_length=50)
    Engineering_Chemistry= models.CharField(max_length=2)
    Engineering_Chemistry_Lab = models.CharField(max_length=2)
    Materials_Thermodynamics= models.CharField(max_length=2)
    Engineering_Mathematical_2 = models.CharField(max_length=2)
    Metallography_Lab = models.CharField(max_length=2)
    Physical_Metallurgy= models.CharField(max_length=2)
    PDS = models.CharField(max_length=2)
    PDS_Lab = models.CharField(max_length=2)
    CGPA                     = models.FloatField()

    def values(self):
        return [self.Id_Number,self.Student_Name,self.Engineering_Chemistry,
                self.Engineering_Chemistry_Lab,self.Materials_Thermodynamics,
                self.Engineering_Mathematical_2,self.Metallography_Lab,self.Physical_Metallurgy,
                self.PDS,self.PDS_Lab,self.CGPA]
    @classmethod
    def keys(cls):
        return ["Id_Number","Student_Name","Engineering_Chemistry",
                "Engineering_Chemistry_Lab","Materials_Thermodynamics",
                "Engineering_Mathematical_2","Metallography_Lab","Physical_Metallurgy",
                "PDS","PDS_Lab","CGPA"]


