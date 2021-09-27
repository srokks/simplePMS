from PyQt5.QtSql import QSqlQuery,QSqlQueryModel

import db.Connection


class Room:
    id : int
    floor : int
    room_type_id : int
    room_no : str
    desc : str
    rooms_status_id : int
class Rooms(list):

    def __init__(self, db):
        super(Rooms, self).__init__()

        query = QSqlQuery(db=db)
        query.prepare(
            "SELECT * from tblRooms"
        )
        query.exec_()
        model = QSqlQueryModel()
        model.setQuery(query)
        for i in range(model.rowCount()):
            room = Room()
            room.id = model.index(i,0).data()
            room.floor = model.index(i,1).data()
            room.room_type_id =  model.index(i,2).data()
            room.room_no =  str(model.index(i,3).data())
            room.desc =  model.index(i,4).data()
            room.rooms_status_id =  model.index(i,5).data()
            self.append(room)

