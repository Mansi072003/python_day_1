def check_password_strength(password):

    length = len(password) >= 8
    has_digit = any(char.isdigit() for char in password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_special = any(char in "!@#$%^&*(),.?\":{}|<>" for char in password)

    if length and has_digit and has_upper and has_lower and has_special:
        return "Strong"
    elif length and (has_digit or has_upper or has_special):
        return "Medium"
    else:
        return "Weak"

while True:
    password = input("Enter a password: ")
    strength = check_password_strength(password)

    print(f"Password Strength: {strength}")

    if strength == "Strong":
        print("Strong password accepted!")
        break
    else:
        print("Please enter a stronger password.\n")
