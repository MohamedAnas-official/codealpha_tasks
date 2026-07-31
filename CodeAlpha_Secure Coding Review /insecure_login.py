users = {
    "admin": "admin123",
    "user": "password"
}

username = input("Username: ")
password = input("Password: ")

if username in users and users[username] == password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
