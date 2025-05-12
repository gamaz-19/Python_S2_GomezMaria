listaRobusta = [
    {
        "id":1
        "name":"aleja",
        "apellido":"jose",
        "telefono":[
            {
                "codigo":57,
                "telefono":3144795848,
                "tipo":"personal"
            },
            {
                "codigo":1,
                "telefono":6144793448,
                "tipo":"trabajo"
            }
        ],
        "edad":17
    },
    {
        "id":2
        "name":"danny",
        "apellido":"dante",
        "telefono":[
            {
                "codigo":57,
                "telefono":3134795848,
                "tipo":"personal"
            },
            {
                "codigo":1,
                "telefono":6144563448,
                "tipo":"trabajo"
            }
        ],
        "edad":20
    },
    {
        "id":3
        "name":"dan",
        "apellido":"juli",
        "telefono":[
            {
                "codigo":57,
                "telefono":3144723848,
                "tipo":"personal"
            },
            {
                "codigo":1,
                "telefono":6146593448,
                "tipo":"trabajo"
            }
        ],
        "edad":15
    }
]
booleanito = True
while(booleanito):
    print("##############################")
    print("#### Librería de personas ####")
    print("##############################")
    #CRUD (CREATE , READ , UPDATE & DELETE)
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario=int(input("Escoja una opción (Numérica):"))
    if(opcionUsuario==1):
        print("#######################")
        print("#### Crear Persona ####")
        print("#######################")
        diccionarioVacio={}
        print("Ingrese el nombre de la persona")
        nm = int(input())
        print("Ingrese el numero de telefono de la persona")
        num = int(input())
        print("Ingrese la edad de la persona")
        age = int(input())
        diccionarioVacio = {
            "id":len(listaRobusta)+2
            "name":nm,
            "telefono":num,
            "edad":age
        }
        listaRobusta.append(diccionarioVacio)
listaRobusta[0]["name"] = nuevonombre
    elif(opcionUsuario==2):
        for i in range(len(listaRobusta)):
            print("##########################")
            print("#### Persona #",i+1," ####")
            print("##########################")
            print("ID:", listaRobusta[i]["id"])
            print("Nombre:",listaRobusta[i]["name"])
            print("Telefono:",listaRobusta[i]["telefono"])
            print("Edad",listaRobusta[i]["edad"])
            
            for q in range(len(listaRobusta[i]["telefonos"])):
                print("---------------------------")
                print("Telefono#",q+1,":")
                print("#### - Código:",listaRobusta[i]["telefonos"][q]["codigo"])
                print("#### - Numero:",listaRobusta[i]["telefonos"][q]["numero"])
                if(listaRobusta[i]["telefonos"][q]["tipo"] == "personal"):
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                
                print("---------------------------")

            
            
    elif(opcionUsuario==6):
        print("Chaousssss")
        booleanito=False
    else:
        print("No es una opción válida")