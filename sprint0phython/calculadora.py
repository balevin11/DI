def calculadora():
    from operaciones import plus, minus, multiplication, division
    again = str("s")
    while again == "s":
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
            print(plus(n1, n2))
        elif op == "2":
            print(minus(n1, n2))
        elif op == "3":
            print(multiplication(n1, n2))
        elif op == "4":
            print(division(n1, n2))
        else:
            print("Error: Valor fuera de rango")
        print("¿Realizar otra operación? (s/n)")
        again = input()
        while again != "s" and again != "n":
            if again != "s" and again != "n":
                print ("Error: Valor fuera de rango")
            print ("¿Realizar otra operación? (s/n)")
            again = input()
            print (again)

        if again == "n":
            print ("Fin del programa")
