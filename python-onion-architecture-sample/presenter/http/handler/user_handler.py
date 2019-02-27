#!/usr/bin/env python
# -*- coding: utf-8 -*-
from abc import ABCMeta, abstractmethod
from domain.model.user_model import User

import json
import falcon


class IFUserHandlerResource(metaclass=ABCMeta):

    @abstractmethod
    def on_get(self, req, resp):
        pass

    @abstractmethod
    def on_post(self, req, resp):
        pass

    @abstractmethod
    def on_put(self, req, resp):
        pass

    @abstractmethod
    def on_delete(self, req, resp):
        pass


def new_user_handler(usecase):
    user_handler = UserHandlerResource(usecase)
    return user_handler


class UserHandlerResource(IFUserHandlerResource):

    def __init__(self, user_usecase):
        self._user_usecase = user_usecase

    def on_get(self, req, resp, **kwargs):
        try:
            if 'user_id' in kwargs:
                user_id = int(kwargs['user_id'])
                users = self._user_usecase.get_user(id=user_id)
                serialize_users = users.to_json()
            else:
                params = req.params
                users = self._user_usecase.get_users()
                serialize_users = [user.to_json() for user in users]
                # raise ZeroDivisionError
        except Exception as e:
            print(e)
            body = {'error': 'Users does not exist.'}
            status = falcon.HTTP_404
        else:
            body = serialize_users
            status = falcon.HTTP_200

        resp.status = status
        resp.body = json.dumps(body)

    def on_post(self, req, resp):
        # user = User()
        # pass

        req_body = req.stream.read()
        if not req_body:
            raise falcon.HTTPBadRequest('Empty request body')

        
        print(req_body)

            # user_dic['created_at'].strftime('%Y-%m-%d')
            # user_entity = User(
            #     user_dic['id'],
            #     user_dic['name'],
            #     user_dic['created_at'].strftime('%Y-%m-%d'),
            #     user_dic['updated_at'].strftime('%Y-%m-%d')
            # )
            # users_entity_list.append(user_entity)

    def on_put(self, req, resp, **kwargs):
        pass

    def on_delete(self, req, resp, **kwargs):
        pass

# func (h *userHandler) CreateUser(c echo.Context) error {
# 	user := &model.User{}
# 	if err := c.Bind(user); err != nil {
# 		return err
# 	}

# 	ctx := c.Request().Context()
# 	if ctx == nil {
# 		ctx = context.Background()
# 	}

# 	user, err := h.UserUseCase.CreateUser(ctx, user)
# 	if err != nil {
# 		return echo.NewHTTPError(http.StatusInternalServerError, "User can not Create.")
# 	}

# 	return c.JSON(http.StatusCreated, user)
# }