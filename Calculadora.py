# Lectura del valor de 2 variables enteras por consola:
print("Ingrese el número 1")
numero1 = int(input())
print("Ingrese el número 2")
numero2 = int(input())
print("Ingrese la operación ((+)=suma, (+)=resta), (*)=multiplicación, (/)=división, (M)=modulo, (P)=Potencia)")
operacion = input()

match operacion:
    case '+':
        # Operación suma:
        suma = numero1 + numero2
        print("La suma es " + str(suma))
    case '-':
        # Operación resta:
        resta = numero1 - numero2
        print("La resta es " + str(resta))
    case '*':
        # Operación multiplicación:
        multiplicacion = numero1 * numero2
        print("La multiplicación es " + str(multiplicacion))
    case '/':
        # Operación división:
        division = numero1 / numero2
        print("La división es " + str(division))
    case 'M':
        # MODULO:
        modulo = numero1 % numero2
        print("El módulo es " + str(modulo))
    case 'P':
        # POTENCIA:
        print ("El numeor base es: " + str(numero1))
        print ("El numeor exponente es: " + str(numero2))
        potencia = numero1 ** numero2

        print ("La potencia del numero *" + str(numero1) + "* elevado al *" + str(numero2) + "* es: " + str(potencia))
    case _ :
        print("Operación inválida")

