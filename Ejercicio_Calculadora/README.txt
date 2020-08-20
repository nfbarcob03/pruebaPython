-------------------Ejercicio calculadora matematica---------------------

Caracteristicas del sistema
	- La funcionalidad de la suma y la resta esta unida y no tiene un limite de numeros u operadores, solo asegurarse
	ingresar una operación que siga el patron requerido:

		patron_suma_resta = (+|-|'')n1(+|-)n2(+|-)n3......(+|-)nk  
			siendo ni->i{1,k} los numeros que componen la operacion

	ejemplos: 1+2+3, -1+6-9+4, +1+5-6-7 
	No es sensible a los espacios, es decir, se toma tanto 9 +8+ 6 como  9+8+6 como 9+ 8 + 6...

	- La funcionalidad de multiplicacion de factores no tiene limite de factores, solo asegurse de ingresar
	una operacion de factores valida que siga el patron requerido
		patron_multiplicacion_factores = (patron_suma_resta)(patron_suma_resta)(patron_suma_resta)....(patron_suma_resta)
	ejemplos: (1+2+3), (1+2+3)(-1+6-9+4), (1+2+3)(-1+6-9+4)(+1+5-6-7 )....
	No es sensible a los espacios, es decir, es lo mismo (1+2+3)(-1+6-9+4)(+1+5-6-7) que (1+2+3) (-1 +6- 9+4) (+1+5 -6-7 )
        o que (1+2+3)(-1+6- 9+4) (+1 +5- 6-7) o cualquiera de sus combinaciones

	- La funcionalidad de multiplicación de polinomios no tiene limite de polinomios, solo asegurse de ingresar
	una operacion de polinomios valida que siga el patron requerido:
		patron_multiplicacion_polinomios = [a0,a1,a2....an][b0,b1,b2,...bm][c0,c1,c2...cnn]....
		es decir, una lista con los coeficientes en orden, empezando 0 como el coeficiente para x^0 y continuando
		con los coeficientes 1 (coeficiente para x^1), 2 (coeficiente para  x^2), 3 (coeficiente para  x^3).... 
		hasta el coeficiente n(x^n).
	En caso de que algun coeficiente sea 0 (es decir, no exista ) igual incluirlo en la lista.
	recibe operaciones de suma y resta como coeficientes
	ejemplos: 	[1] ---> (1)
				[1][2,1] ----> (1)(2+x)
				[1][2,1][2,1,3]  -----> (1)(2+x)(2+x+3x^2)
				[1][2,1][2,1,3][2,0,3,0,1]  -----> (1)(2+x)(2+x+3x^2)(2+3x^2+x^4)
				[1][2,1][2,1,3][2,0,3,0,1][1+2+4-3, -1-2 + 5, 1 +2 -1]  -----> (1)(2+x)(2+x+3x^2)(2+3x^2+x^4)(4+2x+2x^2)

	Al igual que las anteriores funcionalidades, no es sensible a los espacios

	-La funcionalidad de evaluar polinomio no tiene limite de polinomio pero aplica solo para 1 variable. Se requiere
	que se siga el patron definido:
		patron_multiplicacion_polinomios x=numero
		donde x se debe poner literal y numero sera el valor que se le asignara a la variable
	ejemplos:	[1]x=0 ---> (1)  evalua x=0
				[1][2,1]x=1 ----> (1)(2+x) evalua x=1
				[1][2,1][2,1,3]x=2  -----> (1)(2+x)(2+x+3x^2) evalua x=2
				[1][2,1][2,1,3][2,0,3,0,1]x=3  -----> (1)(2+x)(2+x+3x^2)(2+3x^2+x^4) evalua x=3
				[1][2,1][2,1,3][2,0,3,0,1][1+2+4-3, -1-2 + 5, 1 +2 -1]x=4  -----> (1)(2+x)(2+x+3x^2)(2+3x^2+x^4)(4+2x+2x^2) evalua x=4
	Al igual que las anteriores funcionalidades, no es sensible a los espacios

Consideraciones:
	-Tener instalado python >3.6 
	-Al ingresar las operaciones de suma y resta, garantizar finalizar con algun digito y no en un 
        operador como (+ o -). 
	-Se hace uso de regex para validar lso patrones de las entradas de usuario
	-Se hace uso de funciones map y conprenhesion para hacer operaciones sobre arreglos y listas

Como proceder:
	- 1. Pararce en el directorio principal, donde esta el archivo requirements.txt y 
	     abrir la consola de comandos (cmd)
	- 2. Con la instrucción 'pip install -r requirements.txt instalar los paquetes necesarios
	- 3. Correr la ejecución del programa con Main.py y seguir las instrucciones