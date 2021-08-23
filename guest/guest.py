import sqlite3


class Guest:
    __database_name = r'test_db.db'

    def __init__(self):
        self.conn = sqlite3.connect(self.__database_name)
        self.cur = self.conn.cursor()
        self.guest_table_pattern = [
            'idGuest',
            'lastN',
            'firstN',
            'email',
            'Phone',
            'idAddress'
        ]

    def create_table(self):
        pass

    def getGuestDataByID(self, guest_id):
        try:
            sql = "SELECT * FROM Guests where guest_id='{}'".format(guest_id)
            self.cur.execute(sql)
            return dict(zip(self.guest_table_pattern, self.cur.fetchone()))
        except sqlite3.Error as Err:
            print(Err)
            return False

    def getGuestByName(self, name='', fetch_limit=15):
        self.name = name
        sql = "SELECT * FROM Guests where guest_first_name like '{}%' ".format(self.name)
        try:
            self.cur.execute(sql)
            rows = self.cur.fetchmany(size=fetch_limit)
            for pos, el in enumerate(rows):
                rows[pos] = dict(zip(self.guest_table_pattern, el))
            return rows
        except sqlite3.Error as Err:
            print(Err)

    def updateByID(self, new_guest=[]):
        try:
            sql = "UPDATE Guests SET guest_last_name='{}',guest_first_name='{}',guest_email='{}',guest_phone='{}' WHERE guest_id={}".format(
                new_guest[1], new_guest[2], new_guest[3], new_guest[4], int(new_guest[0]))
            self.cur.execute(sql)
            self.conn.commit()
            return True
        except sqlite3.Error as Err:
            print(Err)
            return False

    def getGuestInfo(self, fetch_limit=15):
        '''

        :param fetch_limit: max rows to fetch
        :return:
        '''
        sql = "SELECT * FROM Guests"
        try:
            self.cur.execute(sql)
            rows = self.cur.fetchmany(size=fetch_limit)
            for pos, el in enumerate(rows):
                rows[pos] = dict(zip(self.guest_table_pattern, el))
            return rows
        except sqlite3.Error as Err:
            print(Err)

    def addGuest(self, guest_first_name, guest_last_name, guest_email, guest_phone, adress_id="NULL"):
        sql = "INSERT INTO Guests(guest_first_name,guest_last_name,guest_email,guest_phone,address_id) VALUES ('{}','{}','{}','{}','{}')".format(
            guest_first_name, guest_last_name, guest_email, guest_phone, adress_id)
        try:
            self.cur.execute(sql)
            self.conn .commit()
            return self.cur.lastrowid
        except sqlite3.Error as Error:
            print(Error)

