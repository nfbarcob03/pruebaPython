-------------------Ejercicio calculadora matematica---------------------

Caracteristicas del sistema
	- La funcionalidad de la suma y la resta esta unida y no tiene un limite de numeros u operadores, solo asegurarse
	ingresar una operación que siga el patron requerido:

		patron_suma_resta =(+|-|'')n1(+|-)n2(+|-)n3......(+|-)nk  
			siendo ni->i{1,k} los numeros que componen la operacion

	ejemplos: 1+2+3, -1+6-9+4, +1+5-6-7 
	No es sensible a los espacios, es decir, se toma tanto 9 +8+ 6 como  9+8+6 como 9+ 8 + 6...

	- La funcionalidad de multiplicacion de factores no tiene limite de factores, solo asegurse de ingresar
	una operacion de factores valida que siga el patron requerido
		(patron_suma_resta)(patron_suma_resta)(patron_suma_resta)....(patron_suma_resta)
	ejemplos: (1+2+3), (1+2+3)(-1+6-9+4), (1+2+3)(-1+6-9+4)(+1+5-6-7 )....
	No es sensible a los espacios, es decir, es lo mismo (1+2+3)(-1+6-9+4)(+1+5-6-7) que (1+2+3) (-1 +6- 9+4) (+1+5 -6-7 )
        o que (1+2+3)(-1+6- 9+4) (+1 +5- 6-7) o cualquiera de sus combinaciones

Consideraciones:
	-Tener instalado python >3.6 
	-Al ingresar las operaciones de suma y resta, garantizar finalizar con algun digito y no en un 
        operador como (+ o -). 

Como proceder:
	- 1. Pararce en el directorio principal, donde esta el archivo requirements.txt y 
	     abrir la consola de comandos (cmd)
	- 2. Con la instrucción 'pip install -r requirements.txt instalar los paquetes necesarios
	- 3. Correr la ejecución del programa con Main.py y seguir las instrucciones