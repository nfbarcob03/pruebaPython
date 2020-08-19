class Mensajes:
    menu1 = {
        'Menu': 'Menu',
        '0': 'No es una opcion valida',
        '1': '1. Suma y Resta',
        '2': '2. Multiplicación entre polinomios',
        '3': '3. Multiplicacion por un escalar',
        '4': '4. Evaluación de un polinomio',
        '5': '5. SALIR',

    }

    common = {
        'bienvenida': "Bienvenido al ejercicio para calculos matematicos.",
        'explicacionTablero': "A continuación se muestra las casillas del tablero de ajedrez enumeradas" + '\n' + "desde la 0 (esquina superior izquierda), hasta la 63 esquina inferior derecha",
        'pedirPosicionFicha': "Segun la información anterior, ingrese la casilla donde desea ubicar la ficha" + '\n' + "(no es necesario saber que tipo de pieza del juego va a probar, solo la posición)",
        'tableroConFichaPuesta': "A continuación se presenta el tablero con la ficha ubicada en la posición que se indico" + '\n' + " con un numero 8 y el resto de casillas con un 0, indicando que estan disponibles para el movimiento de la ficha",
        'separador': '---------------------------------------------------------------------------------------',
        'ingresarCasilla': 'Por favor, ingrese la casilla donde desea colocar la ficha ' + '\n',
        'io': 'Ingrese una opcion:' + '\n',
        'es': '\n',
        'tituloTableroNumerado': "---------------------------Tablero con posiciones numeradas---------------------------",
        'tituloTableroVacio': "----------------------------------Tablero en blanco-----------------------------------",

    }

    operaciones = {
        'ingreseOperacionSuma': 'Ingrese la operación que desea realizar que solo incluya sumas y restas' + '\n',
        'ingreseMultiplicacionFactores': 'Ingrese la operación de polinomios a multiplicar' + '\n',
        'opcion1': '1. Realizar otra operacion',
        'opcion2': '2. Volver al menu anterior',
        'opcion3': '3. Salir'
    }

    error = {
        'patronInvalido': 'La operación ingresada no tiene el patron correcto. Revise por favor o consulte el README.'
    }
