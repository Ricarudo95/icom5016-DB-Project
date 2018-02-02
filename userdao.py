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

    def getUserResourcesRequested(self, u_id):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id in (select r_id from stransaction where u_id = %s and status = 'In process');"
        cursor.execute(query, (u_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserResourcesBought(self, u_id):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id in (select r_id from stransaction where u_id = %s and status = 'Completed');"
        cursor.execute(query, (u_id,))
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
        if c_update == 'True':
            update_query1 = "select c_id from creditcard where u_id = %s and cardnumber= %s and in_use = %s"
            cursor.execute(update_query1, (u_id,card_number, "True"))
            update_query2 = "update creditcard set in_use = %s where u_id = %s and cardnumber = %s"
            cursor.execute(update_query2, ("False", u_id, card_number))

        creditcard_query = "insert into creditcard (u_id, cardnumber, expiration_date, cvc_code, in_use) values (%s,%s, to_date(%s, 'MM-YY'), %s,%s) returning *"
        cursor.execute(creditcard_query, (u_id, card_number,expiration_date, cvc_code, 'True',))     
        self.conn.commit()
        result = []
        for row in cursor:
            result.append(row)
        return result

    def createRequest(self, r_id, u_id, quantity):
        cursor = self.conn.cursor()
        print("beggining")
        query1 = "select quantity from resource where r_id = %s "
        print("run query 1")
        cursor.execute(query1,(r_id,))
        qtyAvailable = cursor.fetchone()[0]
      
        query2 = "select price from resource where r_id = %s"
        print("run query 2")
        cursor.execute(query2, (r_id, ))
        price = cursor.fetchone()[0]
        print("All query Run")
        if price==0:
            status='Completed'
            update_query = "update resource set quantity = (quantity- %s) where r_id = %s"
            cursor.execute(update_query, (quantity, r_id, ))
        elif price > 0 and qtyAvailable > 0:
            status='In process'
        else:
            status='Out of stock'
        #create transaction
        query3 = "insert into stransaction (status, quantity, price, r_id, u_id) values (%s, %s, %s, %s, %s) returning t_id"
        cursor.execute(query3, (status, quantity, price, r_id, u_id,))

        t_id = cursor.fetchone()[0]
        self.conn.commit()
        return t_id      

    def getUserTransactionByID(self, t_id):
        cursor = self.conn.cursor()
        query = "select * from stransaction where u_id = %s;"
        cursor.execute(query, (t_id,))
        result = cursor.fetchone()
        return result

    def userPay(self, t_id,u_id,c_id):

        cursor = self.conn.cursor()

        check_query = "select status from stransaction where t_id = %s"
        cursor.execute(check_query, (t_id, ))
        status = cursor.fetchone()[0]

        check_query = "select u_id from creditcard where c_id = %s"
        cursor.execute(check_query, (c_id, ))
        card_owner = cursor.fetchone()[0]

        if status != "Completed" and u_id == card_owner:
            pq_query = "select quantity from stransaction where t_id = %s"
            cursor.execute(pq_query, (t_id, ))
            purchase_qty = cursor.fetchone()[0]

            id_query = "select r_id from stransaction where t_id = %s"
            cursor.execute(id_query, (t_id, ))
            r_id = cursor.fetchone()[0]

            qt_query = "select quantity from resource where r_id = %s"
            cursor.execute(qt_query, (r_id, ))
            current_qty = cursor.fetchone()[0]

            if current_qty >= purchase_qty:
                update_query = "update stransaction set c_id=%s, status = %s where t_id = %s"
                cursor.execute(update_query, (c_id, 'Completed', t_id, ))
                update_query = "update resource set quantity = (quantity- %s) where r_id = %s"
                cursor.execute(update_query, (purchase_qty, r_id ))
                self.conn.commit() 
                return t_id
            else:
                status = 'OutOfStock'
                update_query = "update stransaction set c_id=%s, status = %s where t_id = %s"
                cursor.execute(update_query, (c_id, status, t_id))
                self.conn.commit()
                return t_id
        else:
            return t_id

    def getUserCards(self, u_id):
        cursor = self.conn.cursor()
        query = "select * from creditcard where u_id = %s"
        cursor.execute(query, (u_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserTransaction(self, u_id):
        cursor = self.conn.cursor()
        query = "select * from stransaction where u_id = %s"
        cursor.execute(query, (u_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result


#-----------Search Functions--------------

    def getUserByFname(self, fname):
        cursor = self.conn.cursor()
        query = "select * from siteuser where uFirstName = %s;"
        cursor.execute(query, (fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByLname(self, lname):
        cursor = self.conn.cursor()
        query = "select * from siteuser where uFirstName = %s;"
        cursor.execute(query, (lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByLoc(self, loc):
        cursor = self.conn.cursor()
        query = "select * from siteuser where loc = %s;"
        cursor.execute(query, (loc,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByFnameLname(self, fname,lname):
        cursor = self.conn.cursor()
        query = "select * from siteuser where ufirstName = %s and ulastName = %s;"
        cursor.execute(query, (fname,lname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByLnameLoc(self, lname, loc):
        cursor = self.conn.cursor()
        query = "select * from siteuser where ufirstName = %s and loc = %s;"
        cursor.execute(query, (lname,loc,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByFnameLoc(self, loc, fname):
        cursor = self.conn.cursor()
        query = "select * from siteuser where loc = %s and ufirstName = %s;"
        cursor.execute(query, (loc,fname,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def getUserByFnameLnameLoc(self, fname,lname,loc):
        cursor = self.conn.cursor()
        query = "select * from siteuser where ufirstName = %s and ulastName = %s and loc = %s;"
        cursor.execute(query, (fname,lname, loc, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

#-----------------------------------------
        
