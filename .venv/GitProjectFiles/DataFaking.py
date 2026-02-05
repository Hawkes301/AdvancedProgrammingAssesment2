from faker import Faker
import random
from datetime import timedelta
import csv
from Licensee import Licensee
from RHU import Rehabilitation_Housing_Unit

def save( name,  LicenseesToSave):
    with open( name , 'w') as file:
        for x in  range( len( LicenseesToSave)  ) :
            file.write(str(LicenseesToSave[x].__dict__) [1:-1])
            file.write('\n')


fake = Faker("en_GB")

def generateLicensees(licenseeCount=4000):
    licensees = []
    ReleaseDate = str(fake.date_between(start_date="-1m",end_date="+6m"))
    ExpectedLicenseEnd = str((ReleaseDate + str(timedelta(days=random.choice([60, 90, 180, 365])))))
    for _ in range(licenseeCount):
        licensee = Licensee(
            Name = fake.name(),
            RoleID = fake.unique.random_int(1000,9999),
            Gender = random.choice(["Male","Female"]),
            Category = random.choice(["A","B","C","D"]),
            ReleaseDate = ReleaseDate,
            ExpectedLicenseEnd = ExpectedLicenseEnd,
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

def generateRHUs(rhuCount=200):
    rhus = []
    Capacity = random.randint(10, 200)
    for X in range(rhuCount):
        rhu = Rehabilitation_Housing_Unit(
            RHUID = X,
            HousingCategory = random.choice(["A","B","C","D"]),
            NighttimeCurfew = random.choice([True,False]),
            WeekendCurfew = random.choice([True,False]),
            Location = ((random.randint(0,10000),random.randint(0,10000))),
            SuitableForSexOffenders = random.choice([True,False]),
            MedicalServiceAccess = random.choice([True,False]),
            TransportLinks = random.choice(["None","Rail","Bus","Rail + Bus"]),
            CulturalReligeousServices = random.choice(["None","Chapel","Prayer room","Chapel + Prayer room"]),
            MentalHealthSuitable = random.choice([True,False]),
            Gender = random.choice(["Male","Female","Mixed"]),
            FamilyAccess = random.choice([True,False]),
            Employment = random.choice([True,False]),
            StayPeriod = random.choice([60,90,180,365]),
            CostPerBed = (f"£{random.randint(10,100)}.{random.randint(00,99)}"),
            Capacity = Capacity,
            EmergencyCapacity = (Capacity + random.randint(10,50)),
            ShortTermBeds = random.randint(1,10),
            Address = fake.unique.address(),
            Phone = fake.unique.random_int(1000000,9999999),
            Email = f"RHU{X}@email.com",
            Contact = fake.unique.name(),
        )
        rhus.append(rhu)
    return rhus

licenseeData = generateLicensees()
for x in range(len(licenseeData)):
    print(licenseeData[x].__dict__)

save("Licensees.csv",licenseeData)

rhuData = generateRHUs()
for x in range(len(rhuData)):
    print((rhuData[x].__dict__))

save("RHUS.csv",rhuData)

