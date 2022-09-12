import signin, signup

print("HELLO !")
print("WELCOME TO DUMMY")
print("\nChoose weather you want to Sing-In or Sign-Up")
print("1 : Sign-In    2 : Sign-Up")
n = input("\nType your response : ")
if n==1 : 
    signin()
else :
    signup()