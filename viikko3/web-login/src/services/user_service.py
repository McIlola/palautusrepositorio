from entities.user import User
from repositories.user_repository import (
    user_repository as default_user_repository
)


class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        self.validate(username, password, password_confirmation)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password, password_confirmation):
        user = self._user_repository.find_by_username(username)
        if user:
            raise AuthenticationError("Username taken")
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username)<3 or not username.isalpha():
            raise AuthenticationError("Username too short or not only letters")
        if password != password_confirmation or len(password)<8 or password.isalpha():
            raise AuthenticationError("Passwords do not match, password too short or password has only letters")


user_service = UserService()
