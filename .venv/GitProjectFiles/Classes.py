import datetime
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

class Rehabilitation_Housing_Unit:
    def __init__(self,
                 HousingCategory,
                 NighttimeCurfew,
                 WeekendCurfew,
                 Location,
                 Licensees,
                 SuitableYoungOffenders,
                 MedicalServiceAccess,
                 TransportLinks,
                 CulturalReligeousServices,
                 MentalHealthSuitable,
                 Gender,
                 FamilyAccess,
                 Employment,
                 StayPeriod,
                 FutureExpansion1,
                 FutureExpansion2,
                 FutureExpansion3,
                 StudentSuggested1,
                 StudentSuggested2,
                 CostPerBed,
                 Capacity,
                 EmergencyCapacity,
                 ShortTermBeds,
                 Address,
                 Phone,
                 Email,
                 Contact,
                 ManagementGroup
                 ):
        self.HousingCategory = HousingCategory
        self.Location = Location
        self.StayPeriod = StayPeriod
        self.CostPerBed = CostPerBed
        self.Capacity = Capacity
        self.EmergencyCapacity = EmergencyCapacity
        self.ShortTermBeds = ShortTermBeds
        self.Address = Address
        self.Phone = Phone
        self.Email = Email
        self.Contact = Contact
        self.ManagementGroup = ManagementGroup
        self.Gender = Gender
        self.Licensees = Licensees
        self.SuitableYoungOffenders = SuitableForSexOffenders
        self.NighttimeCurfew = NighttimeCurfew
        self.WeekendCurfew = WeekendCurfew
        self.MedicalServiceAccess = MedicalServiceAccess
        self.TransportLinks = TransportLinks
        self.CulturalReligeousServices = CulturalReligeousServices
        self.MentalHealthSuitable = MentalHealthSuitable
        self.Employment = Employment
        self.FamilyAccess = FamilyAccess
        self.FutureExpansion1 = FutureExpansion1
        self.FutureExpansion2 = FutureExpansion2
        self.FutureExpansion3 = FutureExpansion3
        self.StudentSuggested1 = StudentSuggested1
        self.StudentSuggested2 = StudentSuggested2
        self.Notes = []

class Licensee:
    def __init__(self,Name,HomeAddress,Gender,RoleID,Disability,ReleaseDate,ExpectedLicenceEnd,CurrentLocation,Category):
        self.ReleaseStage = ReleaseStage # 0 - pending release, 1 - allocated to hostel, 2 - exited system
        self.Name = Name
        self.RoleID = RoleID
        self.HomeAddress = HomeAddress
        self.Gender = Gender
        self.ReleaseDate = ReleaseDate
        self.ExpectedLicenceEnd = ExpectedLicenceEnd
        self.Notes = []
        self.CurrentLocation = CurrentLocation
        self.Category = Category
        self.Disability = Disability
    def RegisterOffender(self):
        pass
    def set_state(self,state):
        pass
    def get_details(self):
        pass
    def set_conditions(self):
        pass


class Location:
    def __init__(self,Name,SuitableForSexOffenders,x,y):
        self.Name = Name
        self.SuitableForSexOffenders = SuitableForSexOffenders
        self.x = x
        self.y = y
