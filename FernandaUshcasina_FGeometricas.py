print("                      ESCUELA POLITECNICA NACIONAL")
print("                  ESCUELA DE FORMACION DE TECNOLOGOS")
print("PROGRAMACION AVANZADA")
print("FERNANDA USHCASINA, JESICA CARRILLO")
print("PROYECTO")
print("FIRGURAS GEOMETRICAS")
import math
def aypTriangulo():
    print("Usted seleccinó un *Triangulo* figura de 3Lados")
    b = int(input("Ingresa base: "))
    h = int(input("Ingrese altura: "))
    area= b*h/2
    perimetro= 3*b
    print("el area es: " + str(area))
    print("el perimetro es: " + str(perimetro))

def aypCuadrado():
    print("Usted seleccinó un *Cuadrado* figura de 4Lados")
    a = int(input("Ingrese lado: "))
    area = a * a
    perimetro = 4 * a
    print("el area es: " + str(area))
    print("el perimetro es: " + str(perimetro))

def aypPentagono():
    print("Usted seleccinó un *Pentagono* figura de 5 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*5 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print("el area del pentagono es: " + str(area))
    print("el perimetro del pentagono es: " + str(perimetro))
    
def Intentar():
    
    while(again!="no"):
        menu()
    
def menu():
    print("LISTA DE FIGURAS QUE CONTIENE EL PROGRAMA")
    print("Area y perimetro de una figura geometrica regular")
    print("3. Triangulo")
    print("4. Cuadrado")
    print("5. Pentagono")

    global opcion
    opcion=int(input("Ingrese el numero de lados de la figura: "))
    
    if(opcion==1):
        print("No existe una figura de un solo lado")
        print("Ingrese numero de lados correctos \n")
        opcion
    elif(opcion==2):
        print("No existe una figura de dos lados")
        print("Ingrese numero de lados correctos \n")
        opcion
    elif(opcion==3):
        aypTriangulo()
    elif(opcion==4):
        aypCuadrado()
    elif(opcion==5):
        aypPentagono()

    else:
        print("Opcion ingresada incorrecta")
    print("Quieres elegir nuevamente(si/no)")
    global again
    again=input()
    again=again.lower()
    Intentar()

menu()
