def Access_check(roles: list[str]):
    def decorator(fn: callable) -> callable:
        def wrapper(*args, **kwargs):
            user = kwargs.get("user")
            if not user:
                raise ValueError("User not found!")
            if user.role not in roles:
                raise PermissionError(f"Access denied. Needed role: {roles}")
            return fn(*args, **kwargs)
        return wrapper
    return decorator