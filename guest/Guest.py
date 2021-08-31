import sqlite3
class Guest:
    def __init__(self,**kwargs):
        '''
            gGuestID',
            'gGuestType',int, 0 - guest, 1 - comp., 2 - agent
            'gGender',int,0 - male, 1 -female
            'gFirstName',str
            'gLastName',str
            'gPhoneNumber', - str
            'gMailAddress',str
            'gIdNumber',str
            'FamilyMemberID', list of ints
            'gAddressID', int
        '''
        #
        self.tbl_pattern = [
            'gGuestID',
            'gGuestType',
            'gGender',
            'gFirstName',
            'gLastName',
            'gPhoneNumber',
            'gMailAddress',
            'gIdNumber',
            'gFamilyMemberID',
            'gAddressID',
        ]
        if 'gGuestList' in kwargs.keys():
            '''
            Inits attributes by list, musty be initiated by gGuestList in kwargs.
            Used to init instance from db fetched data.
            '''
            self.gGuestList = kwargs['gGuestList']

            if len(self.gGuestList)!=len(self.tbl_pattern):
                raise Exception("DATABASE INTEGRITY ERROR")
            else:
                self.gGuestID = self.gGuestList[0]
                self.gGuestType = self.gGuestList[1]
                self.gGender = self.gGuestList[2]
                self.gFirstName = self.gGuestList[3]
                self.gLastName = self.gGuestList[4]
                self.gPhoneNumber = self.gGuestList[5]
                self.gMailAddress = self.gGuestList[6]
                self.gIdNumber = self.gGuestList[7]
                self.FamilyMemberID = self.gGuestList[8]
                self.gAddressID = self.gGuestList[9]
        else:
            '''
            Inits by passing exact name of attribute in kwarg dict
            For testing purposes
            '''
            self.gGuestID = kwargs['gguestID'] if 'gguestID' in kwargs.keys() else None
            self.gGuestType = kwargs['gGuestType'] if 'gGuestType' in kwargs.keys() else None
            self.gGender = kwargs['gGender'] if 'ggender' in kwargs.keys() else None
            self.gFirstName = kwargs['gFirstName'] if 'gFirstName' in kwargs.keys() else None
            self.gLastName = kwargs['gLastName'] if 'gLastName' in kwargs.keys() else None
            self.gPhoneNumber = kwargs['gPhoneNumber'] if 'gPhoneNumber' in kwargs.keys() else None
            self.gMailAddress = kwargs['gMailAddress'] if 'gMailAddress' in kwargs.keys() else None
            self.gIdNumber = kwargs['gIDNumber'] if 'gIDNumber' in kwargs.keys() else None
            self.FamilyMemberID = kwargs['FamilyMemberIDs'] if 'FamilyMemberIDs' in kwargs.keys() else []
            self.gAddressID = kwargs['gAddressID'] if 'gAddressID' in kwargs.keys() else None

    def __call__(self,*args,**kwargs):
        if not args:
            print(self.gGuestID, self.gGuestType, self.gGender, self.gFirstName, self.gLastName, self.gPhoneNumber, self.gMailAddress, self.gIdNumber, self.FamilyMemberID, self.gAddressID, sep="|")
    def addFamilyMember(self,gFamilyMemberID):
        self.FamilyMemberID+=a
class GuestCtrl:
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.tbl_name = 'tblGuest'
    def create_table(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS 'tblGuest' ("
            "'gGuestID'	INTEGER NOT NULL UNIQUE,"
            "'gGuestType'	INTEGER,"
            "'gGender'	INTEGER,"
            "'gFirstName'	TEXT,"
            "'gLastName'	BLOB,"
            "'gPhoneNumber'	TEXT,"
            "'gMailAddress'	TEXT,"
            "'gIDNumber'	TEXT,"
            "'gFamilyMemberID'  TEXT,"
            "'gAddressID'   INTEGER,"
            "PRIMARY KEY('gGuestID' AUTOINCREMENT))"
        )
        try:
            self.cur.execute(sql)
            return True
        except sqlite3.Error as Err:
            print(Err)

    def getByID(self, g_id):
        try:
            #FixMe: does not check max id in tableś
            sql = f"SELECT * FROM {self.tbl_name} where {Guest().tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            guest_list = self.cur.fetchone()
            return Guest(gGuestList=guest_list)

        except sqlite3.Error as Err:
            print(Err)
            return False

    def add(self, guest):
        sql = (
            f"INSERT INTO {self.tbl_name} ({','.join(Guest().tbl_pattern[1:])}) "
            f"VALUES ("
            f"'{guest.gGuestType}',"
            f"'{guest.gGender}',"
            f"'{guest.gFirstName}',"
            f"'{guest.gLastName}',"
            f"'{guest.gPhoneNumber}',"
            f"'{guest.gMailAddress}',"
            f"'{guest.gIdNumber}',"
            f"'{guest.FamilyMemberID}'," 
            f"'{guest.gAddressID}')"
        )
        try:
            self.cur.execute(sql)
            self.conn.commit()
            return self.cur.lastrowid
        except sqlite3.Error as Err:
            print(sql)
            print('ERROR OCCURED:', Err)