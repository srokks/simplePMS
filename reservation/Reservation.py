from db.Connection import Connection
from PyQt5.QtCore import QDate
from PyQt5.QtSql import QSqlQuery, QSqlQueryModel


class Reservation:
    def __init__(self, booking_no=None):
        self.booking_no = booking_no
        self.guest_id = None
        self.date_from = None
        self.date_to = None
        self.room_no = None
        self.guest_no = None
        self.booking_status_id = None
        self.room_type = None
        self.nights = 0

    def fetch_by_id(self, db):
        model = QSqlQueryModel()
        query = QSqlQuery(db=db)
        query.prepare(
            "SELECT * from tblBookings WHERE bBookingNumber = :booking_no"
        )

        query.bindValue(':booking_no', self.booking_no)

        if query.exec_():
            model.setQuery(query)
            self.booking_no = model.index(0, 0).data()
            self.guest_id = model.index(0, 1).data()
            self.date_from = QDate(int(model.index(0, 2).data()[6:]),int(model.index(0, 2).data()[3:5]),int(model.index(0, 2).data()[0:2]))
            self.date_to = QDate(int(model.index(0, 3).data()[6:]),int(model.index(0, 3).data()[3:5]),int(model.index(0, 3).data()[0:2]))
            self.room_no =str( model.index(0, 4).data())
            self.guest_no = model.index(0, 5).data()
            self.booking_status_id = model.index(0, 6).data()
            self.room_type = model.index(0, 7).data()
        else:
            print('ERROR')
        return self

    def insert(self, db):
        querry = QSqlQuery(db=db)
        querry.prepare(
            "INSERT INTO "
            "tblBookings (bBookingNumber, bGuestID, bDateFrom, bDateTo, bRoomCount, bGuestCount, bBookingStatusID, bBookingChannelID)"
            "VALUES (:booking_no ,:guest_id ,:date_from,:date_to,:room_no,:guest_no,:booking_status_id,:room_type)"
        )
        self.booking_no = self._gen_res_no(db)
        querry.bindValue(":booking_no", self.booking_no)
        querry.bindValue(":guest_id", self.guest_id)
        querry.bindValue(":date_from", self.date_from)
        querry.bindValue(":date_to", self.date_to)
        querry.bindValue(":room_no", self.room_no)
        querry.bindValue(":guest_no", self.guest_no)
        querry.bindValue(":booking_status_id", self.booking_status_id)
        querry.bindValue(":room_type", self.room_type)
        if querry.exec_():
            return True
        else:
            print('error ', querry.lastError().text())
            print('querry: ', querry.lastQuery())
            return False, querry.lastError().text()

    def update(self, db):
        pass

    def _gen_res_no(self, db):
        'Generates res number by pattern: <yy><9999> - y -current year ex. 210002'
        import datetime
        _year = str(datetime.datetime.now().year)[2:]
        _last_res_number = str(self._get_last_res_no(db) + 1).zfill(4)
        # TODO: prevent from incrementing above 9999
        res_number = _year + _last_res_number
        return res_number

    def _get_last_res_no(self, db):
        model = QSqlQueryModel()
        querry = QSqlQuery(db=db)
        querry.prepare(
            "SELECT bBookingNumber FROM tblBookings ORDER BY bBookingNumber DESC LIMIT 1"
        )
        if querry.exec_():
            model.setQuery(querry)
            result = model.index(0, 0).data()
            result = int(result[2:])
            return result
        else:
            return None
    def is_valid(self):
        if  self.date_from is None or self.date_to:
            return False
        else:
            return True
if __name__ == '__main__':
    db = Connection().db
    res = Reservation('210002').fetch_by_id(db)
    resa = Reservation()
    print(resa.is_valid(),res.is_valid())
    print(res.booking_no)
