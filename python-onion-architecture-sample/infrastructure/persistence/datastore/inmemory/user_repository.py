from domain.model.user_model import User
from domain.repository.user_repository import IFUserRepository

from datetime import datetime

# package datastore

# import (
# 	"context"

# 	"github.com/nanamen/go-echo-rest-sample/domain/model"
# 	"github.com/nanamen/go-echo-rest-sample/domain/repository"
# 	"github.com/jinzhu/gorm"
# )

# type userRepository struct {
# 	Conn *gorm.DB
# }

# // NewUserRepository UserRepositoryを取得します.
# func NewUserRepository(Conn *gorm.DB) repository.UserRepository {
# 	return &userRepository{Conn}
# }

# func (r *userRepository) Fetch(ctx context.Context) ([]*model.User, error) {
# 	var (
# 		users []*model.User
# 		err   error
# 	)
# 	err = r.Conn.Order("id desc").Find(&users).Error
# 	return users, err
# }

# func (r *userRepository) FetchByID(ctx context.Context, id int) (*model.User, error) {
# 	u := &model.User{ID: id}
# 	err := r.Conn.First(u).Error
# 	return u, err
# }

# func (r *userRepository) Create(ctx context.Context, u *model.User) (*model.User, error) {
# 	err := r.Conn.Create(u).Error
# 	return u, err
# }

# func (r *userRepository) Update(ctx context.Context, u *model.User) (*model.User, error) {
# 	err := r.Conn.Model(u).Update(u).Error
# 	return u, err
# }

# func (r *userRepository) Delete(ctx context.Context, id int) error {
# 	u := &model.User{ID: id}
# 	err := r.Conn.Delete(u).Error
# 	return err
# }

# def new_user_repository(conn)->IFUserRepository:
# def new_user_repository(session)->IFUserRepository:
def new_user_repository()->IFUserRepository:
    # user_repository = UserRepository(conn)
    # user_repository = InMemoryUserRepository(session)
    user_repository = InMemoryUserRepository()
    return user_repository


class InMemoryUserRepository(IFUserRepository):

    users_list = [
        {
            'id': 1,
            'name': 'name_sample',
            'created_at': datetime.now().date(),
            'updated_at': datetime.now().date()
        },
        {
            'id': 2,
            'name': 'name_white',
            'created_at': datetime.now().date(),
            'updated_at': datetime.now().date()
        },
        {
            'id': 3,
            'name': 'name_alchemy',
            'created_at': datetime.now().date(),
            'updated_at': datetime.now().date()
        }
    ]

    # def __init__(self, conn):
    def __init__(self):
        # self.conn = conn
        pass

    def fetch(self)->list:

        users_entity_list = []
        for user_dic in self.users_list:

            user_dic['created_at'].strftime('%Y-%m-%d')
            user_entity = User(
                user_dic['id'],
                user_dic['name'],
                user_dic['created_at'].strftime('%Y-%m-%d'),
                user_dic['updated_at'].strftime('%Y-%m-%d')
            )
            users_entity_list.append(user_entity)

        return users_entity_list

    def fetch_by_id(self, identify: int)->User:
        user_entity = None
        for user_dic in self.users_list:
            if user_dic['id'] == identify:
                user_entity = User(
                    user_dic['id'],
                    user_dic['name'],
                    user_dic['created_at'].strftime('%Y-%m-%d'),
                    user_dic['updated_at'].strftime('%Y-%m-%d')
                )
                break
        return user_entity

    def create(self, user: User)->User:

        # str -> date
        created_at = datetime.datetime.strptime(
            user.created_at, '%Y-%m-%d'
        )
        updated_at = datetime.datetime.strptime(
            user.updated_at, '%Y-%m-%d'
        )

        user_dic = {
            'id': user.id,
            'name': user.name,
            'created_at': created_at,
            'updated_at': updated_at
        }
        self.users_list.append(
            user_dic
        )

    def update(self, user: User)->User:
        user_entity = None

        for user_dic in self.users_list:
            if user_dic['id'] == id:
                user_dic['id'] = user.id
                user_dic['name'] = user.name

                # str -> date
                created_at = datetime.datetime.strptime(
                    user.created_at, '%Y-%m-%d'
                )
                updated_at = datetime.datetime.strptime(
                    user.updated_at, '%Y-%m-%d'
                )

                user_dic['created_at'] = created_at
                user_dic['updated_at'] = updated_at
                break
        return user

    def delete(self, identify: int):
        for inc, user_dic in enumerate(self.users_list):
            if user_dic['id'] == identify:
                self.users_list.pop(inc)
                break
        return None
        # return user
