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

    def getResourceById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id = %s;"
        cursor.execute(query, (pid,))
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

     #get list of suppliers of specific resource
    def getResourceSupplierById(self, r_id):
        cursor = self.conn.cursor()
        query = "select s_id, sname, pass, loc, sa_id from supplier natural inner join resource where r_id = %s;"
        cursor.execute(query, (r_id,))
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
        query = "select * from resource where r_id in (select r_id from request);"
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
        query = "----------------------------------------------------;"
        cursor.execute(query, (keyword,))
        result = []
        for row in cursor:
            result.append(row)
        return result