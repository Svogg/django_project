class SqliteExtractor:
    def __init__(self, connection):
        self.connection = connection

    def extract(self, data_class, table_name: str, batch_size: int = 100):
        curs = self.connection.cursor()
        curs.execute(f'select * from {table_name};')

        while True:
            data = curs.fetchmany(batch_size)
            if not data:
                break
            records = []
            for record in data:
                records.append(data_class(**record))
            yield records
