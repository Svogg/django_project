import sqlite3


class SqliteExtractor:
    def __init__(self, conn=None, curs=None):
        self.conn = conn
        self.curs = curs

    def extract_all(self, table_name: str, column: str, data_cls) -> list:
        try:
            self.curs.execute('''
                select {0} from {1}
                order by id;
            '''.format(column, table_name))
            dt = self.curs.fetchall()
            return [data_cls(**dict(query)) for query in dt]
        except (Exception, sqlite3.Error) as error:
            print('{0}\nextraction stopped'.format(error))
            exit()

