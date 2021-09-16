class Address:
    def __init__(self):
        self.address_id = None
        self.address = None
        self.address2 = None
        self.city = None
        self.state = None
        self.zip_code = None
        self.country = None
class Guest(Address):
    def __init__(self):
        Address()
        self.guest_id = None
        self.type = None
        self.gender = None
        self.first_name = None
        self.last_name = None
        self.phone_number = None
        self.mail_address = None
        self.address_id = None
        self.id_number = None
        self.family_members = None
    def fetch_by_id(self):
        pass

