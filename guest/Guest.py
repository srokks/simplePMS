import sqlite3
from Address import Address,AddressCtrl

class Guest:
    def __init__(self, **kwargs):
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
            if self.gGuestList == None:
                print('*DATABASE EROOR INTEGRITY*')
            if len(self.gGuestList) != len(self.tbl_pattern):
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

    def __call__(self, *args, **kwargs):
        if not args:
            print(self.gGuestID, self.gGuestType, self.gGender, self.gFirstName, self.gLastName, self.gPhoneNumber,
                  self.gMailAddress, self.gIdNumber, self.FamilyMemberID, self.gAddressID, sep="|")
            self.address = AddressCtrl().get_by_id(self.gAddressID) if AddressCtrl().get_by_id(self.gAddressID)!=False else Address()
            if self.address!=None:
                self.address()

class GuestCtrl:
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.tbl_name = 'tblGuest'
        self.tbl_pattern = Guest().tbl_pattern.copy()
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

    def check_id(self, g_id):
        try:
            sql = f"SELECT * FROM {self.tbl_name} where {Guest().tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            if self.cur.fetchone() == None:
                return False
            else:
                return True
        except sqlite3.Error as Err:
            print(Err)
            return False

    def get_by_id(self, g_id):
        if self.check_id(g_id):
            try:
                sql = f"SELECT * FROM {self.tbl_name} where {self.tbl_pattern[0]}='{g_id}'"
                self.cur.execute(sql)

                guest_list = self.cur.fetchone()
                return Guest(gGuestList=guest_list)

            except sqlite3.Error as Err:
                print(Err)
                return False
        else:
            return False

    def add(self, guest):
        sql = (
            f"INSERT INTO {self.tbl_name} ({','.join(self.tbl_pattern[1:])}) "
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

    def get_members_of_guest(self, g_id):
        try:
            sql = f"SELECT gFamilyMemberID from {self.tbl_name} WHERE {self.tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            return self.cur.fetchone()[0]
        except sqlite3.Error as Err:
            print(Err)
            return False

    def add_member_to_guest(self, mem, g_id):
        try:
            mem = str(mem)
            g_id = str(g_id)
            sg_members = self.get_members_of_guest(g_id)
            if sg_members == '':
                sg_members = []
            else:
                sg_members = sg_members.split(',')
            sg_members.append(mem)
            sg_members = ','.join(sg_members)

            sql = f"UPDATE {self.tbl_name} SET {self.tbl_pattern[8]}='{sg_members}' WHERE {self.tbl_pattern[0]}='{g_id}'"
            # print(sql)

            # ---
            self.cur.execute(sql)
            self.conn.commit()



        except sqlite3.Error as Err:
            print(Err)
            return False

    def addFamilyMember(self, sg_id, fg_id):
        if self.check_id(sg_id) and self.check_id(fg_id):
            self.add_member_to_guest(fg_id, sg_id)
            self.add_member_to_guest(sg_id, fg_id)
            return True
        else:
            return False

    def add_address(self,g_id,a_id):
        if AddressCtrl().check_id(a_id) and self.check_id(g_id):
            try:
                sql = f"UPDATE {self.tbl_name} SET {self.tbl_pattern[9]}='{a_id}' WHERE {self.tbl_pattern[0]}='{g_id}'"
                self.cur.execute(sql)
                self.conn.commit()
                # print(sql)
                return True
            except sqlite3.Error as Err:
                print(Err)
                return False
        else:
            return False
    def get_attribute_by_id(self,g_id,param):
        if param in self.tbl_pattern and self.check_id(g_id):
            try:
                sql = f"SELECT {self.tbl_pattern[self.tbl_pattern.index(param)]} FROM {self.tbl_name} WHERE {self.tbl_pattern[0]}='{g_id}'"
                print(sql)
                self.cur.execute(sql)
                a = self.cur.fetchone()
                print(a)
                return True

            except sqlite3.Error as Err:
                print(Err)
                return False
        else:
            return False
GuestCtrl().get_attribute_by_id(99,'gLastName')
