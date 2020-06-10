numero=int(input("Ingrese:"))
centena = numero/100

decena =(numero%100)/10
unidad=(numero%100)%10

if (centena == unidad):
    print("el numero es capicúa")
else:
    print("el numero es capicua")
