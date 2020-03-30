from api_gateway import ApiGateway
from user_get_endpoint import UserEndpoint
from user_remove_endpoint import UserRemoveEndpoint
from client import Client

api_gateway = ApiGateway()
userRepo = ['a', 'b', 'c']
api_gateway.add_endpoint(UserEndpoint(userRepo))
api_gateway.add_endpoint(UserRemoveEndpoint(userRepo))

client = Client(api_gateway)
print(client.request('GET', '/users', None))
print(client.request('DELETE', '/users', {'id': 'b'}))
print(client.request('GET', '/users', None))
