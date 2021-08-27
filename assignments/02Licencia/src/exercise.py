
def main():
    edad = int(input("Ingresa tu edad: "))
    #Aquí empieza tu programa...
    if  edad >=18:
        ident= str(input("¿Tienes identificación oficial? (s/n): "))
        if ident == "s" or ident == "S":
            print ("Trámite de licencia concedido")
        elif ident == "n" or ident== "N":
            print ("No cumples requisitos")
        else:
            print("Respuesta incorrecta")
    elif 0<edad<=18:
        print("No cumples requisitos")
    else:
        print("Respuesta incorrecta")


if __name__ == '__main__':
    main()

