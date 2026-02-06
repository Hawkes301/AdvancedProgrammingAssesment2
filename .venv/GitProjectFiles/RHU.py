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

    # Getters
    def get_RHUID(self):
        return self.RHUID

    def get_HousingCategory(self):
        return self.HousingCategory

    def get_Location(self):
        return self.Location

    def get_StayPeriod(self):
        return self.StayPeriod

    def get_CostPerBed(self):
        return self.CostPerBed

    def get_Capacity(self):
        return self.Capacity

    def get_EmergencyCapacity(self):
        return self.EmergencyCapacity

    def get_ShortTermBeds(self):
        return self.ShortTermBeds

    def get_Address(self):
        return self.Address

    def get_Phone(self):
        return self.Phone

    def get_Email(self):
        return self.Email

    def get_Contact(self):
        return self.Contact

    def get_ManagementGroup(self):
        return self.ManagementGroup

    def get_Gender(self):
        return self.Gender

    def get_Licensees(self):
        return self.Licensees

    def get_SuitableForSexOffenders(self):
        return self.SuitableForSexOffenders

    def get_NighttimeCurfew(self):
        return self.NighttimeCurfew

    def get_WeekendCurfew(self):
        return self.WeekendCurfew

    def get_MedicalServiceAccess(self):
        return self.MedicalServiceAccess

    def get_TransportLinks(self):
        return self.TransportLinks

    def get_CulturalReligeousServices(self):
        return self.CulturalReligeousServices

    def get_MentalHealthSuitable(self):
        return self.MentalHealthSuitable

    def get_Employment(self):
        return self.Employment

    def get_FamilyAccess(self):
        return self.FamilyAccess

    def get_FutureExpansion1(self):
        return self.FutureExpansion1

    def get_FutureExpansion2(self):
        return self.FutureExpansion2

    def get_FutureExpansion3(self):
        return self.FutureExpansion3

    def get_StudentSuggested1(self):
        return self.StudentSuggested1

    def get_StudentSuggested2(self):
        return self.StudentSuggested2

    def get_Notes(self):
        return self.Notes

    # Setters
    def set_RHUID(self, RHUID):
        self.RHUID = RHUID

    def set_HousingCategory(self, HousingCategory):
        self.HousingCategory = HousingCategory

    def set_Location(self, Location):
        self.Location = Location

    def set_StayPeriod(self, StayPeriod):
        self.StayPeriod = StayPeriod

    def set_CostPerBed(self, CostPerBed):
        self.CostPerBed = CostPerBed

    def set_Capacity(self, Capacity):
        self.Capacity = Capacity

    def set_EmergencyCapacity(self, EmergencyCapacity):
        self.EmergencyCapacity = EmergencyCapacity

    def set_ShortTermBeds(self, ShortTermBeds):
        self.ShortTermBeds = ShortTermBeds

    def set_Address(self, Address):
        self.Address = Address

    def set_Phone(self, Phone):
        self.Phone = Phone

    def set_Email(self, Email):
        self.Email = Email

    def set_Contact(self, Contact):
        self.Contact = Contact

    def set_ManagementGroup(self, ManagementGroup):
        self.ManagementGroup = ManagementGroup

    def set_Gender(self, Gender):
        self.Gender = Gender

    def set_Licensees(self, Licensees):
        self.Licensees = Licensees

    def set_SuitableForSexOffenders(self, SuitableForSexOffenders):
        self.SuitableForSexOffenders = SuitableForSexOffenders

    def set_NighttimeCurfew(self, NighttimeCurfew):
        self.NighttimeCurfew = NighttimeCurfew

    def set_WeekendCurfew(self, WeekendCurfew):
        self.WeekendCurfew = WeekendCurfew

    def set_MedicalServiceAccess(self, MedicalServiceAccess):
        self.MedicalServiceAccess = MedicalServiceAccess

    def set_TransportLinks(self, TransportLinks):
        self.TransportLinks = TransportLinks

    def set_CulturalReligeousServices(self, CulturalReligeousServices):
        self.CulturalReligeousServices = CulturalReligeousServices

    def set_MentalHealthSuitable(self, MentalHealthSuitable):
        self.MentalHealthSuitable = MentalHealthSuitable

    def set_Employment(self, Employment):
        self.Employment = Employment

    def set_FamilyAccess(self, FamilyAccess):
        self.FamilyAccess = FamilyAccess

    def set_FutureExpansion1(self, FutureExpansion1):
        self.FutureExpansion1 = FutureExpansion1

    def set_FutureExpansion2(self, FutureExpansion2):
        self.FutureExpansion2 = FutureExpansion2

    def set_FutureExpansion3(self, FutureExpansion3):
        self.FutureExpansion3 = FutureExpansion3

    def set_StudentSuggested1(self, StudentSuggested1):
        self.StudentSuggested1 = StudentSuggested1

    def set_StudentSuggested2(self, StudentSuggested2):
        self.StudentSuggested2 = StudentSuggested2

    def set_Notes(self, Notes):
        self.Notes = Notes
