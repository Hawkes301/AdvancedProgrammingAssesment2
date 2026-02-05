class Rehabilitation_Housing_Unit:
    def __init__(self,
                 RHUID,
                 HousingCategory,
                 NighttimeCurfew,
                 WeekendCurfew,
                 Location,
                 SuitableForSexOffenders,
                 MedicalServiceAccess,
                 TransportLinks,
                 CulturalReligeousServices,
                 MentalHealthSuitable,
                 Gender,
                 FamilyAccess,
                 Employment,
                 StayPeriod,
                 CostPerBed,
                 Capacity,
                 EmergencyCapacity,
                 ShortTermBeds,
                 Address,
                 Phone,
                 Email,
                 Contact,
                 Notes
                 ):
        self.RHUID = RHUID
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
        self.ManagementGroup = []
        self.Gender = Gender
        self.Licensees = []
        self.SuitableForSexOffenders = SuitableForSexOffenders
        self.NighttimeCurfew = NighttimeCurfew
        self.WeekendCurfew = WeekendCurfew
        self.MedicalServiceAccess = MedicalServiceAccess
        self.TransportLinks = TransportLinks
        self.CulturalReligeousServices = CulturalReligeousServices
        self.MentalHealthSuitable = MentalHealthSuitable
        self.Employment = Employment
        self.FamilyAccess = FamilyAccess
        self.FutureExpansion1 = FutureExpansion1 = []
        self.FutureExpansion2 = FutureExpansion2 = []
        self.FutureExpansion3 = FutureExpansion3 = []
        self.StudentSuggested1 = StudentSuggested1 = []
        self.StudentSuggested2 = StudentSuggested2 = []
        self.Notes = []