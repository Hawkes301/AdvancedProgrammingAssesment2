
class  OnLicenceHousingAllocationSystem:
    def __init__(self):
        self.RHUs = []
    def Search(self):
        pass
    def Filter(self):
        pass
    def Allocate(self):
        pass
    def AddRHU(self,Rehabilitation_Housing_Unit):
        pass
    def MovePrisoner(self,Licensee,Rehabilitation_Housing_Unit):
        pass
    def GenerateReport(self):
        pass

class Location:
    def __init__(self,Name,SuitableForSexOffenders,x,y):
        self.Name = Name
        self.SuitableForSexOffenders = SuitableForSexOffenders
        self.x = x
        self.y = y
