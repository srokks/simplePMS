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
    def __init__(self,**kwargs):
        self.tbl_pattern = [
            'aAddressID',
            'aAddress',
            'aAddress2',
            'aCity',
            'aState',
            'aZipCode',
            'aCountry'
        ]
        if "aAddressList" in kwargs.keys():
            '''
            Inits attributes by list, musty be initiated by aAddressList in kwargs.
            Used to init instance from db fetched data.
            '''
            self.aAddressList = kwargs['aAddressList']
            if len(self.aAddressList)!=len(self.tbl_pattern):
                raise Exception("DATABASE INTEGRITY ERROR")
            else:
                self.aAddressID = self.aAddressList[0]
                self.aAddress = self.aAddressList[1]
                self.aAddress2 = self.aAddressList[2]
                self.aCity = self.aAddressList[3]
                self.aState = self.aAddressList[4]
                self.aZipCode = self.aAddressList[5]
                self.aCountry = self.aAddressList[6]
        else:
            self.aAddressID = kwargs['aAddressID'] if 'aAddressID' in kwargs.keys() else None
            self.aAddress = kwargs['aAddress'] if 'aAddress' in kwargs.keys() else None
            self.aAddress2 = kwargs['aAddress2'] if 'aAddress2' in kwargs.keys() else None
            self.aCity = kwargs['aCity'] if 'aCity' in kwargs.keys() else None
            self.aState = kwargs['aState'] if 'aState' in kwargs.keys() else None
            self.aZipCode = kwargs['aZipCode'] if 'aZipCode' in kwargs.keys() else None
            self.aCountry = kwargs['aCountry'] if 'aCountry' in kwargs.keys() else None

    def __call__(self, *args, **kwargs):
        if not args:
            print(self.aAddressID,self.aAddress,self.aAddress2,self.aCity,self.aState,self.aZipCode,self.aCountry,sep='|')
        else:
            print('kaks')
class AddressCtrl:
    __database_name = r'test_db.db'
    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.tbl_name = 'tblAddresses'
    def create_table(self):
        sql = (
            "CREATE TABLE IF NOT EXISTS 'tblAddresses' ("
            "'aAddressID'	INTEGER NOT NULL UNIQUE,"
            "'gAddress'	TEXT,"
            "'gAddress2'	TEXT,"
            "'gCity'	TEXT,"
            "'gState'	TEXT,"
            "'gZipCode'	TEXT,"
            "'gCountry'	TEXT,"
            "PRIMARY KEY('aAddressID' AUTOINCREMENT))"
        )
        try:
            self.cur.execute(sql)
            return True
        except sqlite3.Error as Err:
            print(Err)

    def getByID(self, g_id):
        try:
            # FixMe: does not check max id in tableś
            sql = f"SELECT * FROM {self.tbl_name} where {Address().tbl_pattern[0]}='{g_id}'"
            self.cur.execute(sql)
            address_list = self.cur.fetchone()
            a = Address(address_list=address_list)
            return Address(aAddressList=address_list)

        except sqlite3.Error as Err:
            print(Err)
            return False
