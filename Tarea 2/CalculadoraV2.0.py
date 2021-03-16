import os
import psycopg2

def interfaz ():
	print ("--- Calculadora V2.0 ---" + "\n\n")
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

def conectarDB (N1, N2, operacion, resultado):
	try:
		connection = psycopg2.connect(user="postgres", password="CS0384!", database="carlos_solis", host="localhost", port="5432")
		pivote = connection.cursor()
		insertar = 'insert into calculadora_v2(N1, N2, operacion, resultado) values (%s, %s, %s, %s)'
		data = (N1, N2, operacion, resultado)
		pivote.execute(insertar, data)
		connection.commit()
		connection.close()
	except (Exception, psycopg2.DatabaseError) as error:
		print ("¡Error :( no se guardo el resultado en la BD!" + "\n")

def suma ():
	print ("La opcion seleccionada fue SUMA")
	N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!")
	N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!")
	z = N1 + N2
	print ("La suma es: " + str(z) + "\n")
	conectarDB(N1, N2, 'suma', z)

def resta ():
	print ("La opcion seleccionada fue RESTA")
	N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!")
	N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!")
	z = N1 - N2
	print ("La resta es: " + str(z) + "\n")
	conectarDB(N1, N2, 'resta', z)

def multiplicacion ():
	print ("La opcion seleccionada fue MULTIPLICACION")
	N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!")
	N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!")	
	z = N1 * N2
	print ("La multiplicacion es: " + str(z) + "\n")
	conectarDB(N1, N2, 'multiplicacion', z)

def division ():
	print ("La opcion seleccionada fue DIVISION")
	N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!")
	N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!")
	try:
		z = N1 / N2
		print ("La division es: " + str(z) + "\n")
		conectarDB(N1, N2, 'division', z)
	except ZeroDivisionError:
		print ("¡La division entre 0 no esta definida!" + "\n")

def salir ():
	print ("¡Gracias por utilizar nuestra plataforma!" + "\n")

def error ():
	print ("¡Ingrese una opcion valida!")

def calculadora ():
	while True:
		os.system("cls")
		interfaz()
		option = validarOpcion("Seleccione una opcion: ", "¡Ingrese una opcion valida!")
		print ("\n")
		switch_operaciones = {
			1: suma,
			2: resta,
			3: multiplicacion,
			4: division,
			5: salir,
		}
		switch_operaciones.get(option, error)()
		if(option == 5):
			delay = input("Presione cualquier para continuar . . . ")
			break
		delay = input("Presione cualquier tecla para continuar . . . ")
		os.system("cls")

calculadora ()