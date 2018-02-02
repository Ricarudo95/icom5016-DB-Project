from dbconfig import pg_config
import psycopg2

class SupplierDAO:
    
    def __init__(self):
        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                           pg_config['user'],
                                                          pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result

    def getResourcesBySupplier(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from resource where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierResourceSold(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from resource where  s_id = %s and r_id in (select r_id from stransaction where status = 'Completed') "
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierTransactions(self, s_id):
        cursor = self.conn.cursor()
        query = "select * from stransaction where r_id in (select r_id from resource where s_id = %s) "
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def addSupplier(self, s_name, s_pass, s_loc):
        cursor = self.conn.cursor()
        address_query = "insert into supplieraddress (location_name, region, city, zip_code) values (null,null,null,null) returning sa_id"
        cursor.execute(address_query, )
        sa_id = cursor.fetchone()[0]
        query = "insert into supplier(sname, pass, loc, sa_id) values ( %s, %s, %s, %s ) returning s_id"
        cursor.execute(query, (s_name,s_pass,s_loc,sa_id))
        s_id = cursor.fetchone()[0]
        
        self.conn.commit()
        return s_id
