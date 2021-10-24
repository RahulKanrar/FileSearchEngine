import re


def validateEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if (re.fullmatch(regex, email)):
        print("Valid Email")


def validatePasswd(password):
    SpecialSymbol = ['$', '@', '#', '%']
    val = True

    if len(password) < 6:
        print('length should be at least 6')
        val = False

    if len(password) > 20:
        print('length should be not be greater than 8')
        val = False

    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False

    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False

    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False

    if not any(char in SpecialSymbol for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val


def main():
    email = "jyothiketha16@gmail.com"
    validateEmail(email)
    password = "Sarvaani@8"
    if (validatePasswd(password)):
        print("Password is valid")
    else:
        print("Password is invalid!!")


if __name__ == '__main__':
    main()


