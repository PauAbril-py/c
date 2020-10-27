#	1 Kilómetros = 0.6214 Millas = 0.54 Millas náuticas
#	1 Millas = 1.6093 Kilómetros = 0.869 Millas náuticas
#	1 Millas náuticas = 1.852 Kilómetros = 1.1508 Millas
a=int(input("Quina es la teva longitud:	"))
b=int(input("""
	1)	km
	2)	mi
	3)	nmi

"""))
print()
if b == 1:
	print("	",a,"km")
	print("	",a*0.62,"mi")
	print("	",a*0.54,"nmi")
elif b == 2:
	print("	",a*1.61,"km")
	print("	",a,"mi")
	print("	",a*0.869,"nmi")
elif b == 3:
	print("	",a*1.85,"km")
	print("	",a*1.15,"mi")
	print("	",a,"nmi")