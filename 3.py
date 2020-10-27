a=int(input("quin numero de dau vols:	"))
b=["un","dos","tres","quatre","cinc","sis"]
if a>=7 or a<=0:
	print("\nposa un numero correcte")
else:
	print("\nel numero que has tret es",b[a-1])
	print("el numero de darrerra es",7-a)