import os
from dotenv import load_dotenv

load_dotenv()

users = {
    "admin": {
        "login": os.getenv("ADMIN_LOGIN"),
        "password": os.getenv("ADMIN_PASSWORD")
    },
    "manager": {
        "login": os.getenv("MANAGER_LOGIN"),
        "password": os.getenv("MANAGER_PASSWORD")
    }
}

def get_user_creds_by_role(role):
    login = users[role]["login"]
    password = users[role]["password"]
    return login, password