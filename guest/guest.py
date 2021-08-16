import sqlite3


class Guest:
    __database_name = r'test_db.db'
    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(Guest.__database_name)
        self.cur = self.connection.cursor()

    def create_table(self):
        """TODO:create a database table if it does not exist already"""

    def getGuests(self):
        self.cur.execute("SELECT * FROM GUEST")
        self.rows = self.cur.fetchall()
        return self.rows

    def addAdress(self,_line_1,_line_2,_zip_code,_city):
        '''
        Inserts new id
        :param _line_1:str
        :param _line_2: std
        :param _zip_code: std
        :param _city:std
        :return: inserted row id from db
        '''
        sql_command = "INSERT INTO Adresses(line_1,line_2,zip_code,city) VALUES ('{}','{}','{}','{}')".format(_line_1,_line_2,_zip_code,_city)
        try:
            self.cur.execute(sql_command)
            self.connection.commit()
        except sqlite3.Error as Error:
            print(Error)
        finally:
            print("Values added to database!")
            return self.cur.lastrowid

    def addAdressDialogue(self):


print(Guest().addAdress("Podhalańska","47","34-471","Ludźmierz"))

