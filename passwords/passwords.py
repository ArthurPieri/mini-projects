"""
This module contains simple functions related to passwords.
"""
import random
import string


def is_good_password(password: str) -> bool:
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


def random_password_generator(
    password_size: int,
    use_upper: bool,
    use_numbers: bool,
    use_specials: bool
) -> str:
    '''
    Generates a random password
    '''
    password = ''

    if use_upper:
        password += string.ascii_uppercase
    if use_numbers:
        password += string.digits
    if use_specials:
        password += '!@#$%ˆ&*()_+-=\\|/.,<>?;:[]{}'

    password += string.ascii_lowercase

    return ''.join(random.choice(password) for _ in range(password_size))


def passphrase_generator(word_count: int) -> str:
    ...
    # TODO: Implement this function
    # by scrapping the web for a list of random words


if __name__ == '__main__':
    print(random_password_generator(12, True, True, True))
