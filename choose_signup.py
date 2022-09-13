import index, signin

def choose_signup() :
	print("Choose :")
	print("1. Back to MainPage    2. Sign-In")
	n = input("Type your response : ")
	if (n == 1) :
		main()
	else if (n == 2) :
		singin()
	else :
		print("WRONG RESPONSE. TRY AGAIN.")
		choose_signup()