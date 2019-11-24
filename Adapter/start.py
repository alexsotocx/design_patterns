from repository import Repository
from sqlrepository import SQLRepository
from localrepository import LocalStorageAdapter, LocalStorage


def test(client: Repository):
    client.save("1", "Alex")
    print(client.find("1"))
    client.save("2", "bot")
    print(client.findAll())


sqlClient = SQLRepository("psql://user:pass@localhost:5632/db", "user")
localstorageAdapter = LocalStorageAdapter(
    LocalStorage('/tmp/py_storeage.data'))


test(sqlClient)
test(localstorageAdapter)
