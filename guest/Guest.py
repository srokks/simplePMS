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
    def fetch_by_id(self,id):
        db = Connection().db
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



