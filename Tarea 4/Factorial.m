function calculadoraFactorial()
  while(true)
    clc
    disp(strcat("--- Calculadora factorial de N! ---", "\n"))
    N = validarNumero("Ingrese el numero deseado: ", "¡Entrada no valida!");
    nFactorial(N)
    delay = input("Presione cualquier tecla para continuar (s para salir) . . . ", 's');
    clc
    if(delay == "s" || delay == "S")
      break
    endif
  endwhile
endfunction

function archivoTXT(N, resultado)
  try
    archivo = fopen('HistorialDeFactoriales.txt', 'a');
    fprintf(archivo, "El factorial de %d es %d \n", N, resultado);
    fclose(archivo);
  catch
    disp("No se encontro el archivo .txt :(")
  end_try_catch
endfunction

function N = validarNumero(mensaje, advertencia)
  while(true)
    try
      N = input(mensaje);
      if(N >= 0)
        break
      else
        disp(strcat(advertencia, "\n"))
      endif
    catch
      disp(strcat(advertencia, "\n"))
    end_try_catch
  endwhile
endfunction

function nFactorial(N)
  resultado = 1;
  for i = 0 : (N - 1)
    resultado = (i+1)*resultado;
  endfor
  fprintf("El factorial de %d es de %d \n\n", N, resultado)
  archivoTXT(N, resultado);
endfunction