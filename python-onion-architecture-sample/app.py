from presenter.http.handler.user_handler import UserHandlerResource
from usecase.user_usecase import new_user_usecase
# from 
from infrastructure.persistence.datastore.inmemory.user_repository import new_user_repository
# new_user_repository

# import json
import falcon

# class AppResource(object):

#     def __init__(self, responder):
#         self.responder = responder

#     def on_get(self, req, resp):

#         print(self.responder)
#         msg = {
#             "message": "Welcome to the Falcon"
#         }
#         resp.body = json.dumps(msg)

user_repository = new_user_repository()
user_usecase = new_user_usecase(user_repository)

app = falcon.API()
user_handler_resource = UserHandlerResource(user_usecase)
# app_resource = AppResource(object)

# # print(AppResource())
# # print(app_resource)

app.add_route('/', user_handler_resource)
# HEAD, POST

app.add_route('/{user_id}', user_handler_resource)
# GET, PUT, DELETE

if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()
