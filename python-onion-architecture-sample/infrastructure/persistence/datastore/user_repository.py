from domain.model.user_model import User
from domain.repository.user_repository import IFUserRepository




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
def new_user_repository(session)->IFUserRepository:
    # user_repository = UserRepository(conn)
    user_repository = UserRepository(session)
    return user_repository


class UserRepository(IFUserRepository):
    def __init__(self, conn):
        self.conn = conn
        # self.connは使用しないかもしれない

    def fetch(self)->list:

        # users = self.conn.query(User).\
        #             order_by(desc(User.id)).\
        #             all()
        # return users

        # users = session.query(User).\
        # filter(User.name=="tomo").\
        # all()

        # user_tomo = session.query(User).\
        #     filter(User.id==1).\
        #     first()

        pass

    def fetch_by_id(self, id: int)->User:
        pass

    def create(self)->User:
        pass

    def update(self)->User:
        pass

    def delete(self):
        pass
