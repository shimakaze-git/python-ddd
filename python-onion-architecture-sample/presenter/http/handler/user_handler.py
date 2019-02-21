# package handler

# import (
# 	"context"
# 	"net/http"
# 	"strconv"

# 	"github.com/nanamen/go-echo-rest-sample/domain/model"
# 	"github.com/nanamen/go-echo-rest-sample/usecase"
# 	"github.com/labstack/echo"
# )

# // UserHandler interface
# type UserHandler interface {
# 	GetUsers(c echo.Context) error
# 	GetUser(c echo.Context) error
# 	CreateUser(c echo.Context) error
# 	UpdateUser(c echo.Context) error
# 	DeleteUser(c echo.Context) error
# }

# type userHandler struct {
# 	UserUseCase usecase.UserUseCase
# }

# // NewUserHandler UserHandlerを取得します.
# func NewUserHandler(u usecase.UserUseCase) UserHandler {
# 	return &userHandler{u}
# }

# func (h *userHandler) GetUsers(c echo.Context) error {
# 	ctx := c.Request().Context()
# 	if ctx == nil {
# 		ctx = context.Background()
# 	}

# 	users, err := h.UserUseCase.GetUsers(ctx)
# 	if err != nil {
# 		return echo.NewHTTPError(http.StatusNotFound, "Users does not exist.")
# 	}

# 	return c.JSON(http.StatusOK, users)
# }

# func (h *userHandler) GetUser(c echo.Context) error {
# 	id, err := strconv.Atoi(c.Param("id"))
# 	if err != nil {
# 		return echo.NewHTTPError(http.StatusBadRequest, "User ID must be int")
# 	}

# 	ctx := c.Request().Context()
# 	if ctx == nil {
# 		ctx = context.Background()
# 	}

# 	user, err := h.UserUseCase.GetUser(ctx, id)
# 	if err != nil {
# 		return echo.NewHTTPError(http.StatusNotFound, "User does not exist.")
# 	}

# 	return c.JSON(http.StatusOK, user)
# }


import json
import falcon

class AppResource:

    def __init__(self, test):
        self.test = test

    def on_get(self, req, resp):
        print(self.test)

        msg = {
            "message": "Welcome to the Falcon"
        }
        resp.body = json.dumps(msg)

app = falcon.API()
app.add_route("/", AppResource(100))


if __name__ == "__main__":
    from wsgiref import simple_server
    httpd = simple_server.make_server("127.0.0.1", 8000, app)
    httpd.serve_forever()