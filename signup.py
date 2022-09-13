import choose_signup

def signup() :
    print("Sign-Up :")
    id = input("Create Username : ")
    passwd = input("Create Password : ")
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users VALUES('{id}','{passwd}')")
    conn.commit()
    conn.close()
    choose_signup()