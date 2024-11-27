print("Programa para encontrar los litros de leche producido en una semana en la granja: ")
##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int



#Problema huevos

def huevos():
    aves=int(input("Ingrese el numero total de aves que hay en la granja. "))

    gallinas=aves//3
    ponedoras=gallinas//2

    p3=ponedoras*10
    p5=ponedoras*6

    print("La gallinas ponen un total de ",p3+p5," huevos en un mes de 30 dias")

huevos()
print("Programa para:\nEncontrar los litros de leche producidos en una semana en la granja, teniendo en cuenta que:\nPor 100m pastados se producen 15L de leche")
##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int
LitrosxVaca= 15
Dias=7
def Litros (Vacas,Dias,LitrosxVaca):
    LitrosxVaca=(Vacas*LitrosxVaca)//1
    x=(Dias*LitrosxVaca)//1
    return(x)