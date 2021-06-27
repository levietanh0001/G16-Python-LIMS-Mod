import pymysql

class SetDatabase:
    def __init__(self, hst, usr, pw, db, p):
        self.host_name = hst
        self.user_name = usr
        self.my_db = db
        self.my_pass = pw
        self.port_num = p

    def get_host(self):
        return self.host_name
    def get_user(self):
        return self.user_name
    def get_pass(self):
        return self.my_pass
    def get_db(self):
        return self.my_db
    def get_port(self):
        return self.port_num

db_obj = SetDatabase(hst="192.168.1.16", usr="root", pw="", db="g16_db", p=3306)
