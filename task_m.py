from datetime import datetime

task_db = []
user_db = []
is_login = None

user_id = 0
task_id = 0


def create_task(title, description, dueration, user_id):
    global task_id
    task_id += 1
    task = {
        "task_id": task_id,
        "title": title,
        "description": description,
        "dueration": dueration,
        "status": False,
        "user_id": user_id,
        "created_at": datetime.now()
    }
    task_db.append(task)


def read_task(task_id, user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            return f"""
Your task {i["task_id"]}:
Title:{i["title"]}
Description:{i["description"]}
Dueration :{i["dueration"]}
Status:{i["status"]}
"""
    else:
        return False


def update_task(task_id, title, descp, due, status, user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            if title:
                i["title"] = title
            if descp:
                i["description"] = descp
            if due:
                i["dueration"] = due
            if status:
                i["status"] = status


def delete_task(task_id, user_id):
    for i in task_db:
        if i["task_id"] == task_id and i["user_id"] == user_id:
            task_db.remove(i)
            return True
    else:
        return False


def registration(username, password):
    global user_id, is_login
    for user in user_db:
        if user["username"] == username:
            return False
    user_id += 1
    now = datetime.now()
    user = {
        "user_id": user_id,
        "username": username,
        "password": password,
        "created_at": now.strftime("%d-%m-%Y, %H:%M:%S")
    }
    user_db.append(user)
    is_login = user


def login(username, password):
    global is_login
    for user in user_db:
        if user["username"] == username:
            if user["password"] == password:
                # print(f"Welcome back, {username}!")
                is_login = user
                return True
            else:
                print(f"Wrong password!")
                return False
    else:
        print("User not found!")
        return False

def show_profile(user):
    cnt = 0
    for task in task_db:
        if task["user_id"] == user["user_id"]:
            cnt += 1
    print(f"\n===== INFO =====")
    print(f"Username: {user["username"]}")
    print(f"Created at: {user["created_at"]}")
    print(f"Tasks created: {cnt}")
    print(f"Last edited: {last_edit}")

def search(username):
    for user in user_db:
        if user["username"] == username:
            return user
    return False


def change_p(password, user):
    if len(password) > 0:
        user["password"] = password
        return True
    else:
        return False


while True:
    if is_login == None:
        print("\n====== AUTHENTICATION ======")
        try:
            n = int(input("\n1)Registration\n2)Login\n3)Search for user\n0)Exit\nChouse one: "))
        except ValueError:
            print("Please choose from options below!\n")
            continue
        match n:
            case 1:
                username = input("Username: ")
                password = input("Password : ")
                if registration(username, password) == False:
                    print("This user is already registered! Please login")
            case 2:
                username = input("Username: ")
                password = input("Password: ")
                if login(username,password):
                    print(f"Welcome back, {username}!")
            case 3:
                username = input("Username: ")
                user = search(username)
                if user:
                    show_profile(user)
                else:
                    print("User not found!")
            case 0:
                print("Good bye")
                break

    else:
        last_edit = None
        while True:
            print(f"\n====== Login as '{is_login["username"]}' ======")
            print(user_db)

            try:
                n = int(input("1)Create Task\n2)Read task\n3)Update Task\n4)Delete\n5)Show Profile\n0)Logout\nChouse one: "))
            except ValueError:
                print("Please choose from options below!\n")
                continue
            match n:
                case 1:
                    print("Start create task")
                    title = input("Title: ")
                    descp = input("Description: ")
                    durat = input("Duration: ")
                    create_task(title, descp, durat, is_login["user_id"])
                    print("Task created !!")
                    last_edit = datetime.now().strftime("%H:%M:%S")

                case 2:
                    k = int(input("Enter id task: "))
                    print(read_task(k, is_login["user_id"]))

                case 3:
                    print("Start update task")
                    k = int(input("Enter id task: "))
                    if read_task(k, is_login["user_id"]):
                        title = input("Title or put enter for continue: ")
                        descp = input("Description or put enter for continue: ")
                        durat = input("Duration or put enter for continue: ")
                        status = bool(input("Status or put enter for continue: "))
                        update_task(k, title, descp, durat, status, is_login["user_id"])
                        print("Task update !!")
                        last_edit = datetime.now().strftime("%H:%M:%S")
                    else:
                        print("This task dinaded")

                case 4:
                    k = int(input("Enter id task: "))
                    if delete_task(k, is_login["user_id"]):
                        print("Your task deleted!")
                        last_edit = datetime.now().strftime("%H:%M:%S")
                    else:
                        print("This task dinaded")
                case 5:
                    while True:
                        show_profile(is_login)
                        print("Enter 1 for settings or whatever  for exit")
                        try:
                            sett = int(input("Your choice: "))
                            while True:
                                print("\n1)Change the Password\n2)Delete user\n0)Back")
                                choice = int(input("Your choice: "))
                                match choice:
                                    case 1:
                                        chp = input("Enter current password: ")
                                        if login(is_login["username"], chp):
                                            np = input("Enter a new password: ")
                                            if change_p(np, is_login):
                                                print("Password has been changed!")
                                            else:
                                                print("Password can't be empty!")
                                        else:
                                            print("Incorrect password!!")
                                    case 2:
                                        
                                    case 0:
                                        print("=== EXIT! ===")
                                        break
                        except ValueError:
                            print("=== EXIT! ===")
                            break
                    # while True:
                    #     print("\n1)Change the Password\n2)Delete user\n0)Back")
                    #     choice = int(input("Your choice: "))
                    #     match choice:
                    #         case 1:
                    #             chp = input("Enter current password: ")
                    #             if login(is_login["username"], chp):
                    #                 np = input("Enter a new password: ")
                    #                 if change_p(np, is_login):
                    #                     print("Password has been changed!")
                    #                 else:
                    #                     print("Password can't be empty!")
                    #             else:
                    #                 print("Incorrect password!!")
                    #         case 0:
                    #             print("=== EXIT! ===")
                    #             break
                case 0:
                    print("=== Logout! ===")
                    is_login = None
                    break

                case _:
                    print("Invalid input!")