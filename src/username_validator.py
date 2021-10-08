from Repository.user_name_repository import UserNameRepository

class UsernameValidator:
    def validate(self, username: str) -> bool:
        pass
    # TODO: Validate-a að nafnið er i gagnagrunninum

        validate_username = UserNameRepository.get_username(username)
        if validate_username == None:
            return False
        else:
            return True



