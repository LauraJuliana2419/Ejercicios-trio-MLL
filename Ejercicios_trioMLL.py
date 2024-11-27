#@Laura Juliana Rodríguez Ramírez
#@Laura Daniela Marín Barragan
#@Miguel Andres Ordoñez Hernandez

print("Programa para:\nEncontrar los litros de leche producidos en una semana en la granja, teniendo en cuenta que:\nPor 100m pastados se producen 15L de leche")
##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int
LitrosxVaca= 15
Dias=7
Vacas = int(input("Digite la cantidad de vacas: "))
def Litros (x,y,z):
     
    z=(x*z)//1
    lol=(y*z)//1
    return(lol)
print("Se produjeron",Litros(Vacas,Dias,LitrosxVaca),"litros","de leche con ",Vacas," vacas,en una semana de 7 días")
##PROBLEMAS
def huevos():
    aves=int(input("Ingrese el numero total de aves que hay en la granja. "))

    gallinas=aves//3
    ponedoras=gallinas//2

    p3=ponedoras*10
    p5=ponedoras*6

    print("La gallinas ponen un total de ",p3+p5," huevos en un mes de 30 dias")

huevos()
print("Prueba de carga")
