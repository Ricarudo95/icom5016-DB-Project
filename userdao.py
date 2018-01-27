from dbconfig import pg_config
import psycopg2

class UserDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                           pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from siteuser;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from siteuser where u_id = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getUserResources(self, u_id):
        cursor = self.conn.cursor()
        query = "--------------------------------------------;"
        cursor.execute(query, (u_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUserByName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from siteuser where uFirstName = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def addUser(self, fname, lname, upass, loc, address):
        cursor = self.conn.cursor()
        address_query = "insert into useraddress (location_name, region, city, zip_code) values (null,null,null,null) returning ua_id"
        cursor.execute(address_query, )
        ua_id = cursor.fetchone()[0]
        query = "insert into siteuser(uFirstName, uLastName, pass, loc, ua_id) values ( %s, %s, %s, %s, %s ) returning u_id"
        cursor.execute(query, (fname,lname,upass,loc,ua_id))
        u_id = cursor.fetchone()[0]
        
        self.conn.commit()
        return u_id
    
    def updateUserCreditCard(self,u_id, card_number, expiration_date, cvc_code, c_update):
        cursor = self.conn.cursor()
        if c_update:
            update_query1 = "select c_id from creditcard where u_id = %s and card_number= %s and in_use = %s"
            cursor.execute(update_query1, (u_id,card_number, "True"))
            update_query2 = "update creditcard set in_use = %s where u_id = %s and card_number = %s"
            cursor.execute(update_query2, ("False", u_id, card_number))

        creditcard_query = "insert into creditcard (u_id, card_number, expiration_date, cvc_code, in_use) values (%s,%s,%s,%s,%s) returning c_id"
        cursor.execute(creditcard_query, (u_id, card_number, expiration_date, cvc_code, c_update))
        c_id=cursor.fetchone()[0]
        self.conn.commit()
        return c_id
