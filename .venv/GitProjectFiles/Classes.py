import datetime
class Rehabilitation_Housing_Unit:
    def __init__(self,HousingCategory,NighttimeCurfew,WeekendCurfew,Location,Notes,Licensees,SuitableYoungOffenders,MedicalServiceAccess,TransportLinks,CulturalReligeousServices,MentalHealthSuitable,Gender,FamilyAccess,Employment,StayPeriod,FutureExpansion1,FutureExpansion2,FutureExpansion3,StudentSuggested1,StudentSuggested2,CostPerBed,Capacity,EmergencyCapacity,ShortTermBeds,Affress,Phone,Email,Contact,ManagementGroup):
        self.HousingCategory = chr
        self.Location = Location
        self.StayPeriod = int
        self.CostPerBed = float
        self.Capacity = int
        self.EmergencyCapacity = int
        self.ShortTermBeds = int
        self.Address = str
        self.Phone = str
        self.Email = str
        self.Contact = str
        self.ManagementGroup = str
        self.Gender = int
        self.Licensees = list(Licensee)
        self.SuitableYoungOffenders = bin
        self.NighttimeCurfew = bin
        self.WeekendCurfew = bin
        self.MedicalServiceAccess = bin
        self.TransportLinks = list(str)
        self.CulturalReligeousServices = list(bin)
        self.MentalHealthSuitable = list(bin)
        self.Employment = list(bin)
        self.FamilyAccess = bin
        self.FutureExpansion1
        self.FutureExpansion2
        self.FutureExpansion3
        self.StudentSuggested1
        self.StudentSuggested2
        self.Notes = list(str)

class Licensee:
    def __init__(self,Name,HomeAddress,Gender,RoleID,Disability,ReleaseDate,ExpectedLicenceEnd,Notes,CurrentLocation,Category):
        self.Name = str
        self.RoleID = str
        self.HomeAddress = str
        self.Gender = int
        self.ReleaseDate = date()
        self.ExpectedLicenceEnd = date()
        self.Notes = list(str)
        self.CurrentLocation = str
        self.Category = chr
        self.Disability = list(str)

class Location:
    def __init__(self,Name,SuitableForSexOffenders,x,y):
        self.Name = str
        self.SuitableForSexOffenders = bin
        self.x = float
        self.y = float
