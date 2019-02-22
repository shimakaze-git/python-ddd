# package usecase
from usecase.user_repository import IFUserRepository
from domain.user import User

# import "app/domain"

# type UserInteractor struct {
# 	UserRepository UserRepository
# }

# func (interactor *UserInteractor) Add(u domain.User) (user domain.User, err error) {
# 	identifier, err := interactor.UserRepository.Store(u)
# 	if err != nil {
# 		return
# 	}
# 	user, err = interactor.UserRepository.FindById(identifier)
# 	return
# }

# func (interactor *UserInteractor) Users() (user domain.Users, err error) {
# 	user, err = interactor.UserRepository.FindAll()
# 	return
# }

# func (interactor *UserInteractor) UserById(identifier int) (user domain.User, err error) {
# 	user, err = interactor.UserRepository.FindById(identifier)
# 	return
# }

class UserInteractor:
    def __init__(self, user_repository: IFUserRepository):
        self._user_repository = user_repository

    def add(self, user: User)->User:
        identifier, err = self._user_repository.store(user)
        if err != None:
            return
        user, err = self._user_repository.find_by_id(identifier)
        return user

    def users(self)->list:
        users = self._user_repository.find_all()
        return users

    def user_by_id(self, identifier: int):
        user, err = self._user_repository.find_by_id(identifier)
        return user
