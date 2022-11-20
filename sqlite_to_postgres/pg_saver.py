import logging

from psycopg2 import errors


class PgSaver:
    def __init__(self, pg_conn=None):
        self.pg_conn = pg_conn

    def save_all(self, table_name, column, value, record):
        try:
            curs = self.pg_conn.cursor()
            sql_row = '''
                insert into content.{0} {1}
                values {2}
                on conflict (id) do nothing;
            '''.format(table_name, column, value)
            curs.executemany(sql_row, record)
            logging.info(curs.executemany(sql_row, record))

        except (Exception, errors.Error) as error:
            logging.exception(error)
            exit()



