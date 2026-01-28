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
