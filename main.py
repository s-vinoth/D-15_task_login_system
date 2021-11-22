import re

name_reg = r"\b[A-Za-z0-9_]+@[A-Za-z0-9]+\.+[A-z|a-z]{2,}\b"


def Forget_Password(username=None):
    username = str(input("Enter Your Username: "))
    if len(username) > 2:
        data_tx = open("data_signup.txt", "r")
        u_n = []
        p_w = []

        for z in data_tx:
            a, b = z.split(", ")
            b = b.strip()
            u_n.append(a)
            p_w.append(b)
        data_in = dict(zip(u_n, p_w))

        if username in u_n:
            print(f"Hai,{username} your Password is: {data_in[username]}")

        else:
            print("Username not exist please register")
            Sign_up()

    else:
        print("The given username is not correct")
        Home_Page()


def Log_in(username=None, password=None):
    username = str(input("Enter Your Username: "))
    password = str(input("Enter Your Password: "))
    data_tx = open("data_signup.txt", "r")
    u_n = []
    p_w = []

    for z in data_tx:
        a, b = z.split(", ")
        b = b.strip()
        u_n.append(a)
        p_w.append(b)
    data_in = dict(zip(u_n, p_w))
    try:
        if password == data_in[username]:
            print("Login Successful")
            print("Hi", username)

        else:
            print("Incorrect username or password")

    except:
        print("Incorrect username or password")
        Home_Page()


def Sign_up(username=None, password=None, confirm_password=None):
    username = input("Create Your Username: ")
    password = input("Create Your Password: ")
    confirm_password = input("Re-Enter Your Password: ")
    data_tx = open("data_signup.txt", "r")
    u_n = []
    p_w = []

    for z in data_tx:
        a, b = z.split(", ")
        b = b.strip()
        u_n.append(a)
        p_w.append(b)

    if (re.fullmatch(name_reg, username)) is None:
        print("Please try another username \n eg:- 1.sherlock@gmail.com, 2.nothing@yahoo.in")
        Sign_up()

    elif password != confirm_password:
        print("Password doesn't match")
        Sign_up()

    elif not len(password) > 5 and len(password) < 16:
        print("5 < password length > 16 \n 1.Must have minimum one special character \n 2.one digit \n"
              "3.one uppercase \n 4.one lowercase character \n")
        Sign_up()

    elif re.search(r'[!@*$%&]', password) is None:
        print("Password Must have minimum one special character \n eg:- !@*$%&")
        Sign_up()

    elif re.search(r'\d', password) is None:
        print("Password Must have minimum one digit")
        Sign_up()

    elif re.search(r'[A-Z]', password) is None:
        print("Password Must have minimum one Uppercase")
        Sign_up()

    elif re.search(r'[a-z]', password) is None:
        print("Password Must have minimum one Lowercase")
        Sign_up()

    elif username in u_n:
        print("Username already exist")
        Log_in()

    elif re.search(r"\s", password):
        print("Space are not allowed")

    else:
        data_tx = open("data_signup.txt", "a")
        data_tx.write(username + ", " + password + "\n")
        print("YOUR REGISTRATION SUCCESSFUL")
        data_tx.close()
        Log_in()


def Home_Page():
    print("Welcome to your dashboard")
    print("please select the option")
    option = input(" 1.Login: \n 2.Register: \n 3.Forget_password: \n 4.Exist \n Please Enter Your Option: ")
    if option == "1":
        Log_in()
    elif option == "2":
        Sign_up()
    elif option == "3":
        Forget_Password()
    elif option == "4":
        print("Thank You...")
        exit()
    else:
        print("invalid option")
        Home_Page()


Home_Page()
