ROLE_LISTS = ["admin", "regular", "protected"]

# Create Exceptions
class UserAlreadyExists(Exception):
    def __init__(self, email):
        super().__init__(f"User with email '{email}' already exists.")
        self.email = email

class RoleInvald(Exception):
    def __init__(self, role):
        super().__init__(f"Invalid Input: Role '{role}' does not exist. Valid roles include {ROLE_LISTS}.")

class InvalidEmailFormat(Exception):
    def __init__(self, email):
        super().__init__(f"Invalid email format: '{email}'.")
        self.email = email



# Read Exceptions
class UserNotFound(Exception):
    def __init__(self, email):
        super().__init__(f"User with email '{email}' does not exist.")
        self.email = email