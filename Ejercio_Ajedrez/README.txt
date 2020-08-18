-------------------Ejercicio calculo movimientos fichas de ajedrez---------------------

Caracteristicas del sistema
	- Se tiene en cuenta los movimientos de todas las fichas: Reina, Rey, Peon, Alfil, Caballo y Torre
	- En el caso de los Peones se contempla si es blanco (numero 1) o negro (numero 2); si el movimiento
          es inicial, es decir cuando puede mover 2 posiciones (numero 3); y el movimiento cuando come, que es
          de forma diferente a su movimiento tradicional (si es blaco muestra un -1 si es negro muestra un -2)
	- En el caso de los Peones tambien se contempla si esta en una posicion al final del tablero, en este caso
         no hay movimientos posibles pues el jugador ha coronado un peon

Consideraciones:
	-Tener instalado python >3.6 

Como proceder:
	- 1. Pararce en el directorio principal, donde esta el archivo requirements.txt y 
	     abrir la consola de comandos (cmd)
	- 2. Con la instrucción 'pip install -r requirements.txt instalar los paquetes necesarios
	- 3. Correr la ejecución del programa con Main.py y seguir las instrucciones