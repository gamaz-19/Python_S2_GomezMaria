################################
####### Gestion de Datos #######
################################


# CRUD : Create, Read, Update, Delete

'''



Gestión de Datos de Artistas Musicales:

1. Artista
    1.1 Registrar artista
        1.1.1. Nombre del artista.
        1.1.2 País de origen (nombre, código ISO3).
        1.1.3. Años de actividad.
        1.1.4. Año de lanzamiento del primer disco que llegó a las listas.
        1.1.5. Género musical.
        1.1.6 Unidades certificadas totales.
        1.1.7 Ventas reclamadas.
        1.1.8 Estado del artista (si está activo o no).
    1.2 Consultar artistas
        1.2.1 Todos los artistas
    1.3 Editar artista
        1.3.1. Nombre del artista.
        1.3.2 País de origen (nombre, código ISO3).
        1.3.3. Años de actividad.
        1.3.4. Año de lanzamiento del primer disco que llegó a las listas.
        1.3.5. Género musical.
        1.3.6 Unidades certificadas totales.
        1.3.7 Ventas reclamadas.
        1.3.8 Estado del artista (si está activo o no).
    1.4 Eliminar artista

2. Paises y Generos Musicales
    2.1. Países: 
        2.1.1. Consultar paises
        2.1.2. Consultar un pais
        2.1.3. Editar pais

    2.2.Géneros Musicales: 
        2.2.1 ID del género.
        2.2.1 Descripción del género.

3. Generación de Informes:
    (Informes de artistas: Listado de todos los datos de artistas musicales para un país específico en un período de
    tiempo específico, incluyendo detalles de años de actividad y unidades certificadas. Informes de ventas
    musicales: Listado de las unidades certificadas y ventas reclamadas año a año para un artista específico)


4. Módulo de Reportes:
    4.1. Obtener todos los datos de artistas musicales para Reino Unido desde 1960 hasta 1970.
    4.2. Datos de artistas musicales para el género "Rock/pop"
    4.3. Obtener los datos de artistas musicales de los últimos 10 años para todos los países.
    4.4. Número de registros de artistas por año.
    4.5. Unidades certificadas totales registradas para todos los países en 2023.

'''
booleanito = True
while ( booleanito ):
    print ( " ##################################################" )
    print ( " ##### Gestión de Datos de Artistas Musicales #####" )
    print ( " ################## 1. Artistas ###################" )
    print ( " ########## 2. Paises y Generos musicales #########" )
    print ( " ############ 3. Generacion de Informes ###########" )
    print ( " ################### 4. Reportes ##################" )
    menuprincipal = (int (input ( "Ingrese el numero de la opcion que quiere seleccionar: " )))
    if ( menuprincipal == 1 ):
            print (" ################## 1. Artistas ###################")
            print (" 1. Registrar artista \n 2. Ver artistas \n 3. Editar artista \n 4. Eliminar artista ")
            artista = ( int (input (" Ingrese el numero de la opcion que quiere seleccionar" )))
            if ( artista == 1 ):
                    print ( " 1. Crear artista ")
            elif ( artista == 2 ):
                    print ( " 2. Todos los artistas ")
            elif ( artista == 3 ):
                    print ( " 3. Ver un artista ")
            elif ( artista == 4 ):
                    print ( " 4. Editar artista ")
            elif ( artista == 5 ):
                    print ( " 5. Eliminar artista ")

    elif ( menuprincipal == 2 ):
            print (" ########## 2. Paises y Generos musicales #########" )
            print (" 1. Paises \n 2. Generos musicales ")
            paisGenero = ( int (input (" Ingrese el numero de la opcion que quiere seleccionar" )))
            if ( paisGenero== 1 ):
                print ( " Paises ")
                print ( " 1. Ver todos los paises \n 2. Ver un pais \n 3. Editar pais ")
                paisOpcion = ( int (input (" Ingrese el numero de la opcion que quiere seleccionar" )))
                if ( paisOpcion== 1 ):
                        print ( " 1. Ver todos los paises ")
                elif ( paisOpcion == 2 ):
                        print ( " 2. Ver un pais ")
                elif ( paisOpcion == 3 ):
                        print ( " 3. Editar pais ")

            elif ( paisGenero == 2 ):
                print ( " Generos musicales ")
                print ( " 1. Ver todos los generos musicales \n 2. Ver un genero musical y su descripcion")
                generoOpcion = ( int (input (" Ingrese el numero de la opcion que quiere seleccionar" )))
                if ( generoOpcion == 1 ):
                        print ( " 1. Ver todos los generos musicales ") 
                elif ( generoOpcion  == 2 ):
                        print ( " 2. Ver un genero musical y su descripcion")
    elif ( menuprincipal == 3 ):
        print ( " ")
    elif ( menuprincipal == 4 ):
        print ( " " )

















# pass instruccion nula que se usa como marcador de posicion cuando se requiere una sintazizs valida pero on se desea ejecutar ninguna accion 


