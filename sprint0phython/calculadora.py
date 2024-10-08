def calculadora():
    from operaciones import suma, resta, multiplicacion, division
    continuar = "s"
    while continuar == "s":
        print("Primer número?")
        n1 = float(input())
        print("Segundo número")
        n2 = float(input())
        print("Operaciones:")
        print("1.- Suma")
        print("2.- Resta")
        print("3.- Multiplicación")
        print("4.- División")
        op = input()
        if op == "1":
            print(suma(n1, n2))
        elif op == "2":
            print(resta(n1, n2))
        elif op == "3":
            print(multiplicacion(n1, n2))
        elif op == "4":
            print(division(n1, n2))
        else:
            print("Error: Valor fuera de rango")
        print("¿Realizar otra operación? (s/n)")
        continuar = input()
        while continuar != "s" and continuar != "n":
            if continuar != "s" and continuar != "n":
                print ("Error: Valor fuera de rango")
            print ("¿Realizar otra operación? (s/n)")
            continuar = input()
            print (continuar)

        if continuar == "n":
            print ("Fin del programa")
