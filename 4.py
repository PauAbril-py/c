a=int(input("Introduzca el número del DNI: "))
b=["T","R","W","A","G","M","Y","F","P","D","X","B","N","J","Z","S","Q","V","H","L","C","K","E"]
if a>=10000000 and a<=99999999:
	print("La letra del DNI es: ", b[a%23])