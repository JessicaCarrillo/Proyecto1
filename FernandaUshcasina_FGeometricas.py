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

def aypHexagono():
    print("Usted seleccinó un *Hexagono* figura de 6 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*6 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es", area )
    print ("el perimetro es:", perimetro)
    
def aypHeptagono():
    print("Usted seleccinó un *Heptagono* figura de 7 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*7 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es", area )
    print ("el perimetro es:", perimetro)
    
def aypOctagono():
    print("Usted seleccinó un *Octagono* figura de 8 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*8 
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es", area )
    print ("el perimetro es:", perimetro)
    
def aypNonagono():
    print("Usted seleccinó un *Nonagono* figura de 9 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*9
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es", area )
    print ("el perimetro es:", perimetro)

def aypDecagono():
    print("Usted seleccinó un *Decagono* figura de 10 Lados")
    lado = float(input("Ingrese Lado: "))
    radio= float(input("Ingrese radio: "))
    perimetro = lado*10
    area = (perimetro*(radio**2-(lado/2)**2)**(1/2))/2 
    print ("El area es", area )
    print ("el perimetro es:", perimetro)

    
def Intentar():
    
    while(again!="no"):
        menu()
    
def menu():
    print("LISTA DE FIGURAS QUE CONTIENE EL PROGRAMA")
    print("Area y perimetro de una figura geometrica regular")
    print("3. Triangulo")
    print("4. Cuadrado")
    print("5. Pentagono")
    print("6. Hexagono")
    print("7. Heptagono")
    print("8. Octagono")
    print("9. Nonagono")
    print("10. Decagono")
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
    elif(opcion==6):
        aypHexagono()
    elif(opcion==7):
        aypHeptagono()
    elif(opcion==8):
        aypOctagono()
    elif(opcion==9):
        aypNonagono()
    elif(opcion==10):
        aypDecagono()
    else:
        print("Opcion ingresada incorrecta")
    print("Quieres elegir nuevamente(si/no)")
    global again
    again=input()
    again=again.lower()
    Intentar()




menu()
