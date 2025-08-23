# --------------- PostBoard ---------------#

import datetime

users = {}
posts = []

def user_register():
    while True:
        username = input("\nEnter Username : ").strip()

        if not username:
            print("\nUsername can't be empty.")
            continue
        if username in users:
            print("\nUsername already exists. Try again..!!")
            continue

        password = input("Enter Password : ").strip()

        if not password:
            print("\nPassword can't be empty.")
            continue

        users[username] = password

        print(f"\nUser '{username}' registered successfully!!")
        break

# ---------------------------------------------------------------------------------- #    
 
def user_login():
    attempts = 4
    while attempts > 0:
        username = input("\nUsername : ").strip()
        password = input("Password : ").strip()

        if username in users and users[username] == password:
            print(f"\nWelcome {username}!!")
            return username
        else:
            attempts -= 1
            print(f"\nInvalid Credentials. Attempts left : {attempts}")
    
    print("\nError: Too many failed attempts... Try again later...!!")
    return None

# ---------------------------------------------------------------------------------- #

def create_post(author):

    title = input("\nEnter Post Title : ").strip()
    if not title:
        print("\nTitle can't be empty.")
        return
    
    desc = input("Enter Post Description : ").strip()
    if not desc:
        print("\nDescription can't be empty.")
        return
    
    date = datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    post = {
            "author": author,
            "title": title,
            "desc": desc,
            "date": date    
            }
    
    posts.append(post)

    print("\nPost Created Successfully!!")

# ---------------------------------------------------------------------------------- #

def view_posts():
    
    if not posts:
        print("\nNo Posts Available Yet...!! \n")
        return
    
    print("\n -------- All Posts -------- ")

    for i, post in enumerate(posts, start=1):
        print(f"\n--- Post : {i} ---\n")
        print(f"Author : {post['author']}")
        print(f"Title : {post['title']}")
        print(f"Description : {post['desc']}")
        print(f"Date : {post['date']}")
        print("\n----------------------------\n")

# ---------------------------------------------------------------------------------- #

def search_posts():
    username = input("\nEnter Username to Search Posts : ").strip()

    found = [pt for pt in posts if pt['author'] == username]

    if not found:
        print(f"\nNo Post Found For User '{username}'...!! \n")
    else:
        print(f"\n----- Posts by '{username}' -----")

        for post in found:
            print(f"\nTitle : {post['title']} ({post['date']})")
            print(f"Description : {post['desc']}")
        print()

# ---------------------------------------------------------------------------------- #

def user_menu(user):
    while True:
        print("\n1. Create Post \n2. View All Posts \n3. Search Posts by Username \n4. Logout \n")
        choice = input("Enter Your Choice : ").strip()

        if choice == "1":
            create_post(user)
        elif choice == "2":
            view_posts()
        elif choice == "3":
            search_posts()
        elif choice == "4":
            print(f"Logged out {user}.")
            break
        else:
            print("\nError: Invalid Choice... Try again later...!!")

# ---------------------------------------------------------------------------------- #

def main():
    print("\n-------- Welcome to PostBoard -------- ")

    while True:
        print("\n1. Register \n2. Login \n3. Exit \n")
        choice = input("Enter Your Choice : ").strip()

        if choice == '1':
            user_register()
        elif choice == '2':
            user = user_login()
            if user:
                user_menu(user)
        elif choice == '3':
            print("\nThank You For Using PostBoard... Good Bye!!\n")
            break
        else:
            print("\nError: Invalid Choice... Try again later...!!")

# ---------------------------------------------------------------------------------- #

main()  

# --------------- End of PostBoard ---------------#



