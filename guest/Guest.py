import sqlite3


class Address:
    '''
        :params
        'aAddressID' - int
        'aAddress' - str -
        'aAddress2' - str
        'aCity'- str
        'aState' - str
        'aZipCode'- str
        'aCountry' - str
        '''

    def __init__(self, **kwargs):
        self.tbl_pattern = [
            'aAddressID',
            'aAddress',
            'aAddress2',
            'aCity',
            'aState',
            'aZipCode',
            'aCountry'
        ]
        self.AddressID = None
        self.Address = ''
        self.Address2 = ''
        self.City = ''
        self.State = ''
        self.ZipCode = ''
        self.Country = ''
        if 'aList' in kwargs.keys() and kwargs['aList']!=None:
            self.AddressID = kwargs['aList'][0]
            self.Address = kwargs['aList'][1]
            self.Address2 = kwargs['aList'][2]
            self.City = kwargs['aList'][3]
            self.State = kwargs['aList'][4]
            self.ZipCode = kwargs['aList'][5]
            self.Country = kwargs['aList'][6]

    def __call__(self, *args, **kwargs):
        print(self.AddressID,self.Address, self.Address2, self.City, self.State, self.ZipCode, self.Country, sep='|')


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
        self.guest_tbl_name = 'tblGuest'
        self.guest_tbl_pattern = [
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
        self.GuestID = None
        self.GuestType = None
        self.Gender = None
        self.FirstName = ''
        self.LastName = ''
        self.PhoneNumber = ''
        self.MailAddress = ''
        self.IdNumber = ''
        self.FamilyMemberID = []
        self.AddressID = ''
        if 'aList' in kwargs.keys():
            '''Inicjowanie adresu z listy, jeżeli nie w kwargs a list to tylko inicjuje puste'''
            Address.__init__(self, aList=kwargs['aList'])
        else:
            Address.__init__(self)
        if 'gList' in kwargs.keys() and kwargs['gList']!=None:
            gList = kwargs['gList']
            self.GuestID = gList[0]
            self.GuestType = gList[1]
            self.Gender = gList[2]
            self.FirstName = gList[3]
            self.LastName = gList[4]
            self.PhoneNumber = gList[5]
            self.MailAddress = gList[6]
            self.IdNumber = gList[7]
            self.FamilyMemberID = gList[8]
            self.AddressID = gList[9]

    def __call__(self, *args, **kwargs):
        print('GUEST',self.GuestID, self.FirstName, self.LastName, self.PhoneNumber, self.MailAddress, self.IdNumber,
              self.FamilyMemberID, self.AddressID, sep="|")
        print('ADDRESS',self.AddressID,self.Address, self.Address2, self.City, self.State, self.ZipCode, self.Country, sep='|')


class Controller:
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.guest_tbl_name = 'tblGuest'
        self.address_tbl_name = 'tblAddresses'
        self.guest_tbl_pattern = Guest().guest_tbl_pattern.copy()
        self.address_tbl_pattern = Address().tbl_pattern.copy()

    def _get_guest_by_id(self, g_id):
        'Fetch guest info from db and return it as list'
        sql = f"SELECT * FROM {self.guest_tbl_name} WHERE {self.guest_tbl_pattern[0]}={g_id}"
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()
        except sqlite3.Error as Err:
            print('***ERROR OCCURED ***\n|', Err, '|')
        pass

    def _get_address_by_id(self, a_id):
        'Fetch address info from db adn return it as list'

        sql = f"SELECT * FROM {self.address_tbl_name} WHERE {self.address_tbl_pattern[0]}={a_id}"
        try:
            self.cur.execute(sql)
            return self.cur.fetchone()
        except sqlite3.Error as Err:
            print('***ERROR OCCURED***\n|', Err, '|')
        pass

    def get_by_id(self, g_id):
        'Fetch all guest info (main info + address) and return GuestObject '
        gList = self._get_guest_by_id(g_id)
        if gList[9]!='':
            aList = self._get_address_by_id(gList[9])
            return  Guest(gList=gList,aList=aList)
        else:
            return Guest(gList=gList)
    def add_address(self,guest):
        'Adds address entry to db and return, modifies ids in guest  - '
        sql = f"INSERT INTO {self.address_tbl_name} " \
              f"({','.join(self.address_tbl_pattern[1:])}) " \
              f"VALUES (" \
              f"'{guest.Address}',"\
              f"'{guest.Address2}'," \
              f"'{guest.City}',"\
              f"'{guest.State}',"\
              f"'{guest.ZipCode}',"\
              f"'{guest.Country}')"\


        try:
            self.cur.execute(sql)
            guest.AddressID = self.cur.lastrowid
            return True
        except sqlite3.Error as Err:
            print('***ERROR OCCURED***\n|', Err, '|')

    def add_guest(self,guest):
        'Add guest to db and return true or false'
        sql = f"INSERT INTO {self.guest_tbl_name}" \
              f"({','.join(self.guest_tbl_pattern[1:])}) " \
              f"VALUES " \
              f"('{guest.GuestType}',"\
              f"'{guest.Gender}',"\
              f"'{guest.FirstName}',"\
              f"'{guest.LastName}',"\
              f"'{guest.PhoneNumber}',"\
              f"'{guest.MailAddress}',"\
              f"'{guest.IdNumber}',"\
              f"'',"\
              f"{guest.AddressID})"
        try:
            self.cur.execute(sql)
            guest.GuestID = self.cur.lastrowid

            return True
        except sqlite3.Error as Err:
            print('***ERROR OCCURED***\n|', Err, '|')
            return False
    def add(self,guest):
        'Adds guest obj to database'
        if self.add_address(guest):
            if self.add_guest(guest):
                self.conn.commit()
                return True
            else:
                return False
        else:
           return False

    def get_guest_by_names(self,keyword,fetch_limit=15):
        table = [self.guest_tbl_pattern[4],self.guest_tbl_pattern[3],self.guest_tbl_pattern[5],self.guest_tbl_pattern[6],self.address_tbl_pattern[3]]
        keyword = dict(zip(table,keyword))

        sql = f"SELECT {self.guest_tbl_pattern[0]} " \
              f"FROM {self.guest_tbl_name} INNER JOIN {self.address_tbl_name} " \
              f"ON {self.guest_tbl_name}.{self.guest_tbl_pattern[9]}=" \
              f"{self.address_tbl_name}.{self.address_tbl_pattern[0]}" \
              f" WHERE "

        for key in keyword.keys():
            if keyword[key]!='':
                if key == 'aCity':
                    sql += f"{self.address_tbl_name}.{key} LIKE '{keyword[key]}%'"
                    sql += ' AND '
                else:
                    sql+=f"{key} LIKE '{keyword[key]}%'"
                    sql+=' AND '

            else:
                pass
        if sql[-7:]==' WHERE ':sql=sql[:-7]
        if sql[-5:]==' AND ':sql=sql[:-5]
        try:
            self.cur.execute(sql)
            results = self.cur.fetchmany(fetch_limit)


            guests_list = []
            for el in results:
                guests_list.append(self.get_by_id(el[0]))


            return guests_list
        except sqlite3.Error as Err:
            print("--Fetch by name--")
            print('***ERROR OCCURED***\n|', Err, '|')
            # print(sql)
            return False

    def update_guest(self,guest):
        old_guest = self.get_by_id(guest.GuestID)
        try:
            sql = f"UPDATE {self.guest_tbl_name} " \
                  f"SET "
                  # f"{self.guest_tbl_pattern[1]}={guest.GuestType},"\
                  # f"{self.guest_tbl_pattern[2]}={guest.Gender},"\
                  # f"{self.guest_tbl_pattern[3]}={guest.FirstName},"\
                  # f"{self.guest_tbl_pattern[4]}={guest.LastName},"\
                  # f"{self.guest_tbl_pattern[5]}={guest.PhoneNumber},"\
                  # f"{self.guest_tbl_pattern[6]}={guest.MailAddress},"

            if old_guest.GuestType!=guest.GuestType:
                sql+=f"{self.guest_tbl_pattern[1]}='{guest.GuestType}',"
            if old_guest.Gender != guest.Gender:
                sql += f"{self.guest_tbl_pattern[2]}='{guest.Gender}',"
            if old_guest.FirstName != guest.FirstName:
                sql += f"{self.guest_tbl_pattern[3]}='{guest.FirstName}',"
            if old_guest.LastName != guest.LastName:
                sql += f"{self.guest_tbl_pattern[4]}='{guest.LastName}',"
            if old_guest.PhoneNumber != guest.PhoneNumber:
                sql += f"{self.guest_tbl_pattern[5]}='{guest.PhoneNumber}',"
            if old_guest.MailAddress != guest.MailAddress:
                sql += f"{self.guest_tbl_pattern[6]}='{guest.MailAddress}',"
            if old_guest.IdNumber != guest.IdNumber:
                sql += f"{self.guest_tbl_pattern[7]}='{guest.IdNumber}',"
            if sql[-1:]==",":sql=sql[:-1]
            sql += f" WHERE {self.guest_tbl_pattern[0]}='{guest.GuestID}'"
            self.cur.execute(sql)
            self.conn.commit()
            #TODO:zmiana adresu
            return True
        except sqlite3.Error as Err:
            print("--Update by id--")
            print('***ERROR OCCURED***\n|', Err, '|')
            print(sql)
            return False
