import sqlite3


class Guest:
    '''
    obsługa zapytań bazodanowych gościa
    '''
    __database_name = r'test_db.db'
#TODO - funcja pobierająca zaptanie sql i je realizująca wraz z obsługą błędów
    def __init__(self):
        """Initialize db class variables"""
        self.connection = sqlite3.connect(Guest.__database_name)
        self.cur = self.connection.cursor()
        # self.create_table()

    def create_table(self):
        """Create table if non exsist"""
        sql = ("CREATE TABLE 'Guests'"
               "'guest_id'	INTEGER NOT NULL UNIQUE,"
               "'guest_first_name'	TEXT,"
               "'guest_last_name'	TEXT,"
               "'guest_email'	TEXT,"
               "'guest_phone'	TEXT,"
               "'address_id'	INTEGER,"
               "FOREIGN KEY('address_id') REFERENCES 'Adresses'('address_id') ON DELETE SET NULL,"
               "PRIMARY KEY('guest_id' AUTOINCREMENT))")
        try:
            print("Creating database Guests")
            self.cur.execute(sql)
        except sqlite3.Error as Error:
            print(Error)
        finally:
            print("Created database Guests")
            return True
    def getGuestbyID(self,g_id):
        # temp = ["guest_id","guest_first_name","guest_last_name","guest_email","guest_phone","adress_id"]
        self.cur.execute("SELECT * FROM Guests where guest_id='{}'".format(g_id))
        self.row = self.cur.fetchone()
        return self.row
    def getGuestsbyName(self,name=''):
        # temp = ["guest_id","guest_first_name","guest_last_name","guest_email","guest_phone","adress_id"]
        self.name = name
        self.cur.execute("SELECT * FROM Guests where guest_first_name like '{}%' ".format(self.name))
        self.rows = self.cur.fetchall()
        return self.rows[0:15]
    def updateByID(self,new_data_list=[]):
        """
        Update database
        :param new_data_list[5]:[id,last_name,first_name,mail,phone        ]
        :return:
        """


        sql = "UPDATE Guests SET guest_last_name='{}',guest_first_name='{}',guest_email='{}',guest_phone='{}' WHERE guest_id={}".format(new_data_list[1],new_data_list[2],new_data_list[3],new_data_list[4],int(new_data_list[0]))
        self.cur.execute(sql)
        self.connection.commit()

    def getGuestInfo(self):
        sql = "SELECT * from Guests, Adresses WHERE Guests.address_id=Addresses.address_id"
        self.cur.execute(sql)
        self.rows = self.cur.fetchall()
        return self.rows

    def addGuest(self, guest_first_name, guest_last_name, guest_email, guest_phone, adress_id="NULL"):
        sql_command = "INSERT INTO Guests(guest_first_name,guest_last_name,guest_email,guest_phone,address_id) VALUES ('{}','{}','{}','{}','{}')".format(
            guest_first_name, guest_last_name, guest_email, guest_phone, adress_id)
        try:
            self.cur.execute(sql_command)
            self.connection.commit()
        except sqlite3.Error as Error:
            print(Error)
        finally:
            return self.cur.lastrowid

    def addAddress(self, _line_1, _line_2, _zip_code, _city):
        '''
        Inserts new id
        :param _line_1:str
        :param _line_2: std
        :param _zip_code: std
        :param _city:std
        :return: inserted row id from db
        '''
        sql_command = "INSERT INTO Adresses(line_1,line_2,zip_code,city) VALUES ('{}','{}','{}','{}')".format(_line_1,
                                                                                                              _line_2,
                                                                                                              _zip_code,
                                                                                                              _city)
        try:
            self.cur.execute(sql_command)
            self.connection.commit()
        except sqlite3.Error as Error:
            print(Error)
        finally:
            print("Values added to database!")
            return self.cur.lastrowid

def insert_raw_data():
    Guest().addGuest("Maria","Anders","Maria@Anders.com","(171) 555-2222")
    Guest().addGuest("Ana","Trujillo","Ana@Trujillo.com","(100) 555-4822")
    Guest().addGuest("Antonio","Moreno","Antonio@Moreno.com","(313) 555-5735")
    Guest().addGuest("Thomas","Hardy","Thomas@Hardy.com","(03) 3555-5011")
    Guest().addGuest("Christina","Berglund","Christina@Berglund.com","(98) 598 76 54")
    Guest().addGuest("Hanna","Moos","Hanna@Moos.com","(06) 431-7877")
    Guest().addGuest("Frédérique","Citeaux","Frédérique@Citeaux.com","(03) 444-2343")
    Guest().addGuest("Martín","Sommer","Martín@Sommer.com","(161) 555-4448")
    Guest().addGuest("Laurence","Lebihans","Laurence@Lebihans.com","031-987 65 43")
    Guest().addGuest("Elizabeth","Lincoln","Elizabeth@Lincoln.com","(11) 555 4640")
    Guest().addGuest("Victoria","Ashworth","Victoria@Ashworth.com","(010) 9984510")
    Guest().addGuest("Patricio","Simpson","Patricio@Simpson.com","(069) 992755")
    Guest().addGuest("Francisco","Chang","Francisco@Chang.com","(04721) 8713")
    Guest().addGuest("Yang","Wang","Yang@Wang.com","(0544) 60323")
    Guest().addGuest("Pedro","Afonso","Pedro@Afonso.com","(0)2-953010")
    Guest().addGuest("Elizabeth","Brown","Elizabeth@Brown.com","(503) 555-9931")
    Guest().addGuest("Sven","Ottlieb","Sven@Ottlieb.com","08-123 45 67")
    Guest().addGuest("Janine","Labrune","Janine@Labrune.com","(1) 03.83.00.68")
    Guest().addGuest("Ann","Devon","Ann@Devon.com","(617) 555-3267")
    Guest().addGuest("Roland","Mendel","Roland@Mendel.com","555-8787")
    Guest().addGuest("Aria","Cruz","Aria@Cruz.com","43844108")
    Guest().addGuest("Diego","Roel","Diego@Roel.com","(12345) 1212")
    Guest().addGuest("Martine","Rancé","Martine@Rancé.com","(953) 10956")
    Guest().addGuest("Maria","Larsson","Maria@Larsson.com","(02) 555-5914")
    Guest().addGuest("Peter","Franken","Peter@Franken.com","(514) 555-9022")
    Guest().addGuest("Carine","Schmitt","Carine@Schmitt.com","(089) 6547665")
    Guest().addGuest("Paolo","Accorti","Paolo@Accorti.com","85.57.00.07")
    Guest().addGuest("Lino","Rodriguez","Lino@Rodriguez.com","38.76.98.06")
    Guest().addGuest("Eduardo","Saavedra","Eduardo@Saavedra.com","(514) 555-2955")
    Guest().addGuest("José","Pedro","José@Pedro.com","(171) 555-2222")
    Guest().addGuest("André","Fonseca","André@Fonseca.com","(100) 555-4822")
    Guest().addGuest("Howard","Snyder","Howard@Snyder.com","(313) 555-5735")
    Guest().addGuest("Manuel","Pereira","Manuel@Pereira.com","(03) 3555-5011")
    Guest().addGuest("Mario","Pontes","Mario@Pontes.com","(98) 598 76 54")
    Guest().addGuest("Carlos","Hernández","Carlos@Hernández.com","(06) 431-7877")
    Guest().addGuest("Yoshi","Latimer","Yoshi@Latimer.com","(03) 444-2343")
    Guest().addGuest("Patricia","McKenna","Patricia@McKenna.com","(161) 555-4448")
    Guest().addGuest("Helen","Bennett","Helen@Bennett.com","031-987 65 43")
    Guest().addGuest("Philip","Cramer","Philip@Cramer.com","(11) 555 4640")
    Guest().addGuest("Daniel","Tonini","Daniel@Tonini.com","(010) 9984510")
    Guest().addGuest("Annette","Roulet","Annette@Roulet.com","(069) 992755")
    Guest().addGuest("Yoshi","Tannamuri","Yoshi@Tannamuri.com","(04721) 8713")
    Guest().addGuest("John","Steel","John@Steel.com","(0544) 60323")
    Guest().addGuest("Renate","Messner","Renate@Messner.com","(0)2-953010")
    Guest().addGuest("Jaime","Yorres","Jaime@Yorres.com","(503) 555-9931")
    Guest().addGuest("Carlos","González","Carlos@González.com","08-123 45 67")
    Guest().addGuest("Felipe","Izquierdo","Felipe@Izquierdo.com","(1) 03.83.00.68")
    Guest().addGuest("Fran","Wilson","Fran@Wilson.com","(617) 555-3267")
    Guest().addGuest("Giovanni","Rovelli","Giovanni@Rovelli.com","555-8787")
    Guest().addGuest("Catherine","Dewey","Catherine@Dewey.com","43844108")
    Guest().addGuest("Jean","Fresnière","Jean@Fresnière.com","(12345) 1212")
    Guest().addGuest("Alexander","Feuer","Alexander@Feuer.com","(953) 10956")
    Guest().addGuest("Simon","Crowther","Simon@Crowther.com","(02) 555-5914")
    Guest().addGuest("Yvonne","Moncada","Yvonne@Moncada.com","(514) 555-9022")
    Guest().addGuest("Rene","Phillips","Rene@Phillips.com","(089) 6547665")
    Guest().addGuest("Henriette","Pfalzheim","Henriette@Pfalzheim.com","85.57.00.07")
    Guest().addGuest("Marie","Bertrand","Marie@Bertrand.com","38.76.98.06")
    Guest().addGuest("Guillermo","Fernández","Guillermo@Fernández.com","(514) 555-2955")
    Guest().addGuest("Georg","Pipps","Georg@Pipps.com","(171) 555-2222")
    Guest().addGuest("Isabel","de","Isabel@de.com","(100) 555-4822")
    Guest().addGuest("Bernardo","Batista","Bernardo@Batista.com","(313) 555-5735")
    Guest().addGuest("Lúcia","Carvalho","Lúcia@Carvalho.com","(03) 3555-5011")
    Guest().addGuest("Horst","Kloss","Horst@Kloss.com","(98) 598 76 54")
    Guest().addGuest("Sergio","Gutiérrez","Sergio@Gutiérrez.com","(06) 431-7877")
    Guest().addGuest("Paula","Wilson","Paula@Wilson.com","(03) 444-2343")
    Guest().addGuest("Maurizio","Moroni","Maurizio@Moroni.com","(161) 555-4448")
    Guest().addGuest("Janete","Limeira","Janete@Limeira.com","031-987 65 43")
    Guest().addGuest("Michael","Holz","Michael@Holz.com","(11) 555 4640")
    Guest().addGuest("Alejandra","Camino","Alejandra@Camino.com","(010) 9984510")
    Guest().addGuest("Jonas","Bergulfsen","Jonas@Bergulfsen.com","(069) 992755")
    Guest().addGuest("Jose","Pavarotti","Jose@Pavarotti.com","(04721) 8713")
    Guest().addGuest("Hari","Kumar","Hari@Kumar.com","(0544) 60323")
    Guest().addGuest("Jytte","Petersen","Jytte@Petersen.com","(0)2-953010")
    Guest().addGuest("Dominique","Perrier","Dominique@Perrier.com","(503) 555-9931")
    Guest().addGuest("Art","Braunschweiger","Art@Braunschweiger.com","08-123 45 67")
    Guest().addGuest("Pascale","Cartrain","Pascale@Cartrain.com","(1) 03.83.00.68")
    Guest().addGuest("Liz","Nixon","Liz@Nixon.com","(617) 555-3267")
    Guest().addGuest("Liu","Wong","Liu@Wong.com","555-8787")
    Guest().addGuest("Karin","Josephs","Karin@Josephs.com","43844108")
    Guest().addGuest("Miguel","Angel","Miguel@Angel.com","(12345) 1212")
    Guest().addGuest("Anabela","Domingues","Anabela@Domingues.com","(953) 10956")
    Guest().addGuest("Helvetius","Nagy","Helvetius@Nagy.com","(02) 555-5914")
    Guest().addGuest("Palle","Ibsen","Palle@Ibsen.com","(514) 555-9022")
    Guest().addGuest("Mary","Saveley","Mary@Saveley.com","(089) 6547665")
    Guest().addGuest("Paul","Henriot","Paul@Henriot.com","85.57.00.07")
    Guest().addGuest("Rita","Müller","Rita@Müller.com","38.76.98.06")
    Guest().addGuest("Pirkko","Koskitalo","Pirkko@Koskitalo.com","(514) 555-2955")
    Guest().addGuest("Paula","Parente","Paula@Parente.com","38.76.98.07")
    Guest().addGuest("Karl","Jablonski","Karl@Jablonski.com","(514) 555-2956")
    Guest().addGuest("Matti","Karttunen","Matti@Karttunen.com","38.76.98.08")

# new_data = ['117','Maria','Magdalena','maria@niebo.com','777888777']
# Guest().updateByID(new_data)
