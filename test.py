from house import User

def test_user_create():
    user_1 = User("abc", "hanks911008@gmail.com", "AJ@dheuai", "admin").create()


user_1 = User.delete("joshua@example.com")