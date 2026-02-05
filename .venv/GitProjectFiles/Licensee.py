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
        #self.CurrentLocation = CurrentLocation
    def RegisterOffender(self):
        pass
    def set_state(self,state):
        pass
    def get_details(self):
        pass
    def set_conditions(self):
        pass
