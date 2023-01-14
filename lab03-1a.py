import base64
while True:
	wybor = input('Jezeli chcesz zaszyfrowac swoj lancuch znakow, wpisz z i nacisnij enter.\nJezeli chcesz deszyfrowac swoj lancuch znakow, wpisz d i nacisnij enter.\nJezeli chcesz wyjsc z programu, wpisz exit i nacisnij enter.')
	
	if wybor == 'z':
		do_zakodowania = input("Podaj lancuch znakow do zaszyfrowania: ")
		zakodowany = base64.b64encode(do_zakodowania.encode())
		print("Twoj zaszyfrowany lancuch znakow wyglada tak: ", zakodowany.decode())
	
	elif wybor == 'd':
		do_zdekodowania = input("Podaj lancuch znakow do deszyfrowania: ")
		zdekodowany = base64.b64decode(do_zdekodowania.encode()).decode()
		print("Twoj lancuch pod deszyfrowaniu wyglada tak: ", zdekodowany)
		
	elif wybor == 'exit':
		break
	
	else:
		print("Zly wybor, wpisz z dla zaszyfrowania lub d dla deszyfrowania.")