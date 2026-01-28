import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *
# class Ui_LoginWindow(object):
#     def setupUi(self, LoginWindow,Password):
#         if not LoginWindow.objectName():
#             LoginWindow.setObjectName(u"LoginWindow")
#         LoginWindow.resize(640, 480)
#         self.centralwidget = QWidget(LoginWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.label = QLabel(self.centralwidget)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(210, 200, 49, 16))
#         #TextBox Logic
#         self.textEdit = QLineEdit(self.centralwidget)
#         self.textEdit.setObjectName(u"textEdit")
#         self.textEdit.setEnabled(True)
#         self.textEdit.setGeometry(QRect(270, 190, 256, 31))
#         self.Password = Password
#
#
#         self.label_2 = QLabel(self.centralwidget)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(290, 70, 49, 16))
#         LoginWindow.setCentralWidget(self.centralwidget)
#         self.menubar = QMenuBar(LoginWindow)
#         self.menubar.setObjectName(u"menubar")
#         self.menubar.setGeometry(QRect(0, 0, 640, 33))
#         LoginWindow.setMenuBar(self.menubar)
#         self.statusbar = QStatusBar(LoginWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         LoginWindow.setStatusBar(self.statusbar)
#
#         self.retranslateUi(LoginWindow)
#
#         QMetaObject.connectSlotsByName(LoginWindow)
#     # setupUi
#     def retranslateUi(self, LoginWindow):
#         LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
#         self.label.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
#         self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
#     # retranslateUi





class Ui_Dashboard(object):
    def setupUi(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(640, 480)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 631, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 0, 30, 50)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)

        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        Dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUi(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUi(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dashboard", u"Update Licencee Details", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Dashboard", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dashboard", u"Search For Licensee Suitable Accomodation", None))
        self.pushButton.setText(QCoreApplication.translate("Dashboard", u"Add Licensee", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dashboard", u"Search Licensees", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dashboard", u"Exit System", None))
    # retranslateUi

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setupUiLogin(self,"Password")
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
    def PasswordLogic(self):
        print(self.textEdit.text())
        if self.Password == str(self.textEdit.text()):
            self.setupUiDashboard(self)
        else:
            self.close()



    def retranslateUiLogin(self, LoginWindow):
        LoginWindow.setWindowTitle(QCoreApplication.translate("LoginWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("LoginWindow", u"Password:", None))
        self.label_2.setText(QCoreApplication.translate("LoginWindow", u"Login", None))
    # retranslateUi
    def setupUiDashboard(self, Dashboard):
        if not Dashboard.objectName():
            Dashboard.setObjectName(u"Dashboard")
        Dashboard.resize(640, 480)
        self.centralwidget = QWidget(Dashboard)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 0, 631, 421))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(30, 0, 30, 50)
        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 3, 0, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label.setWordWrap(False)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.gridLayout.addWidget(self.pushButton_4, 4, 0, 1, 1)

        self.pushButton = QPushButton(self.gridLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.gridLayout.addWidget(self.pushButton_5, 5, 0, 1, 1)

        Dashboard.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Dashboard)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 640, 33))
        Dashboard.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Dashboard)
        self.statusbar.setObjectName(u"statusbar")
        Dashboard.setStatusBar(self.statusbar)

        self.retranslateUiDashboard(Dashboard)

        QMetaObject.connectSlotsByName(Dashboard)
    # setupUi

    def retranslateUiDashboard(self, Dashboard):
        Dashboard.setWindowTitle(QCoreApplication.translate("Dashboard", u"MainWindow", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dashboard", u"Update Licencee Details", None))
        self.label.setText(QCoreApplication.translate("Dashboard", u"Dashboard", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dashboard", u"Search For Licensee Suitable Accomodation", None))
        self.pushButton.setText(QCoreApplication.translate("Dashboard", u"Add Licensee", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dashboard", u"Search Licensees", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dashboard", u"Exit System", None))
    # retranslateUi




app = QApplication(sys.argv)

window = MainWindow()

# UiWind = Ui_LoginWindow()
# UiWind.setupUi(window,"Password")

window.show()
app.exec()