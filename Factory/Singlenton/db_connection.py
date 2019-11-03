class DatabaseConnection:
    __singleton = None

    @staticmethod
    def create():
        if DatabaseConnection.__singleton == None:
            DatabaseConnection.__singleton == DatabaseConnection.__create()
        return DatabaseConnection.__singleton

    @staticmethod
    def __create():
        connection = DatabaseConnection()
        connection.port = 5432
        connection.ip = 'localhost'
        connection.database = 'database'
        return connection

    def connect(self):
        print("Connected to Databa at {ip}:{port}".format(
            ip=self.ip, port=self.port))
