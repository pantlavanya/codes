#Simple Library for Python with DB Connection and Querying
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
        return self.mysql_qry(sql,0)

    def mysql_update(self,table,values,conditions):
        sql = "UPDATE " + table + " SET " + values + " WHERE " + conditions
        return self.mysql_qry(sql,0)

    def mysql_delete(self,table,condtions):
        sql = "DELETE FROM " + table + " WHERE " + condition;
        return self.mysql_qry(sql,0)

    def mysql_select(self,table):
        sql =  "SELECT * FROM "+table
        return self.mysql_qry(sql,1)

db = DbFunctions("localhost","root","root","clients_edit_place_db")
result = db.mysql_qry("",1)
print result;
result = db.mysql_insert("cep_languages","`lang_name`,`lang_code`","'Espanish','es'") # In place of string we can pass List also
print result;
