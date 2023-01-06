def pass_validator(password: str) -> bool:
    '''
    Validates a password to make sure it meets the following criteria:
    - At least 12 characters long
    - Contains at least one number
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one special character
    '''
    if len(password) < 12:
        raise Exception('Password must be at least 12 characters long')

    if not any(char.isdigit() for char in password):
        raise Exception('Password must contain at least one number')

    if not any(char.isupper() for char in password):
        raise Exception('Password must contain at least one uppercase letter')

    if not any(char.islower() for char in password):
        raise Exception('Password must contain at least one lowercase letter')

    if not any(char in '!@#$%ˆ&*()_+-=' for char in password):
        raise Exception('Password must contain at least one special character')

    return True
