from repository import Repository


class SQLRepository(Repository):

    def __init__(self, url, table):
        self.url = url
        self.table = table
        self.data = {}

    def find(self, id):
        self.__connect()
        print(
            "SELECT * FROM {table} WHERE id = '{id}';".format(id=id, table=self.table))
        return self.data[id]

    def findAll(self):
        self.__connect()
        print(
            "SELECT * FROM {table};".format(table=self.table))
        return list(map(lambda x: self.data[x], self.data.keys()))

    def save(self, id, name):
        self.__connect()
        print("INSERT INTO {table} (id, name) VALUES ('{id}', '{name}')".format(
            table=self.table, id=id, name=name))
        self.data[id] = {
            id: id,
            name: name
        }

        return self.data[id]

    def __connect(self):
        print("Connecting to {url}".format(url=self.url))
