from models.user import User

def get_users():
    return [
        User(id=1, name="Alice"),
        User(id=2, name="Bob"),
    ]
