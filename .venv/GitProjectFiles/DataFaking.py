#Reuben Hawkes
#W24014386
from faker import Faker
import random
from datetime import timedelta
import csv
from Licensee import Licensee
from RHU import Rehabilitation_Housing_Unit

def save( name,  LicenseesToSave,Headers):
    with open( name , 'w') as file:
        for x in range(len(Headers)):
            file.write(str(Headers[x]))
            file.write(", ")
        file.write('\n')
        for x in  range( len( LicenseesToSave)  ) :
            for key, value in (LicenseesToSave[x].__dict__).items():
                #line = line.strip().replace('\n', '')
                file.write(str(value).strip().replace('\n', ''))
                file.write(", ")
            #file.write(str(LicenseesToSave[x].__dict__))
            file.write('\n')


fake = Faker("en_GB")

def generateLicensees(licenseeCount=4000):
    licensees = []

    for _ in range(licenseeCount):
        ReleaseDate = fake.date_between(start_date="-1m", end_date="+6m")
        ExpectedLicenseEnd = str((ReleaseDate + timedelta(days=random.choice([60, 90, 180, 365]))))
        licensee = Licensee(
            Name = fake.name(),
            RoleID = fake.unique.random_int(1000,9999),
            Gender = random.choice(["Male","Female"]),
            Category = random.choice(["A","B","C","D"]),
            ReleaseDate = str(ReleaseDate),
            ExpectedLicenseEnd = str(ExpectedLicenseEnd),
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
            Location = (f"X{random.randint(0,10000)}Y{random.randint(0,10000)}"),
            SuitableForSexOffenders = random.choice([True,False]),
            MedicalServiceAccess = random.choice([True,False]),
            TransportLinks = random.choice(["None","Rail","Bus","Rail + Bus"]),
            CulturalReligeousServices = random.choice(["None","Chapel","Prayer room","Chapel + Prayer room"]),
            MentalHealthSuitable = random.choice([True,False]),
            Gender = random.choice(["Male","Female","Mixed"]),
            FamilyAccess = random.choice([True,False]),
            Employment = random.choice([True,False]),
            StayPeriod = random.choice([60,90,180,365]),
            CostPerBed = (f"{random.randint(10,100)}.{random.randint(00,99)}"),
            Capacity = Capacity,
            EmergencyCapacity = (Capacity + random.randint(10,50)),
            ShortTermBeds = random.randint(1,10),
            Address = fake.unique.address(),
            Phone = fake.unique.random_int(1000000,9999999),
            Email = f"RHU{X}@email.com",
            Contact = fake.unique.name(),
            Notes = [],
        )
        rhus.append(rhu)
    return rhus

licenseeData = generateLicensees()
for x in range(len(licenseeData)):
    print(licenseeData[x].__dict__)

licenseeHeaders = ['Name',
                 'RoleID',
                 'Gender',
                 'Category',
                 'ReleaseDate',
                 'ExpectedLicenseEnd',
                 'HomeAddress',
                 'DrugSearchRequired',
                 'SchoolExcluded',
                 'NightCurfew',
                 'WeekendCurfew',
                 'MentalHealthFlagged',
                 'Disability',
                 'CurrentRHU']

save("Licensees.csv",licenseeData,licenseeHeaders)

rhuData = generateRHUs()
for x in range(len(rhuData)):
    print((vars(rhuData[x])))

rhuHeaders = ['RHUID', 'HousingCategory', 'Location', 'StayPeriod', 'CostPerBed',
               'Capacity', 'EmergencyCapacity', 'ShortTermBeds', 'Address', 'Phone', 'Email',
               'Contact', 'ManagementGroup', 'Gender', 'Licensees', 'SuitableForSexOffenders', 'NighttimeCurfew', 'WeekendCurfew',
               'MedicalServiceAccess', 'TransportLinks',
                'CulturalReligeousServices',
                'MentalHealthSuitable', 'Employment',
                'FamilyAccess', 'FutureExpansion1', 'FutureExpansion2', 'FutureExpansion3', 'StudentSuggested1', 'StudentSuggested2','Notes']
save("RHUS.csv",rhuData,rhuHeaders)

