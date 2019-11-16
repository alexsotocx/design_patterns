from http_adapter import HttpAdapter
from tcp_adapter import TcpAdapter


class NetworkConnectorAdapter:
    @staticmethod
    def create(connector_type):
        if connector_type == "HTTP":
            return HttpAdapter(NetworkConnectorAdapter.__env_url())
        if connector_type == "TCP":
            return TcpAdapter("3000", "localhost")
        return None

    @staticmethod
    def __env_url():
        return "http://my.service.com/"
