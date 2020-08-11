import psycopg2

class A():

    def get_connection(self):
        connection = psycopg2.connect(dbname='conifer_production', host='10.52.124.40',
                                        port='5432',
                                        user='indata',
                                        password='qa_staging')
        print('conn = %s' % connection)
        return connection

    def close_connection(connection):
        if connection:
            connection.close()

    def read_database_version(self):
        try:
            connection = self.get_connection()
            cursor = connection.cursor()
            cursor.execute("SELECT version();")
            db_version = cursor.fetchone()
            print("You are connected to PostgreSQL version: ", db_version)
            self.close_connection(connection)
        except (Exception, psycopg2.Error) as error:
            print("Error while getting data", error)

a=A()
a.read_database_version()