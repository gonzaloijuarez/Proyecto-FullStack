def listar_bares(bares):
    print("\nBares: \n")
    count = 1
    for bar in bares:
        data = "{0}. Código: {1} | Nombre: {2} | Dirección: {3}"
        print(data.format(count, bar[0], bar[1], bar[2]))
        count += 1
    print(" ")


def pedir_datos_registro():
    codigo_correcto = False
    codigo=""
    while(not codigo_correcto):
        codigo = input("Ingrese código: ")
        if len(codigo) > 1:
            codigo_correcto = True
        else:
            print("Código incorrecto: Debe tener al menos un digito.")

    nombre = input("Ingrese nombre: ")

    direccion = input("Ingrese dirección: ")

    bar = (codigo, nombre, direccion)
    return bar

def pedir_datos_actualizacion(bares):
    listar_bares(bares)
    existe_codigo = False
    codigo_editar = input("Ingrese el código del bar a editar: ")
    for bar in bares:
        if bar[0] == codigo_editar:
            existe_codigo = True
            break

    if existe_codigo:
        nombre = input("Ingrese nuevo nombre: ")
        direccion = input("Ingrese nueva dirección: ")

        bar = (codigo_editar, nombre, direccion)
    else:
        bar = None

    return bar


def pedir_datos_eliminacion(bares):
    listar_bares(bares)
    existe_codigo = False
    codigo_eliminar = input("Ingrese el código del bar a eliminar: ")
    for bar in bares:
        if bar[0] == codigo_eliminar:
            existe_codigo = True
            break

    if not existe_codigo:
        codigo_eliminar = ""

    return codigo_eliminar