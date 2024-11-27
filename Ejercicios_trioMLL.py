#@Laura Juliana Rodríguez Ramírez
#@Laura Daniela Marín Barragan
#@Miguel Andres Ordoñez Hernandez

##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int
print("\t\tLA GRANJA PRODUCTIVA\n Bienvenido a la granja, Somos expertos productores de leche y huevos a gran escala.")

print("\nPRODUCCIÓN DE LITROS DE LECHE CORTE SEMANAL.\n")

LitrosxVaca= 15
Dias=7
Vacas = int(input("Digite la cantidad de vacas: "))
def Litros (x,y,z):
     
    z=(x*z)//1
    cantidad=(y*z)//1
    return(cantidad)
print("Se produjeron",Litros(Vacas,Dias,LitrosxVaca),"litros","de leche con ",Vacas," vacas,en una semana de 7 días")
print("\n")
##PROBLEMAS
def huevos():
    print("\nPRODUCCIÓN DE HUEVOS CORTE MENSUAL.\n")
    aves=int(input("Ingrese el numero total de aves que hay en la granja: "))

    gallinas=aves//3
    ponedoras=gallinas//2
    print("\n\tUn tercio de las aves son gallinas ponedoras. ")
    print("\tLa mitad de estas gallinas produce un huevo cada 3 dias y la otra otra mitad 1 cada 5 dias. ")
    p3=ponedoras*10
    p5=ponedoras*6
    print("\nLa gallinas ponen un total de ",p3+p5," huevos en un mes de 30 dias\n")

huevos()

