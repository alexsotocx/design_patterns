class TcpAdapter:
    def __init__(self, port, ip):
        self.port = port
        self.ip = ip

    def connect(self):
        self.__hand_shake()
        self.__ping()
        print("Connected!")

    def __ping(self):
        print("Ping ip {ip}".format(ip=self.ip))
        print("response in 1ms")

    def __hand_shake(self):
        print("Handshaking at port {port} in the IP {ip}".format(
            port=self.port, ip=self.ip))
