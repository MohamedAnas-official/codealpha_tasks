import hashlib

users = {
    "admin": hashlib.sha256("admin123".encode()).hexdigest(),
    "user": hashlib.sha256("password".encode()).hexdigest()
}

username = input("Username: ").strip()
password = input("Password: ").strip()

hashed_password = hashlib.sha256(password.encode()).hexdigest()

if username in users:
    if users[username] == hashed_password:
        print("Login Successful")
    else:
        print("Invalid Password")
else:
    print("User Not Found")
