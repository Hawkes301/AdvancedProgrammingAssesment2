class Licensee:
    def __init__(self,
                 Name,
                 RoleID,
                 Gender,
                 Category,
                 ReleaseDate,
                 ExpectedLicenseEnd,
                 HomeAddress,
                 DrugSearchRequired,
                 SchoolExcluded,
                 NightCurfew,
                 WeekendCurfew,
                 MentalHealthFlagged,
                 Disability,):
                 #CurrentLocation
        self.Name = Name
        self.RoleID = RoleID
        self.Gender = Gender
        self.Category = Category
        self.ReleaseDate = ReleaseDate
        self.ExpectedLicenseEnd = ExpectedLicenseEnd
        self.HomeAddress = HomeAddress
        self.DrugSearchRequired = DrugSearchRequired
        self.SchoolExcluded = SchoolExcluded
        self.NightCurfew = NightCurfew
        self.WeekendCurfew = WeekendCurfew
        self.MentalHealthFlagged = MentalHealthFlagged
        self.Disability = Disability
        self.CurrentRHU = []
        #self.CurrentLocation = CurrentLocation

    # Getters
    def get_Name(self):
        return self.Name

    def get_RoleID(self):
        return self.RoleID

    def get_Gender(self):
        return self.Gender

    def get_Category(self):
        return self.Category

    def get_ReleaseDate(self):
        return self.ReleaseDate

    def get_ExpectedLicenseEnd(self):
        return self.ExpectedLicenseEnd

    def get_HomeAddress(self):
        return self.HomeAddress

    def get_DrugSearchRequired(self):
        return self.DrugSearchRequired

    def get_SchoolExcluded(self):
        return self.SchoolExcluded

    def get_NightCurfew(self):
        return self.NightCurfew

    def get_WeekendCurfew(self):
        return self.WeekendCurfew

    def get_MentalHealthFlagged(self):
        return self.MentalHealthFlagged

    def get_Disability(self):
        return self.Disability

    def get_CurrentRHU(self):
        return self.CurrentRHU

    # Setters
    def set_Name(self, Name):
        self.Name = Name

    def set_RoleID(self, RoleID):
        self.RoleID = RoleID

    def set_Gender(self, Gender):
        self.Gender = Gender

    def set_Category(self, Category):
        self.Category = Category

    def set_ReleaseDate(self, ReleaseDate):
        self.ReleaseDate = ReleaseDate

    def set_ExpectedLicenseEnd(self, ExpectedLicenseEnd):
        self.ExpectedLicenseEnd = ExpectedLicenseEnd

    def set_HomeAddress(self, HomeAddress):
        self.HomeAddress = HomeAddress

    def set_DrugSearchRequired(self, DrugSearchRequired):
        self.DrugSearchRequired = DrugSearchRequired

    def set_SchoolExcluded(self, SchoolExcluded):
        self.SchoolExcluded = SchoolExcluded

    def set_NightCurfew(self, NightCurfew):
        self.NightCurfew = NightCurfew

    def set_WeekendCurfew(self, WeekendCurfew):
        self.WeekendCurfew = WeekendCurfew

    def set_MentalHealthFlagged(self, MentalHealthFlagged):
        self.MentalHealthFlagged = MentalHealthFlagged

    def set_Disability(self, Disability):
        self.Disability = Disability

    def set_CurrentRHU(self, CurrentRHU):
        self.CurrentRHU = CurrentRHU