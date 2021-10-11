'''used to validate that username is not longer than 15 letters'''
class UsernameValidator:
    def validate(self, username: str) -> bool:
        return len(username) < 15
