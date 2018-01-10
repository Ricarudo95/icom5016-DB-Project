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