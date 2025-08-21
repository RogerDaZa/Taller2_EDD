import os

class Cliente:
    def __init__(self, cedula, nombre, saldo):
        self.cedula = cedula
        self.nombre = nombre
        self.saldo = float(saldo)

    def __str__(self):
        return f"{self.cedula},{self.nombre},{self.saldo}"

# Archivo donde se guardan los clientes
ARCHIVO = "banco.txt"

# Asegurarse de que el archivo existe
if not os.path.exists(ARCHIVO):
    with open(ARCHIVO, "w") as f:
        pass  # Crear archivo vacío

def ingresar_cliente():
    cedula = input("Escriba la cédula: ")
    nombre = input("Digite su nombre: ")
    saldo = input("Digite el saldo: ")

    cliente = Cliente(cedula, nombre, saldo)
    with open(ARCHIVO, "a") as f:
        f.write(str(cliente) + "\n")
    print("Cliente guardado correctamente en banco.txt")

def buscar_cliente():
    nombre_buscado = input("Digite el nombre del cliente a buscar: ")
    encontrado = False

    with open(ARCHIVO, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                nombre = datos[1]
                saldo = datos[2]
                if nombre.lower() == nombre_buscado.lower():
                    print(f"Cliente encontrado: {nombre} | Saldo: {saldo}")
                    encontrado = True
                    break

    if not encontrado:
        print(f"No se encontró el cliente con nombre: {nombre_buscado}")

def clientes_mayores_50():
    print("Clientes con saldo mayor a 50:")
    alguno = False

    with open(ARCHIVO, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                nombre = datos[1]
                saldo = float(datos[2])
                if saldo > 50:
                    print(f"Nombre: {nombre} | Saldo: {saldo}")
                    alguno = True

    if not alguno:
        print("No hay clientes con saldo mayor a 50.")

def ordenar_por_saldo():
    lista_clientes = []

    with open(ARCHIVO, "r") as f:
        for linea in f:
            datos = linea.strip().split(",")
            if len(datos) == 3:
                lista_clientes.append(Cliente(datos[0], datos[1], datos[2]))

    # Ordenar por saldo
    lista_clientes.sort(key=lambda c: c.saldo)

    print("Clientes ordenados por saldo (ascendente):")
    for c in lista_clientes:
        print(f"{c.nombre} | Saldo: {c.saldo}")

def menu():
    salir = False
    while not salir:
        print("\nBienvenido a ventas, digite la opción:")
        print("1. Ingresar un cliente")
        print("2. Buscar cliente por nombre")
        print("3. Mostrar clientes con saldo > 50")
        print("4. Ordenar clientes por saldo ascendente")
        print("5. Salir")

        opcion = input("Opción: ")

        if opcion == "1":
            ingresar_cliente()
        elif opcion == "2":
            buscar_cliente()
        elif opcion == "3":
            clientes_mayores_50()
        elif opcion == "4":
            ordenar_por_saldo()
        elif opcion == "5":
            salir = True
            print("Usted ha salido del sistema.")
        else:
            print("Opción inválida.")

if __name__ == "__main__":
    menu()  