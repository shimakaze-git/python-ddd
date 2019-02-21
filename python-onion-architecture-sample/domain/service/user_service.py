# package service

# import (
# 	"context"

# 	"github.com/nanamen/go-echo-rest-sample/domain/repository"
# )

# // UserService ドメインサービスとして利用し,複数のエンティティやレポジトリを扱う処理をここで実装する.
# // ※ ドメインサービスはアプリケーションサービスではないのでトランザクションの境界などは持たない.
# // ※ なんでもドメインサービスで実装するとドメインモデル貧血症となるので気をつける(ドメインモデルで表現できないかよくよく検討すること).
# type UserService interface {
# 	DoSomething(ctx context.Context, foo int) error
# }

# type userService struct {
# 	repository.UserRepository
# }

# // NewUserService UserServiceを取得します.
# func NewUserService(r repository.UserRepository) UserService {
# 	return &userService{r}
# }

# func (u *userService) DoSomething(ctx context.Context, foo int) error {
# 	// some code
# 	return nil
# }

from abc import ABCMeta, abstractmethod
from domain.repository.user_repository import IFUserRepository


class IFUserService(metaclass=ABCMeta):

    @abstractmethod
    def do_something(self, foo: int)->None:
        pass




def new_user_service(repository: IFUserRepository):
    user_service = UserService(repository)
    return user_service

class UserService(IFUserService):
    def __init__(self, user_repository: IFUserRepository):
        self.user_repository = user_repository

    def do_something(self, foo: int)->None:
        
        return None