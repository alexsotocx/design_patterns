from api_gateway import ApiGateway
from user_get_endpoint import UserEndpoint
from user_remove_endpoint import UserRemoveEndpoint

api_gateway = ApiGateway()
userRepo = ['a', 'b', 'c']
api_gateway.add_endpoint(UserEndpoint(userRepo))
api_gateway.add_endpoint(UserRemoveEndpoint(userRepo))
print(api_gateway.process_request('GET', '/users', None))
print(api_gateway.process_request('DELETE', '/users', {'id': 'b'}))
print(api_gateway.process_request('GET', '/users', None))
