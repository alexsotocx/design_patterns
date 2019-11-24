import json
from repository import Repository


class LocalStorage:
    def __init__(self, localPath):
        self.localPath = localPath

    def write(self, data):
        print("Opening file {file} for writing".format(file=self.localPath))
        file = open(self.localPath, "a")
        file.write("{json}\n".format(json=json.dumps(data)))
        file.close()
        return data

    def read(self):
        print("Opening file {file} for reading".format(file=self.localPath))
        file = open(self.localPath, "r")
        lines = file.readlines()
        file.close()
        return lines


class LocalStorageAdapter(Repository):
    def __init__(self, localstorage: LocalStorage):
        self.localstorage = localstorage

    def find(self, id):
        lines = self.localstorage.read()
        match = list(
            filter(lambda x: LocalStorageAdapter.__parse_line(x).get("id", None)== id, lines))
        if len(match) > 0:
            return match[0]
        return None

    def findAll(self):
        lines = self.localstorage.read()
        return list(map(lambda l: LocalStorageAdapter.__parse_line(l), lines))

    def save(self, id, name):
        data = {
            id: id,
            name: name
        }
        self.localstorage.write(data)
        return data

    @staticmethod
    def __parse_line(line: str):
        print("Parsing {line}".format(line=line))
        return dict(json.loads(line))
