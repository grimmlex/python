def is_acceptable_password(password):
    strip = password.split()
    if len(password) <= 6:
        return False
    elif len(strip) > 1:
        return False
    elif not password.isalpha():
        return True
    else:
        return False


print(is_acceptable_password("muchlonger"))
