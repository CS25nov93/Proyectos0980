import os

def archivoTXT(N, resultado):
	try:
		archivo = open("HistorialDeFactoriales.txt", "a")
		archivo.write("El factorial de " + str(N) + " es " + str(resultado) + "\n")
		archivo.close()
	except:
		print ("No se encontro el archivo .txt :(")

def validarNumero(mensaje, advertencia):
	while True:
		try:
			N = int(input(mensaje))
			if (N >= 0):
				return N 
				break
			else:
				print (advertencia + "\n")
		except ValueError:
			print (advertencia + "\n")

def nFactorial(N):
	resultado = 1
	for i in range (N):
		resultado = (i+1)*resultado
	print ("El factorial de " + str(N) + " es " + str(resultado) + "\n")
	archivoTXT(N, resultado)

def calculadoraFactorial():
	while True:
		os.system("cls")
		print ("--- Calculadora factorial de N! ---" + "\n")
		N = validarNumero("Ingrese el numero deseado: ", "¡Entrada no valida!")
		nFactorial(N)
		delay = input("Presione cualquier tecla para continuar (s para salir) . . . ")
		os.system("cls")
		if (delay == "s" or delay == "S"):
			break

calculadoraFactorial()