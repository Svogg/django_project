import logging
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
            dt = self.curs.fetchmany(500)
            return [data_cls(**dict(query)) for query in dt]
        except (Exception, sqlite3.Error) as error:
            logging.exception(error)
            exit()

    def __exit__(self, error: Exception, value: object, traceback: object):
        self.conn.commit()
        self.curs.close()
        self.conn.close()

