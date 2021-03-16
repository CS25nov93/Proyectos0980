pkg load database

function interfaz()
  disp(strcat("--- Calculadora V2.0 ---", "\n\n"))
	disp("1) Suma")
  disp("2) Resta")
	disp("3) Multiplicacion")
	disp("4) Division")
	disp(strcat("5) Salir", "\n"))
endfunction

function N = validarOpcion(mensaje, advertencia)
  while(true)
    try
      N = input(mensaje);
      if(N >= 1 && N <= 5)
        break
      else
        disp(strcat(advertencia, "\n"))
      endif
    catch
        disp(strcat(advertencia, "\n"))
    end_try_catch
  endwhile
endfunction

function N = validarNumero(mensaje, advertencia)
  while(true)
    try
      N = input(mensaje);
        break
    catch
        disp(strcat(advertencia, "\n"))
    end_try_catch
  endwhile
endfunction

function conectarDB(N1, N2, operacion, resultado)
  try
    connection = pq_connect (setdbopts ("dbname", "carlos_solis", "host", "localhost", "port", "5432", "user", "postgres", "password", "CS0384!"));
  catch
    disp(strcat("¡Error :( no se guardo el resultado en la BD!", "\n"));
  end_try_catch
  
  id = 1;
  while(true)
    try
      connection = pq_connect (setdbopts ("dbname", "carlos_solis", "host", "localhost", "port", "5432", "user", "postgres", "password", "CS0384!"));
      B = pq_exec_params(connection, "select id from calculadora_v2 where id = $1;", {id}).data{1};
      id = id + 1;
    catch
      pq_exec_params(connection, "insert into calculadora_v2 values ($1, $2, $3, $4, $5);", {id, N1, N2, operacion, resultado});
      break
    end_try_catch
  endwhile
    pq_close(connection);
endfunction

function suma()
  disp("La opcion seleccionada fue SUMA")
  N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!");
  N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!");
  z = N1 + N2;
  conectarDB(N1, N2, 'suma', z)
  fprintf("La suma es: %f \n\n", z)
  
endfunction

function resta()
  disp("La opcion seleccionada fue RESTA")
  N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!");
  N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!");
  z = N1 - N2;
  conectarDB(N1, N2, 'resta', z)
  fprintf("La resta es: %f \n\n", z)
endfunction

function multiplicacion()
  disp("La opcion seleccionada fue MULTIPLICACION")
  N1 = validarNumero("Ingrese el numero (1): ", "¡Error :( intente de nuevo!");
  N2 = validarNumero("Ingrese el numero (2): ", "¡Error :( intente de nuevo!");
  z = N1 * N2;
  conectarDB(N1, N2, 'multiplicacion', z)
  fprintf("La multiplicacion es: %f \n\n", z)
endfunction

function division()
  disp("La opcion seleccionada fue DIVISION")
  N1 = validarNumero("Ingrese el numero (1): ", "�Error :( intente de nuevo!");
  N2 = validarNumero("Ingrese el numero (2): ", "�Error :( intente de nuevo!");
  if(N2 != 0)
    z = N1 / N2;
    conectarDB(N1, N2, 'division', z)
    fprintf("La division es: %f \n\n", z)
  elseif
    fprintf("¡La division entre 0 no esta definida! \n\n")   
  endif
endfunction

function salir()
  disp(strcat("¡Gracias por utilizar nuestra plataforma!", "\n"))
endfunction

function calculadora()
  while(true)
    clc
    interfaz()
    option = validarOpcion("Seleccione una opcion: ", "¡Ingrese una opcion valida!");
    disp("\n")
    switch(option)
      case 1
        suma()
      case 2
        resta()
      case 3
        multiplicacion()
      case 4
        division()
      case 5
        salir() 
    endswitch
    if(option == 5)
      delay = input("Presione cualquier tecla para continuar . . . ", 's');
      break
    endif
    delay = input("Presione cualquier tecla para continuar . . . ", 's');
    clc
  endwhile
endfunction

calculadora()