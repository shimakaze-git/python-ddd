# package domain

# import "fmt"

# type Users []User

# type User struct {
# 	ID        int
# 	FirstName string
# 	LastName  string
# 	FullName  string
# }

# func (u *User) Build() *User {
# 	u.FullName = fmt.Sprintf("%s %s", u.FirstName, u.LastName)
# 	return u
# }

class User:
    def __init__(self, first_name: str, last_name: str):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__full_name = None

    def build(self):
        self.__full_name = self.__first_name + " " + self.__last_name
        return self
