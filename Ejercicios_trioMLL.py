print("Programa para:\nEncontrar los litros de leche producidos en una semana en la granja, teniendo en cuenta que:\nPor 100m pastados se producen 15L de leche")
##Definir las variables ,y pedir los datos mediante un input para poder trabajar con los datos
##anteriormente transformados en en int
LitrosxVaca= 15
Dias=7
def Litros (Vacas,Dias,LitrosxVaca):
    LitrosxVaca=(Vacas*LitrosxVaca)//1
    x=(Dias*LitrosxVaca)//1
    return(x)
