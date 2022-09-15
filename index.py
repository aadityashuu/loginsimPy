import sqlite3
import signin, signup

def choose() : 
    print("\nChoose weather you want to Sing-In or Sign-Up")
    print("1 : Sign-In    2 : Sign-Up")
    n = input("\nType your response : ")
    if (n==1) : 
        signin()
    elif (n == 2) :
        signup()
    else : 
        print("WRONG RESPONSE. TRY AGAIN.")
def main() :
    print("HELLO !")
    print("WELCOME TO DUMMY")
    choose()