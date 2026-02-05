from faker import Faker
import random
from datetime import timedelta
import csv
from Licensee import Licensee

def save( name,  LicenseesToSave):
    with open( name , 'w') as file:
        for x in  range( len( LicenseesToSave)  ) :
            file.write(str(LicenseesToSave[x].__dict__) [1:-1])
            file.write('\n')


fake = Faker("en_GB")

def generateLicensees(licenseeCount=4000):
    licensees = []

    for _ in range(licenseeCount):
        licensee = Licensee(
            Name = fake.name(),
            RoleID = fake.unique.random_int(1000,9999),
            Gender = random.choice(["Male","Female"]),
            Category = random.choice(["A","B","C","D"]),
            ReleaseDate = str(fake.date_between(start_date="-1m",end_date="+6m")),
            ExpectedLicenseEnd = str((fake.date_between(start_date="-1m",end_date="+6m") + timedelta(days = random.choice([60,90,180,365])))),
            HomeAddress = fake.unique.address(),
            DrugSearchRequired = random.choice([True,False]),
            SchoolExcluded = random.choice([True, False]),
            NightCurfew=random.choice([True, False]),
            WeekendCurfew=random.choice([True, False]),
            MentalHealthFlagged=random.choice([True, False]),
            Disability=random.choice([True, False]),
        )
        licensees.append(licensee)
    return licensees
licenseeData = generateLicensees()
for x in range(len(licenseeData)):
    print(licenseeData[x].__dict__)

save("Licensees.csv",licenseeData)

