import datetime
class Rehabilitation_Housing_Unit:
    def __init__(self,HousingCategory,NighttimeCurfew,WeekendCurfew,Location,Licensees,SuitableYoungOffenders,MedicalServiceAccess,TransportLinks,CulturalReligeousServices,MentalHealthSuitable,Gender,FamilyAccess,Employment,StayPeriod,FutureExpansion1,FutureExpansion2,FutureExpansion3,StudentSuggested1,StudentSuggested2,CostPerBed,Capacity,EmergencyCapacity,ShortTermBeds,Affress,Phone,Email,Contact,ManagementGroup):
        self.HousingCategory
        self.Location = Location
        self.StayPeriod
        self.CostPerBed
        self.Capacity
        self.EmergencyCapacity
        self.ShortTermBeds
        self.Address
        self.Phone
        self.Email
        self.Contact
        self.ManagementGroup
        self.Gender
        self.Licensees
        self.SuitableYoungOffenders
        self.NighttimeCurfew
        self.WeekendCurfew
        self.MedicalServiceAccess
        self.TransportLinks
        self.CulturalReligeousServices
        self.MentalHealthSuitable
        self.Employment
        self.FamilyAccess
        self.FutureExpansion1
        self.FutureExpansion2
        self.FutureExpansion3
        self.StudentSuggested1
        self.StudentSuggested2

class Licensee:
    def __init__(self,Name,HomeAddress,Gender,RoleID,ReleaseDate,ExpectedLicenceEnd,Notes,CurrentLocation,Category):
        self.Name = str
        self.RoleID = str
        self.HomeAddress = str
        self.Gender = str
        self.ReleaseDate = date()
        self.ExpectedLicenceEnd = date()
        self.Notes = list(str)
        self.CurrentLocation = str
        self.Category = chr
class Location:
    def __init__(self,Name,SuitableForSexOffenders):
        self.Name = str
        self.SuitableForSexOffenders = bin
    pass