import MySQLdb
class DbFunctions(object):
    def __init__(self,server,username,password,dbname):
        self.server = server
        self.username = username
        self.password = password
        self.dbname = dbname
        self.db = None
        self.cur = None

    def connection_open(self):
        self.db = MySQLdb.connect(host=self.server,user=self.username,passwd=self.password,db=self.dbname)
        self.cur = self.db.cursor()

    def connection_close(self):
        self.db.close()
# Python Library for Simple DB Operations
    def mysql_qry(self,sql,bool): # 1 for select and 0 for insert update delete
        self.connection_open()
        try:
            self.cur.execute(sql)
            if bool:
                return self.cur.fetchall()
            else:
                self.db.commit()
                return True
        except MySQLdb.Error, e:
            try:
                print "Mysql Error:- "+str(e)
            except IndexError:
                print "Mysql Error:- "+str(e)
        self.connection_close()

    def mysql_insert(self,table,fields,values):
        sql = "INSERT INTO " + table + " (" + fields + ") VALUES (" + values + ")";
        #print sql
        return self.mysql_qry(sql,0)


db = DbFunctions("localhost","root","root","clients_edit_place_db")
result = db.mysql_qry("SELECT * FROM `cep_languages`",1)
print result;
result = db.mysql_insert("cep_languages","`lang_name`,`lang_code`","'Espanish','es'")
print result;
