from http_adapter import HttpAdapter

class NetworkConnectorAdapter:
    def create(connector_type):
        if connector_type == "HTTP":
            return HttpAdapter(NetworkConnectorAdapter.__env_url)
            
    def __env_url():
        return "http://my.service.com/"
