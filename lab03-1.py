import base64

do_zakodowania = input("Podaj lancuch znakow do zaszyfrowania: ")
zakodowany = base64.b64encode(do_zakodowania.encode())
print("Twoj zaszyfrowany lancuch znakow wyglada tak: ", zakodowany.decode())