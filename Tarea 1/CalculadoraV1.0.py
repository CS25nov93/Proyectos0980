import os

def interfaz ():
	print ("--- Calculadora V1.0 ---" + "\n\n")
	print ("1) Suma")
	print ("2) Resta")
	print ("3) Multiplicacion")
	print ("4) Division")
	print ("5) Salir" + "\n")

def validarOpcion (mensaje, advertencia):
	while True:
		try:
			N = int(input(mensaje))
			if (N >= 1 and N <= 5):
				return N
				break
			else:
				print (advertencia + "\n")
		except ValueError:
			print (advertencia + "\n")

def validarNumero (mensaje, advertencia):
	while True:
		try:
			N = float(input(mensaje))
			return N
			break
		except ValueError:
			print (advertencia + "\n")

def calculadora ():
	while True:
		os.system("cls")
		interfaz()
		option = validarOpcion("Seleccione una opcion: ", "¡Ingrese una opcion valida!")
		print ("\n")
		while (option > 0 and option < 5):
			N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!")
			N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!")
			if(option == 1):
				z = N1 + N2
				print ("La suma es: " + str(z) + "\n")
			elif(option == 2):
				z = N1 - N2
				print ("La resta es: " + str(z) + "\n")
			elif(option == 3):
				z = N1 * N2	
				print ("La multiplicacion es: " + str(z) + "\n")
			elif(option == 4):
				try:
					z = N1 / N2
					print ("La division es: " + str(z) + "\n")
				except ZeroDivisionError:
					print ("¡La division entre 0 no esta definida!" + "\n")
			break
		if(option == 5):
			print ("¡Gracias por utilizar nuestra plataforma!" + "\n")
			delay = input("Presione cualquier para continuar . . . ")
			break
		delay = input("Presione cualquier tecla para continuar . . . ")
		os.system("cls")

calculadora ()