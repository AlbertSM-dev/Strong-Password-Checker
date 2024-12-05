def StrongPasswordChecker(password):
    if len(password) < 6:
        return False

    hasLowercase = False
    hasUppercase = False
    hasDigit = False
    hasSpecialChar = False
    specialChars = "!@#$%^&*()-+"

    for i in range(len(password)):
        if password[i].islower():
            hasLowercase = True
        elif password[i].isupper():
            hasUppercase = True
        elif password[i].isdigit():
            hasDigit = True
        elif password[i] in specialChars:
            hasSpecialChar = True

        if i > 0 and password[i] == password[i - 1]:
            return False

    if hasLowercase and hasUppercase and hasDigit and hasSpecialChar:
        return True
    else:
        return False


def main():
    password = None

    print("Enter password: ")
    password = input()

    if password:
        if StrongPasswordChecker(password):
            print("Password is strong")
        else:
            print("Password is not strong")
    else:
        print("Password is empty")


if __name__ == "__main__":
    main()
