datos={}
estado=True
numero=0
while estado==True:
    nombre=input("Ingrese nombre completo ")
    correo=input("In grese su correo ")
    datos[nombre]=correo
    pregunta=input("Desea agregar otro usuario s/n ")
    if pregunta=="s" or pregunta=="S":
        pass
    else:
        estado=False
for x in datos:
    numero=numero+1
    print(str(numero)+" "+ x + "Su correo es " + datos[x])