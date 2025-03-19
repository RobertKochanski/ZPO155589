def validate(fn: callable) -> callable:
    def wrapper(**kwargs):
        for key, value in kwargs.items():
            if not value:
                return f"{key} cannot be empty"
            if key == "password" and len(value) <= 5:
                return f"{key} must be longer than 5 characters"
        return fn(**kwargs)
    return wrapper


@validate
def check_validate(username:str, password:str) -> str:
    return f"Your username: {username} and password: {password}"


print(check_validate(username="username", password="short"))