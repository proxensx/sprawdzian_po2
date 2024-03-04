from flask import Flask, request, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


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


class UsersResource(Resource):
    def get(self):
        users = user_service.get_all_users()
        return users

    def post(self):
        data = request.get_json()
        if all(key in data for key in ['firstName', 'lastName', 'birthYear', 'group']):
            user = user_service.create_user(data)
            return user, 200
        else:
            return jsonify({"error": "Invalid input data"}), 400


class UserResource(Resource):
    def get(self, user_id):
        user = user_service.get_user_by_id(user_id)
        if user:
            return user, 200
        else:
            return jsonify({"error": "User not found"}), 404

    def patch(self, user_id):
        data = request.get_json()
        user = user_service.update_user(user_id, data)
        if user:
            return user, 200
        else:
            return 404

    def delete(self, user_id):
        user = user_service.delete_user(user_id)
        if user:
            return user, 200
        else:
            return jsonify({"error": "User not found"}), 404


api.add_resource(UsersResource, '/users')
api.add_resource(UserResource, '/users/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)



