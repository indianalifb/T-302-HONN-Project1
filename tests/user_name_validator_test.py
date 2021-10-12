from src.username_validator import UsernameValidator

def test_that_validator_returns_true_when_username_is_right_length():
    # arrange
    validator = UsernameValidator()

    # act
    boolean = validator.validate("Aoeu")

    # assert
    assert boolean == True

def test_that_validator_returns_false_when_username_is_too_long():
    # arrange
    validator = UsernameValidator()

    # Act
    boolean = validator.validate("aoeuihdtns;qjkxbm")

    # assert
    assert boolean == False
