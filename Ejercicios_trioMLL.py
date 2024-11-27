print("Programa para encontrar los litros de leche producido en una semana en la granja: ")
##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int 
def litros_de_leche():
    vacas = int(input("Digite la cantidad de vacas: "))
    leche = 15
    cantidad = (7*leche)
    litros = vacas * cantidad
    print("Se produjeron ",litros," de leche con ",vacas," vacas")
litros_de_leche()
