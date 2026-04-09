from db import get_user_by_email

# BUG #2: No null check — crashes if user not found
def login(email, password):
    user = get_user_by_email(email)
    role = user.role          # <-- AttributeError if user is None!
    if check_password(user, password):
        return {"token": generate_token(user), "role": role}
    return {"error": "invalid password"}

def get_user_role(user):
    return user.role          # same pattern — no guard

def check_password(user, password):
    return user.password_hash == hash(password)