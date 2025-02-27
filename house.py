import json
import os
from exceptions import UserAlreadyExists, InvalidEmailFormat, RoleInvald, UserNotFound

# Used ID
USER_ID = -1
ROOM_ID = -1
DEVICE_ID = -1
HOUSE_ID = -1

ROLE_LISTS = ["admin", "regular", "protected"]




db_location = "smart_home_data.json"

def load_data():
    if os.path.exists(db_location):
        with open(db_location, "r") as f:
            content = f.read().strip()  # Read and strip any whitespace
            if not content:  # If the file is empty
                return {"users": {}, "houses": {}, "rooms": {}, "devices": {}}
            return json.loads(content)  # Load JSON
    return {"users": {}, "houses": {}, "rooms": {}, "devices": {}}


def save_data(data):
    with open(db_location, "w") as f:
        json.dump(data, f, indent=4)


db = load_data()


# User Class
class User():
    def __init__(self, username: str, email: str, password: str, role: str):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    @classmethod
    def create(cls, username: str, email: str, password: str, role: str):
        """Creates user instance while saving it to db. Simple validation included."""
        
        # Input Validation
        if email in db["users"]:
            raise UserAlreadyExists(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)
        
        if role not in ROLE_LISTS:
            raise RoleInvald(role)
        
        
        # Saving to Database
        user = cls(username, email, password, role)
        db["users"][email] = user.__dict__
        save_data(db)
        return user
    
    @classmethod
    def read(cls, email):
        """
        Reads User Data from the Database. Only supports read from email input now. Could include read from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)

        # Read from Database
        user_data = db["users"][email]  # Fix this so that password is not returned
        return cls(**user_data)  # Returns an object


    def update(self, new_email):
        """
        Updates User Data from the Database. Only supports update from email input now. Could include update from username or others.
        Simple Input Validation Included
        """
        self.email = new_email
        db["users"][self.email] = self.__dict__
        save_data(db)
        return f"Email updated to {self.email}"


    @classmethod
    def delete(cls, email):
        """
        Deletes User Data from the Database. Only supports delete from email input now. Could include delete from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        # Deleting Object
        del db["users"][email]
        save_data(db)
        return f"User {email} deleted."


# House Class
class House():
    def __init__(self, username: str, email: str, password: str, role: str):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    @classmethod
    def create(cls, username: str, email: str, password: str, role: str):
        """Creates user instance while saving it to db. Simple validation included."""
        
        # Input Validation
        if email in db["users"]:
            raise UserAlreadyExists(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)
        
        if role not in ROLE_LISTS:
            raise RoleInvald(role)
        
        
        # Saving to Database
        user = cls(username, email, password, role)
        db["users"][email] = user.__dict__
        save_data(db)
        return user
    
    @classmethod
    def read(cls, email):
        """
        Reads User Data from the Database. Only supports read from email input now. Could include read from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)

        # Read from Database
        user_data = db["users"][email]  # Fix this so that password is not returned
        return cls(**user_data)  # Returns an object


    def update(self, new_email):
        """
        Updates User Data from the Database. Only supports update from email input now. Could include update from username or others.
        Simple Input Validation Included
        """
        self.email = new_email
        db["users"][self.email] = self.__dict__
        save_data(db)
        return f"Email updated to {self.email}"


    @classmethod
    def delete(cls, email):
        """
        Deletes User Data from the Database. Only supports delete from email input now. Could include delete from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        # Deleting Object
        del db["users"][email]
        save_data(db)
        return f"User {email} deleted."


# Room Class
class Room():
    def __init__(self, username: str, email: str, password: str, role: str):
        self.username = username
        self.email = email
        self.password = password
        self.role = role

    @classmethod
    def create(cls, username: str, email: str, password: str, role: str):
        """Creates user instance while saving it to db. Simple validation included."""
        
        # Input Validation
        if email in db["users"]:
            raise UserAlreadyExists(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)
        
        if role not in ROLE_LISTS:
            raise RoleInvald(role)
        
        
        # Saving to Database
        user = cls(username, email, password, role)
        db["users"][email] = user.__dict__
        save_data(db)
        return user
    
    @classmethod
    def read(cls, email):
        """
        Reads User Data from the Database. Only supports read from email input now. Could include read from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)

        # Read from Database
        user_data = db["users"][email]  # Fix this so that password is not returned
        return cls(**user_data)  # Returns an object


    def update(self, new_email):
        """
        Updates User Data from the Database. Only supports update from email input now. Could include update from username or others.
        Simple Input Validation Included
        """
        self.email = new_email
        db["users"][self.email] = self.__dict__
        save_data(db)
        return f"Email updated to {self.email}"


    @classmethod
    def delete(cls, email):
        """
        Deletes User Data from the Database. Only supports delete from email input now. Could include delete from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        # Deleting Object
        del db["users"][email]
        save_data(db)
        return f"User {email} deleted."

# Device Class
class Device():
    def __init__(self, name: str, in_room: Room, device_type: str):
        self.name = name
        self.device_type = device_type
        self.room = in_room

    @classmethod
    def create(cls, username: str, email: str, password: str, role: str):
        """Creates user instance while saving it to db. Simple validation included."""
        
        # Input Validation
        if email in db["users"]:
            raise UserAlreadyExists(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)
        
        if role not in ROLE_LISTS:
            raise RoleInvald(role)
        
        
        # Saving to Database
        user = cls(username, email, password, role)
        db["users"][email] = user.__dict__
        save_data(db)
        return user
    
    @classmethod
    def read(cls, email):
        """
        Reads User Data from the Database. Only supports read from email input now. Could include read from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        if "@" not in email:
            raise InvalidEmailFormat(email)

        # Read from Database
        user_data = db["users"][email]  # Fix this so that password is not returned
        return cls(**user_data)  # Returns an object


    def update(self, new_email):
        """
        Updates User Data from the Database. Only supports update from email input now. Could include update from username or others.
        Simple Input Validation Included
        """
        self.email = new_email
        db["users"][self.email] = self.__dict__
        save_data(db)
        return f"Email updated to {self.email}"


    @classmethod
    def delete(cls, email):
        """
        Deletes User Data from the Database. Only supports delete from email input now. Could include delete from username or others.
        Simple Input Validation Included
        """

        # Input Validation
        if email not in db["users"]:
            raise UserNotFound(email)
        
        # Deleting Object
        del db["users"][email]
        save_data(db)
        return f"User {email} deleted."






