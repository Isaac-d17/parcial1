nombre= input("Introduzca su nombre:\n")
ancho= int(input("Introduzca el ancho en metros:\n"))
longitud= int(input("Introduzca la longitud en metros:\n"))
costo= int(input("Introduzca el costo:\n"))
resp= int(ancho*longitud)
costot= int(resp*costo)
print("Bienvenido :", nombre,
"\nEl terreno tiene un costo de:",costot,"por metros cuadrados")
