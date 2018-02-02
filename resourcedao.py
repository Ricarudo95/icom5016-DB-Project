from dbconfig import pg_config
import psycopg2

class ResourceDAO:
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                           pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceById(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id = %s;"
        cursor.execute(query, (r_id,))
        result = cursor.fetchone()
        return result

    #check if resource is available

    def checkAvailableByID(self, r_id):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id = %s and quantity > 0;"
        cursor.execute(query, (r_id,))
        result = cursor.fetchone()
        return result

    #get all available resources

    def getAvailableResource(self):
        cursor = self.conn.cursor()
        query = "select * from resource where quantity > 0;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    #Route used to search available resources via keyword(search resource names)
    def searchAvailable(self, keyword):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s;"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    #get list of resources requested
    def getRequestedResource(self):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id in (select r_id from stransaction where status = 'In process');"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # search available resources via keyword(search resource names). Sorted by Resouce name
    def searchRequested(self, keyword):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s and quantity > 0 order by(rname);"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result
	    
    def getResourcesSuppplierFrom(self, rid, location):
        cursor = self.conn.cursor()
        query = "select s_id, sname, pass, loc, sa_id from supplier natural inner join resource where loc = %s and r_id = %s ;"
        cursor.execute(query, (location,rid, ))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, s_id, rname, category, quantity, price):
        cursor = self.conn.cursor()
        query = "insert into resource(s_id, rname, category, quantity, price) values (%s, %s, %s, %s, %s) returning r_id;"
        cursor.execute(query, ( s_id, rname, category, quantity, price,))
        r_id = cursor.fetchone()[0]
        self.conn.commit()
        return r_id

    def update(self, r_id,  s_id, rname, category, quantity, price):
        cursor = self.conn.cursor()
        query = "update resource set s_id= %s, rname=%s, category=%s, quantity=%s, price=%s where r_id =%s;"
        cursor.execute(query, ( s_id, rname, category, quantity, price, r_id,))
        self.conn.commit()
        return r_id


#--------Search Resource Daos


    def searchByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def searchByCat(self,cat):
        cursor = self.conn.cursor()
        query = "select * from resource where category = %s;"
        cursor.execute(query, (cat,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    
    def searchByNameAvailable(self, name):
        cursor = self.conn.cursor()
        query = "select * from resource where rname = %s and quantity >0;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def searchByNameRequested(self, name):
        cursor = self.conn.cursor()
        query = "select * from resource where category = %s r_id in (select r_id from stransaction where status = 'In process');"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def searchByCatAvailable(self, cat):
        cursor = self.conn.cursor()
        query = "select * from resource where category = %s and quantity > 0;"
        cursor.execute(query, (cat,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        

    def searchByCatRequested(self, cat):
        cursor = self.conn.cursor()
        query = "select * from resource where category = %s r_id in (select r_id from stransaction where status = 'In process');"
        cursor.execute(query, (cat,))
        result = []
        for row in cursor:
            result.append(row)
        return result
        

#--------Search Suppliers Daos

    def supplierByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join resource where rname = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def supplierByCat(self, cat):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join resource where category = %s;"
        cursor.execute(query, (cat,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def supplierByNameAndLoc(self, name, loc):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join resource where rname = %s and loc = %s;"
        cursor.execute(query, (name,loc,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    
    def supplierByCatAndLoc(self, cat, loc):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join resource where category = %s and loc = %s;"
        cursor.execute(query, (cat,loc))
        result = []
        for row in cursor:
            result.append(row)
        return result

#-----------------------------        
    

