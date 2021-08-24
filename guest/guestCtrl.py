import sqlite3

class GuestCtrl:
    __database_name = r'test_db.db'


    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.tbl_name = 'tblGuest'
        self.tbl_pattern = [
            "gGuestID",
            "gFirstName",
            "gLastName",
            "gAddress",
            "gAddress2",
            "gCity",
            "gState",
            "gZipCode",
            "gCountry",
            "gPhoneNumber",
            "gMailAddress",
            "gGender",
        ]

    def create_table(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS 'tblGuest' ("
            "'gGuestID'	INTEGER NOT NULL UNIQUE,"
            "'gFirstName'	TEXT,"
            "'gLastName'	BLOB,"
            "'gAddress'	TEXT,"
            "'gAddress2'	TEXT,"
            "'gCity'	TEXT,"
            "'gState'	TEXT,"
            "'gZipCode'	TEXT,"
            "'gCountry'	TEXT,"
            "'gPhoneNumber'	TEXT,"
            "'gMailAddress'	TEXT,"
            "'gGender'	TEXT,"
            "PRIMARY KEY('gGuestID' AUTOINCREMENT))"
        )
        try:
            self.cur.execute(sql)
            return True
        except sqlite3.Error as Err:
            print(Err)

    def addGuest(self, gFirstName,gLastName,gAddress,gAddress2,gCity,gState,gZipCode,gCountry,gPhoneNumber,gMailAddress,gGender):
        #gGuestID,gFirstName,gLastName,gAddress,gAddress2,gCity,gState,gZipCode,gCountry,gPhoneNumber,gMailAddress,gGender
        sql =(
            f"INSERT INTO {self.tbl_name} (gFirstName,gLastName,gAddress,gAddress2,gCity,gState,gZipCode,gCountry,gPhoneNumber,gMailAddress,gGender) "
            f"VALUES ('{gFirstName}','{gLastName}','{gAddress}','{gAddress2}','{gCity}','{gState}','{gZipCode}','{gCountry}','{gPhoneNumber}','{gMailAddress}','{gGender}')"
        )
        print(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.Error as Err:
            print(Err)

    def getGuestBySurName(self,name = '',fetch_limit=15):
        self.name = name
        sql = f"SELECT * FROM {self.tbl_name} where {self.tbl_pattern[2]} like '{self.name}%' "
        print(sql)
        try:
            self.cur.execute(sql)
            rows = self.cur.fetchmany(size=fetch_limit)
            for pos, el in enumerate(rows):
                rows[pos] = dict(zip(self.tbl_pattern, el))
            return rows
        except sqlite3.Error as Err:
            print(Err)

    def getGuestByID(self, g_id):
        try:
            sql = f"SELECT * FROM {self.tbl_name} where {self.tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            return dict(zip(self.tbl_pattern, self.cur.fetchone()))
        except sqlite3.Error as Err:
            print(Err)
            return False
    def updatebyID(self,guest):
        sql=(
            f"UPDATE {self.tbl_name} SET "
            # f"{self.tbl_pattern[1]}='{guest[self.tbl_pattern[1]]}'"
             )
        for i in range(1,len(self.tbl_pattern)):
            sql+= f"{self.tbl_pattern[i]}='{guest[self.tbl_pattern[i]]}',"
        sql = sql[0:-1]
        sql+= f" WHERE {self.tbl_pattern[0]}={guest[self.tbl_pattern[0]]}"
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.Error as Err:
            print(Err)

