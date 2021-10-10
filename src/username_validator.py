
class UsernameValidator:
    def validate(self, username: str) -> bool:
        return len(username) < 15
