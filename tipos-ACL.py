ACL = int(input("¿Cuál es el número IPv4 ACL? "))
if ACL >= 1 and ACL <= 99:
	print ("Este es una ACL IPv4 estándar. ")
elif ACL >= 100 and ACL <= 199:
	print ("Este es una ACL IPv4 extendida")
else:
	print ("Esta ACL IPv4 no es extendida o estandar .")
