import psycopg2

try:
    conexion = psycopg2.connect(
        host = "localhost",  
        port = "5432", 
        user = "postgres", 
        password = "admin",
        dbname = "ejemploclase"
    )
    print("conexión exitosa")
except psycopg2.Error as e:
    print("Ocurrio un error en la conexión")
    print("Verifique los parametros")
cursor = conexion.cursor()

def verHistorial(): 
    SQL = 'SELECT*FROM datos;'
    cursor.execute(SQL)
    valores = cursor.fetchall()
    print(valores)



def main():
    correcto = False
    while(not correcto):
        try:    
            nombre = str(input("Ingrese su nombre: "))
            carnet = int(input("Ingrese su número de carnet: "))
            if carnet > 0:
                cursor.execute("INSERT INTO datos(nombre, carnet) VALUES(%s,%s);",(nombre,carnet))
                conexion.commit()
                print("carnet valido")
            else:
                print("carnet invalido")
            correcto = True
        except ValueError:
            print("Datos ingresados incorrectos")


def pedirNumero():
    correcto = False
    num = 0
    while(not correcto):
        try:
            correcto=True
            num = int(input("Ingrese una opción "))
        except ValueError:
            print("Seleccione una opción válida")
    return num

salir = False   
while not salir:
    print("1. Ejecuto el programa")
    print("2. Ver historial de base de datos")
    print("3. Salir")

    opcion = pedirNumero()

    if opcion == 1:
        main()
    
    elif opcion == 2:
        verHistorial()
    
    elif opcion == 3:
        salir = True

    else: 
        print ("Ingrese una opción válida")

print ("Gracias por utilizar el programa")



cursor.close()
conexion.close()
