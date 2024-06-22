from user import *
from post import *


def main():
    user1 = User('Sujan', 'Campsie', 'email@email.com', 'password', 'Software Developer')
    user1.get_user_info()

    user2 = User('Thapa', 'Campsie', 't@email.com', 'password', 'Software Developer')
    user2.get_user_info()

    new_post = Post('Learning Python Today!!!', user1.name)
    new_post.get_post_info()


main()
