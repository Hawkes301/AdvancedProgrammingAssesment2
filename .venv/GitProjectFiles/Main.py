#Reuben Hawkes
#W24014386
import csv
import sys
from turtledemo.penrose import start

from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
from faker import Faker
import random
from datetime import timedelta
from Allocation import OnLicenceHousingAllocationSystem, Location
from Licensee import Licensee
from RHU import Rehabilitation_Housing_Unit
from DataFaking import save
import re


class MatchResult:
    def __init__(self,rhu,score,conflicts,licensee):
        self.rhu = rhu
        self.score = score
        self.conflicts = conflicts
        self.licensee = licensee
class CustomDialog(QDialog):
    def __init__(self,conflicts):
        super().__init__()
        self.conflicts = conflicts
        self.setWindowTitle("Warning!")

        QBtn = (
            QDialogButtonBox.Ok | QDialogButtonBox.Cancel
        )

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()
        if conflicts:
            message = QLabel("Warning! Conflicts found")
            layout.addWidget(message)
        #display conflicts
        for x in conflicts:
            layout.addWidget(QLabel(x))

        message2 = QLabel("Would you Like to assign this housing?")

        layout.addWidget(message2)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.licensees = []
        self.rhus = []
        self.setupUiLogin(self,"Password")
        self.results = []
        self.currentLicensee = Licensee


    def setupUiLogin(self, LoginWindow,Password):
        if not LoginWindow.objectName():
            LoginWindow.setObjectName(u"LoginWindow")
        LoginWindow.resize(640, 480)
        self.centralwidget = QWidget(LoginWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(210, 200, 49, 16))
        #TextBox Logic
        self.textEdit = QLineEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(True)
        self.textEdit.setGeometry(QRect(270, 190, 256, 31))
        self.Password = Password
        self.textEdit.returnPressed.connect(self.PasswordLogic)


        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(290, 70, 49, 16))
        LoginWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(LoginWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        LoginWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(LoginWindow)
        self.statusbar.setObjectName(u"statusbar")
        LoginWindow.setStatusBar(self.statusbar)

        self.retranslateUiLogin(LoginWindow)

        QMetaObject.connectSlotsByName(LoginWindow)
        self.readData()
    def boolify(self,value):
        return str(value).strip().lower() == "true"
    def readData(self):
        #Read RHUS
        with open("RHUS.csv",newline = "") as file:
            reader = csv.DictReader(file)
            for row_number, row in enumerate(reader):
                rhu = Rehabilitation_Housing_Unit(
                    RHUID = row["RHUID"],
                    HousingCategory = row[" HousingCategory"],
                    Location = row[" Location"],
                    StayPeriod = int(row[" StayPeriod"]),
                    CostPerBed = float(row[" CostPerBed"]),
                    Capacity = int(row[" Capacity"]),
                    EmergencyCapacity= int(row[" EmergencyCapacity"]),
                    ShortTermBeds = int(row[" ShortTermBeds"]),
                    Address = row[" Address"],
                    Phone = row[" Phone"],
                    Email = row[" Email"],
                    Contact = row[" Contact"],
                    Gender = row[" Gender"],
                    SuitableForSexOffenders = self.boolify(row[" SuitableForSexOffenders"]),
                    NighttimeCurfew = self.boolify(row[" NighttimeCurfew"]),
                    WeekendCurfew = self.boolify(row[" WeekendCurfew"]),
                    MedicalServiceAccess = self.boolify(row[" MedicalServiceAccess"]),
                    TransportLinks = row[" TransportLinks"],
                    CulturalReligeousServices = row[" CulturalReligeousServices"],
                    MentalHealthSuitable = self.boolify(row[" MentalHealthSuitable"]),
                    Employment = self.boolify(row[" Employment"]),
                    FamilyAccess = self.boolify(row[" FamilyAccess"]),
                    Notes = row[" Notes"],


                )
                self.rhus.append(rhu)
        #Read Licensees
        with open("Licensees.csv",newline = "") as file:
            reader = csv.DictReader(file)
            for row_number, row in enumerate(reader):
                licensee = Licensee(
                    Name = row["Name"],
                    RoleID = row[" RoleID"],
                    Gender = row[" Gender"],
                    Category = row[" Category"],
                    ReleaseDate = row[" ReleaseDate"],
                    ExpectedLicenseEnd = row[" ExpectedLicenseEnd"],
                    HomeAddress = row[" HomeAddress"],
                    DrugSearchRequired = self.boolify(row[" DrugSearchRequired"]),
                    SchoolExcluded = self.boolify(row[" SchoolExcluded"]),
                    NightCurfew = self.boolify(row[" NightCurfew"]),
                    WeekendCurfew = self.boolify(row[" WeekendCurfew"]),
                    MentalHealthFlagged = self.boolify(row[" MentalHealthFlagged"]),
                    Disability = self.boolify(row[" Disability"]),

                )
                self.licensees.append(licensee)


    def setupUiAssign(self, AssignWindow):
            if not AssignWindow.objectName():
                AssignWindow.setObjectName(u"AssignWindow")
            AssignWindow.resize(800, 600)
            self.centralwidget = QWidget(AssignWindow)
            self.centralwidget.setObjectName(u"centralwidget")
            self.tableWidget = QTableWidget(self.centralwidget)
            if (self.tableWidget.columnCount() < 6):
                self.tableWidget.setColumnCount(6)
            __qtablewidgetitem = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
            __qtablewidgetitem1 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
            __qtablewidgetitem2 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
            __qtablewidgetitem3 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
            __qtablewidgetitem4 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
            __qtablewidgetitem5 = QTableWidgetItem()
            self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
            self.tableWidget.cellClicked.connect(self.on_cell_clicked2)
            self.tableWidget.setObjectName(u"tableWidget")
            self.tableWidget.setGeometry(QRect(10, 50, 771, 481))
            self.label = QLabel(self.centralwidget)
            self.label.setObjectName(u"label")
            self.label.setGeometry(QRect(30, 20, 101, 16))
            self.label_2 = QLabel(self.centralwidget)
            self.label_2.setObjectName(u"label_2")
            self.label_2.setGeometry(QRect(140, 20, 121, 16))
            self.pushButton = QPushButton(self.centralwidget)
            self.pushButton.setObjectName(u"pushButton")
            self.pushButton.setGeometry(QRect(280, 10, 171, 26))
            AssignWindow.setCentralWidget(self.centralwidget)
            self.menubar = QMenuBar(AssignWindow)
            self.menubar.setObjectName(u"menubar")
            self.menubar.setGeometry(QRect(0, 0, 800, 33))
            AssignWindow.setMenuBar(self.menubar)
            self.statusbar = QStatusBar(AssignWindow)
            self.statusbar.setObjectName(u"statusbar")
            AssignWindow.setStatusBar(self.statusbar)


            self.retranslateUiAssign(AssignWindow)

            QMetaObject.connectSlotsByName(AssignWindow)
            self.results = self.populateRowsAssign(self.FindHome(),self.tableWidget)

            # Assign Housing button
            self.pushButton.setCheckable(True)
            self.pushButton.clicked.connect(self.AssignButtonPressed)


    def AssignButtonPressed(self):
        rhu = self.results[(self.tableWidget.currentRow())]
        if not rhu.conflicts:
            print("no conflicts")
        else:
            for x in rhu.conflicts:
                print(x)
        dlg = CustomDialog(rhu.conflicts)
        if dlg.exec():
            print("Success! Housing assigned!")
            self.currentLicensee.set_CurrentRHU(rhu.rhu.get_RHUID())
            save("Licensees.csv", self.licensees, ['Name',
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
                 'CurrentRHU'])
            print(self.currentLicensee.get_CurrentRHU())
            # HOUSING ASSIGNED!
        else:
            print("Canceled")
    def retranslateUiAssign(self, AssignWindow):
            AssignWindow.setWindowTitle(QCoreApplication.translate("AssignWindow", u"MainWindow", None))
            ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
            ___qtablewidgetitem.setText(QCoreApplication.translate("AssignWindow", u"RHUID", None));
            ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
            ___qtablewidgetitem1.setText(QCoreApplication.translate("AssignWindow", u"HousingCategory", None));
            ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
            ___qtablewidgetitem2.setText(QCoreApplication.translate("AssignWindow", u"SuitableForSexOffendors", None));
            ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
            ___qtablewidgetitem3.setText(QCoreApplication.translate("AssignWindow", u"Gender", None));
            ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
            ___qtablewidgetitem4.setText(QCoreApplication.translate("AssignWindow", u"CostPerBed", None));
            ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
            ___qtablewidgetitem5.setText(QCoreApplication.translate("AssignWindow", u"Address", None));
            self.label.setText(QCoreApplication.translate("AssignWindow", u"RHUID", None))
            self.label_2.setText(QCoreApplication.translate("AssignWindow", u"RoleID", None))
            self.pushButton.setText(QCoreApplication.translate("AssignWindow", u"Assign Selected House", None))

    def populateRowsAssign(self,results,table):
        for row in range(len(results)):
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition,0,QTableWidgetItem(results[row].rhu.get_RHUID()))
            table.setItem(rowPosition, 1, QTableWidgetItem(results[row].rhu.get_HousingCategory()))
            table.setItem(rowPosition, 2, QTableWidgetItem(str(results[row].rhu.get_SuitableForSexOffenders())))
            table.setItem(rowPosition, 3, QTableWidgetItem(results[row].rhu.get_Gender()))
            table.setItem(rowPosition, 4, QTableWidgetItem(str(results[row].rhu.get_CostPerBed())))
            table.setItem(rowPosition, 5, QTableWidgetItem(results[row].rhu.get_Address()))
        return results



    def retranslateUiLogin(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Login", None))

    def PasswordLogic(self):
        print(self.textEdit.text())
        if self.Password == str(self.textEdit.text()):
            self.setupUiLicensees(self)
        else:
            self.close()
    def setupUiLicensees(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QSize(640, 480))
        MainWindow.setBaseSize(QSize(1000, 900))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tableWidget = QTableWidget(self.centralwidget)
        if (self.tableWidget.columnCount() < 13):
            self.tableWidget.setColumnCount(13)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(11, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(12, __qtablewidgetitem12)

        self.tableWidget.cellClicked.connect(self.on_cell_clicked1)

        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(-5, 71, 801, 471))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"FindHome")
        self.pushButton.setGeometry(QRect(520, 30, 81, 26))

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 30, 161, 20))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 30, 131, 16))

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        #Find home button
        self.pushButton.setCheckable(True)
        self.pushButton.clicked.connect(self.FindButtonPressed)

        self.retranslateUiLicensees(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
        self.populateRowsLicense(self.tableWidget)
    def FindButtonPressed(self):
        self.setupUiAssign(self)

    def FindHome(self):

        licensee = self.currentLicensee


        self.label_2.setText(f"RoleID {licensee.get_RoleID()}")
        results = []
        for rhu in self.rhus:
            score = 0
            conflicts = []

            if rhu.get_Gender() == "Mixed" or rhu.get_Gender() == licensee.get_Gender():
                score += 2
            else:
                score -= 1
                conflicts.append("Uncompattible Gender")



            if licensee.SchoolExcluded and not(rhu.get_SuitableForSexOffenders()):
                score -= 2
                conflicts.append("Near a school")


            if licensee.get_NightCurfew():
                if rhu.get_NighttimeCurfew():
                    score += 1
                else:
                    score -= 1
                    conflicts.append("Nighttime curfew not supported")

            if licensee.get_WeekendCurfew():
                if rhu.get_WeekendCurfew():
                    score += 1
                else:
                    score -= 1
                    conflicts.append("Weekend curfew not supported")


            if licensee.get_MentalHealthFlagged():
                if rhu.get_MentalHealthSuitable():
                    score += 1
                else:
                    score -= 1
                    conflicts.append("Mental health needs not supported")

            # Cost awareness (cheaper RHUs score higher)
            if rhu.get_CostPerBed() < 80:
                score += 1

            results.append(MatchResult(rhu, score, conflicts,licensee))



        results.sort(key=lambda result: result.score, reverse=True)

        return results

    def on_cell_clicked1(self, row, column):
        self.label.setText(f"{self.tableWidget.item(row,1).text()}")
        self.label_2.setText(f"RoleID {self.tableWidget.item(row,0).text()}")
        self.currentLicensee = self.licensees[(self.tableWidget.currentRow())]
    def on_cell_clicked2(self,row,column):
        self.label.setText(f"RHUID {self.tableWidget.item(row,0).text()}")
    def populateRowsLicense(self,table):
        for row in range(len(self.licensees)):
            rowPosition = table.rowCount()
            table.insertRow(rowPosition)
            table.setItem(rowPosition,0,QTableWidgetItem(self.licensees[row].get_RoleID()))
            table.setItem(rowPosition, 1, QTableWidgetItem(self.licensees[row].get_Name()))
            table.setItem(rowPosition, 2, QTableWidgetItem(self.licensees[row].get_HomeAddress()))
            table.setItem(rowPosition, 3, QTableWidgetItem(self.licensees[row].get_Gender()))
            table.setItem(rowPosition, 4, QTableWidgetItem(self.licensees[row].get_ReleaseDate()))
            table.setItem(rowPosition, 5, QTableWidgetItem(self.licensees[row].get_Category()))
            table.setItem(rowPosition, 6, QTableWidgetItem(str(self.licensees[row].get_SchoolExcluded())))
            table.setItem(rowPosition, 7, QTableWidgetItem(str(self.licensees[row].get_MentalHealthFlagged())))
            table.setItem(rowPosition, 8, QTableWidgetItem(self.licensees[row].get_ExpectedLicenseEnd()))
            table.setItem(rowPosition, 9, QTableWidgetItem(str(self.licensees[row].get_DrugSearchRequired())))
            table.setItem(rowPosition, 10, QTableWidgetItem(str(self.licensees[row].get_NightCurfew())))
            table.setItem(rowPosition, 11, QTableWidgetItem(str(self.licensees[row].get_WeekendCurfew())))
            table.setItem(rowPosition, 12, QTableWidgetItem(str(self.licensees[row].get_Disability())))

    def retranslateUiLicensees(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"RoleID", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gender", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ReleaseDate", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Category", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"SchoolExcluded", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"MentalHealthFlagged", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"ExpectedLicenseEnd", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"DrugSearchRequired", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"NightCurfew", None));
        ___qtablewidgetitem11 = self.tableWidget.horizontalHeaderItem(11)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"WeekendCurfew", None));
        ___qtablewidgetitem12 = self.tableWidget.horizontalHeaderItem(12)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Disability", None));
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Find Home", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"RoleID", None))

#Window Logic
app = QApplication(sys.argv)

window = MainWindow()


window.show()
app.exec()
