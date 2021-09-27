from  db.Connection import Connection
from PyQt5.QtSql import QSqlQuery,QSqlQueryModel
class Address:
    def __init__(self):
        self.address_id = None
        self.address = None
        self.address2 = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.country = None
    def insert_address(self,db):
        print('***insertin address***')
        querry = QSqlQuery(db=db)
        querry.prepare(
            "INSERT INTO tblAddresses(aAddress,aAddress2,aCity,aState,aZipCode,aCountry) "
            "VALUES (:address,:address2,:city,:state,:zip_code,:country)"

        )
        querry.bindValue(":address", self.address)
        querry.bindValue(":address2",self.address2)
        querry.bindValue(":city", self.city)
        querry.bindValue(":state", self.state)
        querry.bindValue(":zip_code", self.zip_code)
        querry.bindValue(":country", self.country)

        if querry.exec_():
            self.address_id = querry.lastInsertId()
            return True
        else:
            print('error ', querry.lastError().text())
            return False, querry.lastError().text()
class Guest(Address):
    def __init__(self):
        Address()
        self.guest_id = None
        self.type = None
        self.gender = None
        self.first_name = None
        self.last_name = None
        self.phone_number = None
        self.mail_address = None
        self.address_id = None
        self.id_number = None
        self.family_members = None
    def fetch_by_id(self,db,id):
        model = QSqlQueryModel()

        query = QSqlQuery(db=db)
        query.prepare(
            "SELECT * FROM tblGuest "
            "INNER JOIN tblAddresses ON tblGuest.gAddressID = tblAddresses.aAddressID "
            "WHERE "
            "gGuestID = :guest_id "


        )
        query.bindValue(':guest_id',id)
        query.exec_()
        model.setQuery(query)

        self.guest_id = model.index(0,0).data()
        self.type = model.index(0,1).data()
        self.gender = model.index(0,2).data()
        self.first_name = model.index(0,3).data()
        self.last_name = model.index(0,4).data()
        self.phone_number = model.index(0,5).data()
        self.mail_address = model.index(0,6).data()
        self.mail_address = model.index(0,6).data()
        self.id_number = model.index(0,7).data()
        self.family_members = model.index(0,8).data()
        self.address_id = model.index(0,10).data()
        self.address = model.index(0,11).data()
        self.address2 = model.index(0,12).data()
        self.city = model.index(0,13).data()
        self.state = model.index(0,14).data()
        self.zip_code = model.index(0,15).data()
        self.country = model.index(0,16).data()



    def insert_guest(self,db):

        if self.insert_address(db):
            pass
        else:
            print("*ERROR*")

        print('*inserting guest_id_signal**')
        querry = QSqlQuery(db=db)
        querry.prepare(
            "INSERT INTO "
            "tblGuest(gGuestType,gGender,gFirstName,gLastName,gPhoneNumber,gMailAddress,gIDNumber,gAddressID) "
            "VALUES (:guest_type,:gender,:first_name,:last_name,:phone_number,:mail_address,:id_number,:address_id)"

        )
        querry.bindValue(":guest_type", self.type)
        querry.bindValue(':gender', self.gender)
        querry.bindValue(':first_name', self.first_name)
        querry.bindValue(':last_name', self.last_name)
        querry.bindValue(':phone_number', self.phone_number)
        querry.bindValue(':mail_address', self.mail_address)
        querry.bindValue(':id_number', self.id_number)
        querry.bindValue(':address_id', self.address_id)

        if querry.exec_():
            self.guest_id = querry.lastInsertId()
            return True
        else:
            print('error ', querry.lastError().text())
            return False, querry.lastError().text()

    def get_address_id_by_guest_id(self,db,guest_id:int):
        'returns address_id from db based on guest_id'
        model = QSqlQueryModel()
        query = QSqlQuery(db=db)
        query.prepare(
            "SELECT gAddressID FROM tblGuest "
            "WHERE "
            "gGuestID = :guest_id "

        )
        query.bindValue(':guest_id', guest_id)
        query.exec_()
        model.setQuery(query)
        return model.index(0,0).data()
    def update_guest(self,db):

        querry = QSqlQuery(db=db)
        querry.prepare(
            "UPDATE tblGuest "
            "SET "
            "gGuestType= :guest_type,"
            "gGender = :gender,"
            "gFirstName = :first_name,"
            "gLastName = :last_name,"
            "gPhoneNumber = :phone_number,"
            "gMailAddress = :mail_address,"
            "gIDNumber = :id_number "
            "WHERE gGuestID = :guest_id"

        )
        querry.bindValue(":guest_type", str(self.type))
        querry.bindValue(':gender', self.gender)
        querry.bindValue(':first_name', self.first_name)
        querry.bindValue(':last_name', self.last_name)
        querry.bindValue(':phone_number', self.phone_number)
        querry.bindValue(':mail_address', self.mail_address)
        querry.bindValue(':id_number', self.id_number)

        querry.bindValue(':guest_id', str(self.guest_id))

        if self.update_address(db) and querry.exec_():
            return True
        else:
            print('error ', querry.lastError().text())
            return False, querry.lastError().text()

    def update_address(self,db):
        self.address_id = self.get_address_id_by_guest_id(db,self.guest_id)
        querry = QSqlQuery(db=db)
        querry.prepare(
            "UPDATE tblAddresses "
            "SET "
            "aAddress = :address,"
            "aAddress2 = :address2,"
            "aCity = :city,"
            "aState = :state,"
            "aZipCode = :zip_code,"
            "aCountry = :country "
            "WHERE aAddressID = :address_id"

        )
        querry.bindValue(":address", self.address)
        querry.bindValue(":address2", self.address2)
        querry.bindValue(":city", self.city)
        querry.bindValue(":state", self.state)
        querry.bindValue(":zip_code", self.zip_code)
        querry.bindValue(":country", self.country)
        querry.bindValue(":address_id", str(self.address_id))


        if querry.exec_():
            return True
        else:
            print('error ', querry.lastError().text())
            return False, querry.lastError().text()


