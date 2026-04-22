import re

def check_password_strength(password):
    score = 0

    # 1. Length check
    if len(password) >= 8:
        score += 1
    else:
        print(" Password is short")

    # 2. Lowercase check
    if re.search(r"[a-z]", password):
        score += 1
    else:
        print("no small letters")

    # 3. Uppercase check
    if re.search(r"[A-Z]", password):
        score += 1
    else:
        print("no capital letters")

    # 4. Numbers check
    if re.search(r"[0-9]", password):
        score += 1
    else:
        print("no numbers")

    # 5. Special characters check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        print("No special characters")

    # RESULT
    print("\n--- RESULT ---")

    if score == 5:
        print(" Strong Password")
    elif score >= 3:
        print("Medium Password ")
    else:
        print("Weak Password ")


# MAIN PROGRAM
password = input("Enter your password: ")
check_password_strength(password)