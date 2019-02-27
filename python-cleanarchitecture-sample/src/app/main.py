from interfaces.database.user_repository import UserRepository

def main():
    repo = UserRepository()
    print(repo)
    # print(UserRepository)


if __name__ == '__main__':
    main()
