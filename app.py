from flask import Flask

app = Flask(__name__)


class UserService:
    def __init__(self):
        self.users = []
        self.id_counter = 1

    def get_all_users(self):
        return self.users

    def get_user_by_id(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                return user
        return None

    def create_user(self, data):
        user = {
            "id": self.id_counter,
            "firstName": data['firstName'],
            "lastName": data['lastName'],
            "age": 2024 - data['birthYear'],
            "group": data['group']
        }
        self.users.append(user)
        self.id_counter += 1
        return user

    def update_user(self, user_id, data):
        for user in self.users:
            if user['id'] == user_id:
                user['firstName'] = data.get('firstName', user['firstName'])
                user['lastName'] = data.get('lastName', user['lastName'])
                user['group'] = data.get('group', user['group'])
                return user
        return None

    def delete_user(self, user_id):
        for user in self.users:
            if user['id'] == user_id:
                self.users.remove(user)
                return user
        return None


user_service = UserService()