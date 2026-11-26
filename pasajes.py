# --- VARIABLES GLOBALES (No se reinician al repetir) ---
# D = disponible, R = reservado, O = ocupado
asientos = [
    ["D", "D", "R", "O"],
    ["D", "O", "D", "D"],
    ["R", "D", "D", "O"],
    ["D", "D", "D", "D"]
]

# colores texto
rojo = "\033[31m"
azul = "\033[34m"
blanco = "\033[37m"
cian = "\033[36m"
verde = "\033[32m"
amarillo = "\033[33m"
magenta = "\033[35m"
cortar = "\033[0m"

# colores fondo
frojo = "\033[41m"
fazul = "\033[44m"
fblanco = "\033[47m"
fcian = "\033[46m"
fverde = "\033[42m"
famarillo = "\033[43m"
fmagenta = "\033[45m"


# --- FUNCIÓN PRINCIPAL DEL PROGRAMA ---
def iniciar_programa():
    # Estas variables SÍ deben reiniciarse en cada compra nueva
    total = 0
    pasaje = 0
    i = 0
    cantidad = 0

    print("")
    print(f" {fcian} Bienvenido a Aeropuerto 24 {cortar} ")
    print("")

    print(f'''{fblanco}Categorías de vuelos:{cortar}
{verde}1. Partida: Calama, Chile, 11/08 a las 11:15 AM - Destino: Sao Paulo, Brazil, 12/08 a las 01:34 PM - Código de vuelo: GBD437
    Costo: $5.600{cortar}
{amarillo}2. Partida: Lima, Perú, 15/08 a las 4:23 PM - Destino: Mendoza, Argentina, 16/08 a las 7:20 AM - Código de vuelo: YUG376
    Costo: $7.200{cortar}
{magenta}3. Partida: Tokio, Japon, 13/08 a las 8:00 AM - Destino: Washington D.C., 14/08 a las 6:50 PM - Código de vuelo: HSG647
    Costo: $6.300{cortar}''')

    op = input("")
    print("")
    print("")

    if (op == "1"):
        pasaje = 5600
        vuelo = "Calama, Chile -> Sao Paulo, Brazil"
        salida = "11/08 a las 11:15 AM"
        llegada = "12/08 a las 01:34 PM"
        codigo = "GBD437"

    if (op == "2"):
        pasaje = 7200
        vuelo = "Lima, Perú - Mendoza, Argentina"
        salida = "15/08 a las 4:23 PM"
        llegada = "16/08 a las 7:20 AM"
        codigo = "YUG376"

    if (op == "3"):  
        pasaje = 6300
        vuelo = "Tokio, Japon -> Washington D.C."
        salida = "13/08 a las 8:00 AM"
        llegada = "14/08 a las 6:50 PM"
        codigo = "HSG647"

    print(f'''{fblanco}Tipo de pasaje:{cortar}
1. Basic: $3.000 Solo con bolso de mano pequeño
2. Light: $7.000 Bolso de mano + maleta pequeña en cabina de hasta 10kg
3. Premium: $13.000 Bolso de mano + maleta en cabina + equipaje en bodega de hasta 23kg + embarque prioritario''')

    op2 = input("")
    print("")
    print("")

    if (op2 == "1"):
        pasaje += 3000
        tarifa = " Basic"

    if (op2 == "2"):
        pasaje += 7000
        tarifa = "Light"

    if (op2 == "3"):     
        pasaje += 13000
        tarifa = "Premium"

    cantidad = int(input(f"{fblanco}Cuantos pasajes desea comprar?{cortar}: "))
    print("")

    while(i < cantidad):

        print(f"{amarillo}Asientos disponibles:{cortar}")
        print(f"{fverde} DISPONIBLE {cortar} - {famarillo} RESERVADO {cortar} - {frojo} OCUPADO {cortar}")

        for fila in range(4):
            print(f"Fila {chr(65 + fila)}: ", end="")
            for columna in range(4):
                estado = asientos[fila][columna]

                if estado == "D":
                    color = fverde
                elif estado == "R":
                    color = famarillo
                else:
                    color = frojo

                print(f"{color} {chr(65 + fila)}{columna + 1} {cortar}", end=" ")
            print()

        while True:
            asiento = input("Elija un asiento disponible [ejemplo A1]: ").upper().strip()

            if len(asiento) == 2 and asiento[0] in "ABCD" and asiento[1] in "1234":
                fila = ord(asiento[0]) - ord("A")
                columna = int(asiento[1]) - 1

                if asientos[fila][columna] == "D":
                    asientos[fila][columna] = "R"
                    print(f"Asiento {asiento} reservado correctamente.")
                    break
                else:
                    print("Ese asiento no está disponible. Elija otro.")
            else:
                print("Asiento no válido. Use una letra de A a D y un número de 1 a 4.")

        # datos personales
        print("")
        rut = int(input("Ingrese su rut: "))
        nmb = input("ingrese su nombre. ")
        genero = input("Ingrese su genero: ")
        edad = int(input("ingrese su edad: "))

        i = i + 1

    print("")
    print("")
    print(f'''{fblanco}Ticket de abordaje confirmado:{cortar}
        {rojo}Pasajero: {nmb}{cortar} / {azul}rut: {rut}{cortar} / {verde}edad: {edad}{cortar} / {cian}genero: {genero}{cortar}
        {fazul}Vuelo: {vuelo}{cortar}
        {fverde}Hora de salida: {salida}{cortar}
        {famarillo}Hora de llegada: {llegada}{cortar}
        {fmagenta}Código de vuelo: {codigo}{cortar}
        {frojo}asiento: {asiento} / tarifa: {tarifa}{cortar}
        total pagado: ${verde}{pasaje}{cortar} CLP
    ''')

    con = input(f"{fblanco}Desea continuar? (si/no):   {cortar}").lower().strip()

    if (con == "si"):
        iniciar_programa() 
    else:
        print("Gracias por usar Aeropuerto 24.")
        exit()


iniciar_programa()
