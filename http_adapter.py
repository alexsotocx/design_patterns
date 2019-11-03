class HttpAdapter:
    def __init__(self, root_url):
        self.root_url = root_url
    
    
    def connect(self):
        self.__handshake()
        print("Connected to {url}".format(url=self.root_url))
        
    def __handshake(self):
        print("Handshaking with url {url}".format(url=self.root_url))
        
        
        
