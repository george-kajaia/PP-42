def require_role(allowed_role="admin"):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if allowed_role == "admin":
                func(*args, **kwargs)
            else:
                print("Permission Denied: User is not an admin")
        return wrapper
    return decorator

@require_role("admin")
def admin_func():
    print("Function executed successfully.")

admin_func()

@require_role("user")
def user_func():
    print("Function executed successfully.")

user_func()
