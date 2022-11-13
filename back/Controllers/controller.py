# Acá ingresaremos el código q funciona como intermediario entre el modelo y la vista.

from Models.model import DAO
from Models import functions


def main_menu():
    advance = True
    while advance:
        correct_option = False
        while not correct_option:
            print("==================== MENÚ PRINCIPAL ====================")
            print("1.- Listar bares")
            print("2.- Registrar bar")
            print("3.- Actualizar bar")
            print("4.- Eliminar bar")
            print("5.- Salir")
            print("========================================================")
            option = int(input("Seleccione una opción: "))

            if option < 1 or option > 5:
                print("Opción incorrecta, ingrese nuevamente...")
            elif option == 5:
                advance = False
                print("¡Gracias por usar este sistema!")
                break
            else:
                correct_option = True
                execute_option(option)


def execute_option(option):
    dao = DAO()

    if option == 1:
        try:
            bares = dao.leer_bares()
            if len(bares) > 0:
                functions.listar_bares(bares)
            else:
                print("No se encontraron bares...")
        except:
            print("Ocurrió un error...")
    elif option == 2:
        bar = functions.pedir_datos_registro()
        try:
            dao.crear_bar(bar)
        except:
            print("Ocurrió un error...")
    elif option == 3:
        try:
            bares = dao.leer_bares()
            if len(bares) > 0:
                bar = functions.pedir_datos_actualizacion(bares)
                if bar:
                    dao.actualizar_bar(bar)
                else:
                    print("Código de bar a actualizar no encontrado...\n")
            else:
                print("No se encontraron bares...")
        except:
            print("Ocurrió un error...")
    elif option == 4:
        try:
            bares = dao.leer_bares()
            if len(bares) > 0:
                codigo = functions.pedir_datos_eliminacion(bares)
                if not(codigo == ""):
                    dao.eliminar_bar(codigo)
                else:
                    print("Código de bar no encontrado...\n")
            else:
                print("No se encontraron bares...")
        except:
            print("Ocurrió un error...")
    else:
        print("Opción no válida...")


main_menu()