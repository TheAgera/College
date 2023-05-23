common_passwords = ["123456", "123456789", "qwerty", "password", "12345", "qwerty123", "1q2w3e", "12345678", "111111", "1234567890"]

user_password = input("Enter a password: ")

while user_password in common_passwords:
    print("Password is common. Please choose a different one.")
    user_password = input("Enter a different password: ")
else:
    print("You have chosen a secure password.")

