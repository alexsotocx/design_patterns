class HTTPClient:
    def get(self, path, headers):
        raise NotImplementedError()

    def __build_url(self, path):
        return self.base_url + path

