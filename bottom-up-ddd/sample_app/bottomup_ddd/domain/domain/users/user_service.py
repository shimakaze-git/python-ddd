
# namespace Domain.Domain.Users {
#     public class UserService {
#         private readonly IUserRepository userRepository;

#         public UserService(IUserRepository userRepository) {
#             this.userRepository = userRepository;
#         }

#         public bool IsDuplicated(User user) {
#             var name = user.UserName;
#             var searched = userRepository.Find(name);

#             return searched != null;
#         }
#     }
# }

class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def is_duplicated(self, user):
        name = user.user_name
        searched = self._user_repository.find(name)

        return searched != None