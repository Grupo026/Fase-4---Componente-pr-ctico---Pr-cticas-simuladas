# MAIN.py
from clientes import Cliente
from servicios import ReservaSala, AlquilerEquipo
from Reserva import Reserva

print("\n--- CASOS VALIDOS ---")

try:

    cliente1 = Cliente(
        1,
        "Juan",
        "juan@gmail.com",
        "3001234567"
    )

    servicio1 = ReservaSala(
        "S1",
        "Sala de reuniones",
        50000
    )

    reserva1 = Reserva(
        cliente1,
        servicio1,
        2
    )

    reserva1.confirmar()
    reserva1.procesar()

except Exception as e:
    print(e)


print("\n--- CASOS INVALIDOS ---")

# EMAIL INVALIDO
try:

    cliente2 = Cliente(
        2,
        "Ana",
        "correo_mal",
        "12345"
    )

except Exception as e:
    print(e)

# PRECIO NEGATIVO
try:

    servicio2 = ReservaSala(
        "S2",
        "Sala",
        -10
    )

except Exception as e:
    print(e)

# DURACION INVALIDA
try:

    cliente3 = Cliente(
        3,
        "Luis",
        "luis@gmail.com",
        "3001112222"
    )

    servicio3 = AlquilerEquipo(
        "E1",
        "Proyector",
        20
    )

    reserva2 = Reserva(
        cliente3,
        servicio3,
        0
    )

except Exception as e:
    print(e)

# PROCESAR SIN CONFIRMAR
try:

    reserva3 = Reserva(
        cliente3,
        servicio3,
        2
    )

    reserva3.procesar()

except Exception as e:
    print(e)

# CANCELAR DOS VECES
try:

    reserva3.confirmar()

    reserva3.cancelar()

    reserva3.cancelar()

except Exception as e:
    print(e)
