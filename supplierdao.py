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

    def getSupplierResourceSold(self, sid):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id in (select r_id from stransaction;) and s_id=%s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
