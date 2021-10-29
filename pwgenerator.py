import string
import random

#karakterer til at oprette passwords
karakterer = list(string.ascii_letters + string.digits + "#%&/()^*)")
længde = 12

def generer_random_pw():
	#længde
	#længde = int(input ("Indtast pw længde"))

	random.shuffle(karakterer)	

	password = []
	for i in range(længde):
		password.append(random.choice(karakterer))


	random.shuffle(password)

	print("".join(password))


generer_random_pw()
