import sqlite3 as sq
import os 
# import json

db_name = 'TESTS'

class DB_ORM:
    def __init__(self):
        self.__connect(db_name)
    
    def __connect(self, db_name):
        os.mkdir('DBs') if not os.path.exists('DBs') else ...

        self.connection = sq.connect(f"DBs/{db_name}.db")
        self.cursor = self.connection.cursor()

        self.execute('''CREATE TABLE IF NOT EXISTS CARGOS_STORED (
                        id INTEGER UNIQUE,
                        weight REAL,
                        long_width_height TEXT,
                        fragile INTEGER
                    );
            ''', is_change=False)


    def execute(self, query : str, is_change : bool, **values) -> list:
        if self.connection_check():

            if values:
                if list(values.keys())[0] == 'values':
                    self.cursor.execute(query, values['values'])
            else:
                self.cursor.execute(query)
            
            if is_change:
                self.connection.commit()
                return True
            
            else:
                return self.cursor.fetchall()
            
        else:
            print('Have no connection to database')

    

    def get_unique(self, table_name : str, column_name : str) -> list:
        if self.connection_check():
            return([j for j in [i[0] for i in self.execute(f'''
                SELECT DISTINCT {column_name} 
                    FROM {table_name};
            ''', 
                is_change = False)]])

        else:
            print('Have no connection to database')

    
    def columns_names(self, table_name : str) -> list:
        return([name[1] for name in self.execute(f'''PRAGMA table_info({table_name});''', is_change = False)])



    def connection_check(self):
        try:
            self.cursor.execute('SELECT 1;')
            return True

        except Exception:
            return False


    def connection_close(self):
        self.connection.close()