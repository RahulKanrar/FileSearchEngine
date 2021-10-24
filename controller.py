from authentication import *
from errorLogging import *
from searchTemplate import *
from database import DatabaseOperations
#from TableLoginCredentials import close


# clos = DatabaseOperations()
# input login credentials
def login_credentials():
    username = input('ENter Email: ')
    password = input("Enter password: ")
    return username, password


# login flow
def login():
    option = int(input('Choose options:\n\n1. sign-in\n\n2. Register\n\n-> '))
    validateLoginChoice(option)

    if option == 1:
        udetails = login_credentials()
        obj_login = Login(udetails[0], udetails[-1])
        res = obj_login.signin()
        if res == 'Invalid':
            loginres = obj_login.re_login()
            if loginres == True:
                login()
            else:
                print("Buye")
    elif option == 2:
        udetails = login_credentials()
        obj_login = Login(udetails[0], udetails[-1])
        # obj_login.validateUdetails()
        # obj_login = Login(username, password)
        resR = obj_login.register()
        if resR == 'Invalid':
            loginres = obj_login.re_login()
            if loginres == True:
                login()
            else:
                print("Buye")


# input file name
def file_name():
    filename = input("Enter file name: ")
    return filename


# search flow
def search():
    obj_search = SearchTemplate()
    availdrives = obj_search.display_drives()
    search_drive = obj_search.search_drives()
    rdrives = obj_search.resultantdrives()
    if rdrives == 0:
        re_attempt = obj_search.re_search()
        if re_attempt == 1:
            search()
        else:
            print("Bue")
    else:
        filename = file_name()
        if len(rdrives) == 1:
            obj_search.search_single_drive(filename, rdrives[0])
        else:
            obj_search.search_Multiple_drives(filename, rdrives)


def main():
    login()
    search()
    clos = close()


if __name__ == '__main__':
    main()
