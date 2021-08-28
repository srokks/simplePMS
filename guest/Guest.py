import sqlite3


class GuestCtrl:
    '''
    Guest class controller for operations on database
    '''
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.tbl_name = 'tblGuest'

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
            "'gGuestType'	INTEGER,"
            "'gIDNumber'	TEXT,"
            "PRIMARY KEY('gGuestID' AUTOINCREMENT))"
        )
        try:
            self.cur.execute(sql)
            return True
        except sqlite3.Error as Err:
            print(Err)

    def addGuest(self, guest):
        sql = (
            f"INSERT INTO {self.tbl_name} ({','.join(Guest().tbl_pattern[1:])}) "
            f"VALUES ('{guest.gFirstName}','{guest.gLastName}','{guest.gAddress}','{guest.gAddress2}','{guest.gCity}','{guest.gState}','{guest.gZipCode}','{guest.gCountry}','{guest.gPhoneNumber}','{guest.gMailAddress}','{guest.gGender}','{guest.gGuestType}','{guest.gIdNumber}')"
        )
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.Error as Err:
            print('ERROR OCCURED:',Err)

    def getGuestBySurName(self, name='', fetch_limit=15):
        self.name = name
        sql = f"SELECT * FROM {self.tbl_name} where {Guest().tbl_pattern[2]} like '{self.name}%' "

        try:
            self.cur.execute(sql)
            rows = self.cur.fetchmany(size=fetch_limit)
            for pos, el in enumerate(rows):
                rows[pos] = Guest(gGuestList=el)
            return rows
        except sqlite3.Error as Err:
            print(Err)

    def getGuestByID(self, g_id):
        try:
            #FixMe: does not check max id in tableś
            sql = f"SELECT * FROM {self.tbl_name} where {Guest().tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            guest_list = self.cur.fetchone()
            return Guest(gGuestList=guest_list)

        except sqlite3.Error as Err:
            print(Err)
            return False

    def updateGuestObj(self, guest):
        sql = (
            f"UPDATE {self.tbl_name} SET "
        )
        for pos,el in enumerate(guest.tbl_pattern[1:]):
            sql+=el+"='"+str(guest(pos+1))+"',"
        sql=sql[:-1]
        sql+= " WHERE "+guest.tbl_pattern[0]+"="+str(guest(0))+";"
        # print(sql)
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except sqlite3.Error as Err:
            print('***ERROR OCCURED***\n',Err)

    def getGuestByColName(self,col_name,key_word):
        pass
class Guest:
    # gGuestID,gFirstName,gLastName,gAddress,gAddress2,gCity,gState,gZipCode,gCountry,gPhoneNumber,gMailAddress,gGender
    def __init__(self,**kwargs):
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
        'gGuestType',
        'gIdNumber'
    ]
        if 'gGuestList' in kwargs.keys():
            self.gGuestList = kwargs['gGuestList']
            if len(self.gGuestList)!=14:
                #TODO: wyrzucić jakiś błąd
                print('lipa')
            else:
                self.gGuestID = self.gGuestList[0]
                self.gFirstName = self.gGuestList[1]
                self.gLastName = self.gGuestList[2]
                self.gAddress = self.gGuestList[3]
                self.gAddress2 = self.gGuestList[4]
                self.gCity = self.gGuestList[5]
                self.gState = self.gGuestList[6]
                self.gZipCode = self.gGuestList[7]
                self.gCountry = self.gGuestList[8]
                self.gPhoneNumber = self.gGuestList[9]
                self.gMailAddress = self.gGuestList[10]
                self.gGender = self.gGuestList[11]
                self.gGuestType = self.gGuestList[12]
                self.gIdNumber = self.gGuestList[13]

        else:
            self.gGuestID = kwargs['gguestID'] if 'gguestID' in kwargs.keys() else None
            self.gFirstName = kwargs['gFirstName'] if 'gFirstName' in kwargs.keys() else None
            self.gLastName = kwargs['gLastName'] if 'gLastName' in kwargs.keys() else None
            self.gAddress = kwargs['gAddress'] if 'gAddress' in kwargs.keys() else None
            self.gAddress2 = kwargs['gAddress2'] if 'gAddress2' in kwargs.keys() else None
            self.gCity = kwargs['gCity'] if 'gCity' in kwargs.keys() else None
            self.gState = kwargs['gState'] if 'gState' in kwargs.keys() else None
            self.gZipCode = kwargs['gZipCode'] if 'gZipCode' in kwargs.keys() else None
            self.gCountry = kwargs['gCountry'] if 'gCountry' in kwargs.keys() else None
            self.gPhoneNumber = kwargs['gPhoneNumber'] if 'gPhoneNumber' in kwargs.keys() else None
            self.gMailAddress = kwargs['gMailAddress'] if 'gMailAddress' in kwargs.keys() else None
            self.gGender = kwargs['gGender'] if 'ggender' in kwargs.keys() else None
            self.gGuestType = kwargs['gGuestType'] if 'gGuestType' in kwargs.keys() else None
            self.gIdNumber = kwargs['gIDNumber'] if 'gIDNumber' in kwargs.keys() else None


    def __call__(self, *args, **kwargs):
        if not args:
            print(self.gGuestID, self.gFirstName, self.gLastName, self.gAddress, self.gAddress2, self.gCity, self.gState, self.gZipCode, self.gCountry, self.gPhoneNumber, self.gMailAddress, self.gGender, self.gGuestType, self.gIdNumber, sep="|")
        if len(args)==1:
            querry = 'self.'+self.tbl_pattern[args[0]]
            temp = eval(querry)
            return temp
