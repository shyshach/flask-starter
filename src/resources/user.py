from flask import request, jsonify
from flask_restful import Resource

from repositories import UserRepository


class User(Resource):
    def get(self, username: str):
        user = UserRepository.get(username)
        return user, 200


class UserList(Resource):

    def post(self):
        """Create user."""
        request_json = request.get_json(silent=True)
        username: str = request_json['username']
        avatar_url: str = request_json.get('avatar_url', '')
        password: str = request_json.get('password', 'None')
        try:
            user = UserRepository.create(username, avatar_url, password)
            return user, 200
        except Exception as e:
            response = jsonify(e.to_dict())
            response.status_code = e.status_code
            return response

    def get(self):
        """ Get users list."""
        users_query = UserRepository.all()
        if len(users_query):
            users = []
            for user in users_query:
                users.append(
                    {
                        'username': user.username,
                        'avatar': user.avatar_url,
                        'created': str(user.date_created)

                    }
                )
        else:
            users = {}
        return users, 200
